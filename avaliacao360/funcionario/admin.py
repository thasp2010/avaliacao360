from django.contrib import admin
from models import Funcionario
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class FuncionarioInline(admin.StackedInline):
	model = Funcionario
	can_delete = True
	verbose_name_plural = 'funcionarios'

class UserAdmin(UserAdmin):
    inlines = (FuncionarioInline, )

admin.site.register(Funcionario)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

