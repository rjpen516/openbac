from django.contrib import admin
from django.contrib.admin import helpers
from django.template.response import TemplateResponse
from .models import UnregisteredDevice

# Register your models here.





class UnregisteredDeviceAdmin(admin.ModelAdmin):

    def convert_unregistered_to_reg(self, request, queryset):
        if request.POST.get('post'):
                # process the queryset here
                pass
        else:
            context = {
                'title': ("Add new device to system"),
                'queryset': queryset[0],
                'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
            }
            return TemplateResponse(request, 'add_device.html',
                context)

    convert_unregistered_to_reg.short_description = "Register Device"
    actions = [convert_unregistered_to_reg]

admin.site.register(UnregisteredDevice,UnregisteredDeviceAdmin)
