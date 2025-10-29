from django.contrib import admin

# Register your models here.

from.models import Profile,Posts,Interested

admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(Interested)

