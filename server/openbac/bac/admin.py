from django.contrib import admin
from .models import Reader, Relay, Location, Access_group, Event, Action
# Register your models here.

admin.site.register(Reader)
admin.site.register(Relay)
admin.site.register(Location)
admin.site.register(Access_group)
admin.site.register(Event)
admin.site.register(Action)
