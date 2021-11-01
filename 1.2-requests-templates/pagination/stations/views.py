import urllib
from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    data_station = []
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for station in reader:
            dict_station = {'Name': station['Name'],
                'Street': station['Street'],
                'District': station['District']}
            data_station.append(dict_station)
    paginator = Paginator(data_station, 10)
    current_page = int(request.GET.get('page', 1))
    stations = paginator.get_page(current_page)
    if stations.has_previous():
        prev_page_url = reverse('bus_stations') + "?" + urllib.parse.urlencode({'page': stations.previous_page_number()})
    else:
        prev_page_url = None
    if stations.has_next():
        next_page_url = reverse('bus_stations') + "?" + urllib.parse.urlencode({'page': stations.next_page_number()})
    else:
        next_page_url = None

    context = {
        'bus_stations': stations,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }
    return render(request, 'stations/index.html', context)
