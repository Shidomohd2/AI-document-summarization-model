from django import forms
from .models import DocumentSession

class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentSession
        fields = ('file',)

    def clean_file(self):
        file = self.cleaned_data.get('file')
        valid_exts = ['.pdf', '.txt', '.pptx', '.docx', '.png', '.jpg', '.jpeg']
        if not any(file.name.lower().endswith(ext) for ext in valid_exts):
            raise forms.ValidationError("Unsupported file format")
        return file

class ChatMessageForm(forms.Form):
    content = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter page number or ask something...'})
    )