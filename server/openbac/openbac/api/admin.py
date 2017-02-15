from django.contrib import admin
from django.contrib.admin import helpers
from django.template.response import TemplateResponse
from django.template import RequestContext
from .models import UnregisteredDevice
from openbac.bac.models import Location, Reader, Relay
# Register your models here.
from django import forms
from django.shortcuts import render_to_response
import datetime



class UnregisteredDeviceAdmin(admin.ModelAdmin):

    def convert_unregistered_to_reg(self, request, queryset):
        print "Doing shit"
        if 'apply' in request.POST:
                # process the queryset here
                ty = request.POST['type']
                name = request.POST['name']
                location = request.POST['location']

                new_obj = None
                if ty == 'reader':
                    new_obj = Reader()
                elif ty == 'relay':
                    new_obj = Relay()
                else:
                    return

                new_obj.install_date = datetime.datetime.now()
                new_obj.name = name
                new_obj.mac = queryset[0]
                new_obj.save()
                self.message_user(request, "Successfully Created Device")
                return HttpResponseRedirect(request.get_full_path())

        else:
            locations = Location.objects.all()
            context = {
                'title': ("Add new device to system"),
                'queryset': queryset[0],
                'locations': locations,
                'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
            }
            return render_to_response('add_device.html',
                context=context)

    convert_unregistered_to_reg.short_description = "Register Device"
    actions = [convert_unregistered_to_reg]

admin.site.register(UnregisteredDevice,UnregisteredDeviceAdmin)
