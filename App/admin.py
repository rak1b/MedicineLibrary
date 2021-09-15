from django.contrib import admin
from .models import Medicine,Medicine_Group

# Register your models here.

@admin.register(Medicine)
class medicineAdmin(admin.ModelAdmin):
    list_display = ['name','power','group','price']
    def group(self, instance):
            return instance.group.name
@admin.register(Medicine_Group)
class groupAdmin(admin.ModelAdmin):
    list_display = ['name']
    

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     fields=('id','username','first_name','last_name','password','email','phone')
#     list_display = ['username','first_name','last_name','email',]
    #   list_display = ['name','email','password']
    # def name(self):
    #         return self.first_name + self.last_name
