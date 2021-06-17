from django import forms
from django.forms import EmailInput
from django.core.mail import send_mail
from django.forms import ModelForm
from .models import Contacts, Post, Comment


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )


class ContactsCreate(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('name', 'email', 'phone',)

    def send_email(self):
        send_mail(
            self.cleaned_data['name'],
            str(self.cleaned_data['phone']),
            self.cleaned_data['email'],
            ['to@example.com'],
            fail_silently=False,
        )


class UpdateРоstForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'categories', 'memmo']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']

    def get_initial(self):
        """Return the initial data to use for forms on this view."""
        import pdb
        pdb.set_trace()

        return self.initial.copy()

# class ContactsCreate(forms.Form):
#     name = forms.CharField(
#         max_length=60,
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#             "placeholder": "Your Name"
#         })
#     )
#     email = forms.EmailField(
#         widget=EmailInput())
#     phone = forms.IntegerField()


    # def send_email(self):
    #     send_mail(
    #         self.cleaned_data['name'],
    #         str(self.cleaned_data['phone']),
    #         self.cleaned_data['email'],
    #         ['to@example.com'],
    #         fail_silently=False,
    #     )
