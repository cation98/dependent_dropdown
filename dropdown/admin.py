from django.contrib import admin

# Register your models here.
from dropdown.models import Country, Person, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass



@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
