from django.contrib import admin

from .models import BookAppointment, Qrcode


class BookAppointmentAdminSite(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'people')
    list_display_links = ('name', 'email')


class QrcodeBookApp(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'people')
    list_display_links = ('name', 'email')


admin.site.register(BookAppointment, BookAppointmentAdminSite)
admin.site.register(Qrcode, QrcodeBookApp)
