from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from blog.models import Post,Contact
class SignupForm(UserCreationForm):
    password1=forms.CharField(label="Enter Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Enter Password Again",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]
        labels={'first_name':"First Name","last_name":"Last Name","email":"Enter your Email" }
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 }

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':True}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':"current-password",'strip':False}))
    
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title","desc",]
        labels={"desc":"Description"}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 "desc":forms.Textarea(attrs={"class":"form-control"}),                
                 }
        # "author":forms.TextInput(attrs={"class":"form-control"})
