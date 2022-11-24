from django.contrib import admin

# Register your models here.

from hello.models import Person, Fly

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Fly)
class FlyAdmin(admin.ModelAdmin):
    pass