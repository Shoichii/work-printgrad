from django.contrib import admin
from .models import Candidate, Citizenships
import pytz
from django.utils import timezone
from django.utils.html import format_html
from django.contrib import admin


# class CityVacancyInline(admin.TabularInline):
#     model = CitiesVacancies


# @admin.register(Cities)
# class CityAdmin(admin.ModelAdmin):
#     inlines = [CityVacancyInline]


# @admin.register(Vacancies)
# class VacancyAdmin(admin.ModelAdmin):
#     inlines = [CityVacancyInline]
#     list_display = ('name', 'responsibilities', 'requirements', 'conditions')


# @admin.register(CitiesVacancies)
# class CityVacancyAdmin(admin.ModelAdmin):
#     list_display = ('city', 'vacancy')
#     list_filter = ('city', 'vacancy')


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('status', 'start_date_display', 'status_date_display','first_name',
                    'phone',  'citizenship', 'custom_citizenship', 'resume_link', 'resume_file')
    list_filter = ('status', 'start_date', 'status_date', 'first_name',
                    'phone',  'citizenship', 'custom_citizenship', 'note')
    list_display_links = ('status', 'start_date_display', 'status_date_display')
    readonly_fields = ('start_date', 'status_date')

    def start_date_display(self, obj):
        tz = pytz.timezone('Europe/Moscow')
        start_date_local = timezone.localtime(obj.start_date, tz)
        obj.start_date = start_date_local.strftime("%H:%M %d.%m.%Y")
        start_date = obj.start_date
        return format_html(
            '<b>{}</b>',
            start_date,
        )
    start_date_display.short_description = 'Время создания'
    start_date_display.admin_order_field = "start_date"

    def status_date_display(self, obj):
        if obj.status_date:
            tz = pytz.timezone('Europe/Moscow')
            start_date_local = timezone.localtime(obj.status_date, tz)
            obj.status_date = start_date_local.strftime("%H:%M %d.%m.%Y")
            status_date = obj.status_date
            return format_html(
            '<b>{}</b>',
            status_date,
        )
    status_date_display.short_description = 'Время смены статуса'
    status_date_display.admin_order_field = "start_date"
    


# @admin.register(Citizenships)
# class CitizenshipsAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     list_filter = ('name',)
