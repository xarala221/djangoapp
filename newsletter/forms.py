from django import forms

from newsletter.models import Join

class JoinForm(forms.ModelForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={"placeholder": "Your email", "class": "form-control sign-up-email"}))
    class Meta:
        model = Join
        fields = ['email']

    def clean_email(self, *args, **kwrgs):
        email = self.cleaned_data.get("email")

        qs = Join.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already exist")
        return email
