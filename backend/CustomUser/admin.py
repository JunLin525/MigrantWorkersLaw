from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm,UserCreationForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display=[
        "email",
        "username",
        "age",
        "birthday",
        "is_staff"
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age","birthday")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{"fields":("age","birthday")}),)


admin.site.register(CustomUser,CustomUserAdmin)
