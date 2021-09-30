from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from dropdown.forms import PersonForm
from dropdown.models import Person, City


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'  # It's just a human-understandable name of variable to access from templates


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    # fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


def load_cities(request):
    country_id = request.GET.get('country')
    print(country_id)
    cities = City.objects.filter(country=country_id).order_by('name')

    return render(request,
                  'dropdown/city_dropdown_list_options.html',
                  {'cities' : cities})




