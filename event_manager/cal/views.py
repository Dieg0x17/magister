from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from datetime import datetime, date
from .models import *
from .utils import Calendar

from .forms import EventForm

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('fecha', None))

        profesor = self.request.GET.get('profesor', None)
        grupo = self.request.GET.get('grupo', None)

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        events = Event.objects.filter(hora_inicio__year=d.year, hora_inicio__month=d.month)
        if profesor:
            events = events.filter(profesor=profesor)
        if grupo:
            events = events.filter(grupo=grupo)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True, events=events)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def index(request):
    context = {}
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Evento guardado con exito.')
        else:
            return HttpResponse('Error de formato.')
    else:
        form = EventForm()
        context = {
            'form': form,
        }
    return render(request, 'input.html', context)