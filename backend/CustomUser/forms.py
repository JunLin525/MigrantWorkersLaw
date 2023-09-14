from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields= UserCreationForm.Meta.fields+("age", "birthday")

class CustomerUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model=CustomUser
        fields= UserChangeForm.Meta.fields
