from django import forms
from home.models import CustomUser, CV





class CVCreationForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['work_experience', 'education', 'skills', 'achievements', 'certifications', 'references']
        widgets = {
            'work_experience': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'education': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'skills': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'achievements': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'certifications': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'references': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }

    # Clean data and convert non-bytes to bytes if necessary
    def clean(self):
        cleaned_data = super().clean()
        for field, value in cleaned_data.items():
            # Check if field value is already a byte type or can be encoded
            if not isinstance(value, bytes) and not hasattr(value, "encode"):
                raise forms.ValidationError(f"Field '{field}' must be a byte string or support encoding.")
            # If not, attempt to encode it
            try:
                # Encode the value and then decode it back into a string
                cleaned_data[field] = value.encode().decode('utf-8').replace('\r\n', ' ')
            except Exception as e:
                raise forms.ValidationError(f"Error encoding field '{field}': {e}")
        return cleaned_data







class CustomUserForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email',  'phone_number','first_name' ,'last_name','address']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

