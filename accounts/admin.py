from django.contrib import admin

from accounts.models import *

admin.site.register(Province)
admin.site.register(City)
admin.site.register(CustomUser)
admin.site.register(UserProfile)
