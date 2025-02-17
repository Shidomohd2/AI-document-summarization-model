# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import DocumentSession, ChatMessage
from .forms import DocumentForm, ChatMessageForm
from .utils import process_file, extract_pages  # Import the functions
import uuid
import os
import json

def chat_view(request):
    session_id = request.session.get('chat_session')
    chat_session = None
    
    if request.method == 'POST' and 'file' in request.FILES:
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            fs = FileSystemStorage()
            uploaded_file = request.FILES['file']
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = fs.path(filename)
            
            try:
                # Extract pages from the uploaded file
                pages = extract_pages(file_path)
                
                # Create a new DocumentSession
                chat_session = DocumentSession.objects.create(
                    session_key=str(uuid.uuid4()),
                    file=uploaded_file,
                    pages=json.dumps(pages)  # Store pages as JSON
                )
                request.session['chat_session'] = chat_session.id
                
                # Create initial AI message
                ChatMessage.objects.create(
                    session=chat_session,
                    content="I've received your document! Which page number would you like me to summarize?",
                    is_user=False
                )
                
                return JsonResponse({'status': 'success', 'session_id': chat_session.id})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)
    
    elif request.method == 'POST' and session_id:
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_session = get_object_or_404(DocumentSession, id=session_id)
            user_message = form.cleaned_data['content']
            
            # Save user message
            ChatMessage.objects.create(
                session=chat_session,
                content=user_message,
                is_user=True
            )
            
            # Process message
            try:
                page_number = int(user_message)
                pages = json.loads(chat_session.pages)
                if 1 <= page_number <= len(pages):
                    summary = process_file(pages[page_number - 1])
                    response = f"Summary of page {page_number}:\n{summary}"
                else:
                    response = f"Please enter a valid page number between 1 and {len(pages)}."
            except ValueError:
                response = "Please enter a valid page number."
            
            # Save AI response
            ChatMessage.objects.create(
                session=chat_session,
                content=response,
                is_user=False
            )
            
            return JsonResponse({'status': 'success', 'response': response})
    
    return render(request, 'ai_model/chat.html', {'form': ChatMessageForm()})

def load_chat_history(request):
    session_id = request.session.get('chat_session')
    if session_id:
        chat_session = get_object_or_404(DocumentSession, id=session_id)
        messages = chat_session.chatmessage_set.all().order_by('timestamp')
        return render(request, 'ai_model/chat_message.html', {'messages': messages})
    return JsonResponse({'status': 'error'})