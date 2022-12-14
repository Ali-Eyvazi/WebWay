from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm,USerChangeForm
from .models import OtpCode, User
from django.contrib.auth.models import Group

class UserAdmin(BaseUserAdmin):
    form=USerChangeForm
    add_form=UserCreationForm

    list_display=('email','phone_number','is_admin',)
    list_filter=('is_admin',)

    fieldsets=(
        (None,{'fields':('email','phone_number','full_name','password'),}),
        ('permissions',{'fields':('is_active','is_admin','is_superuser','last_login','groups','user_permissions'),})
    
    
    )

    add_fieldsets=(

        (None,{'fields':('phone_number','email','full_name','password1','password2')})

    )


    search_fields= ('email','full_name',)
    ordering=('full_name',)
    filter_horizontal=('groups','user_permissions')




admin.site.register(User,UserAdmin)



@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display= ('phone_number','code','created')











    