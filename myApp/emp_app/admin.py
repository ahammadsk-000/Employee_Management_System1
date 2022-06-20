from django.contrib import admin
from .models import Employee,Department,Role
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','dept','salary','bonus','role','phone','hire_date')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','location')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)


