from django.shortcuts import render
from complaints.models import FaultDetail


def home(request):
    labels = []
    data = []

    queryset = FaultDetail.objects.all()
    for FaultDetail in queryset:
        labels.append(FaultDetail.station)
        data.append(FaultDetail.fault_no)

    return render(request, 'home.html', {
        'labels': labels,
        'data': data,
    })


def home(request):
    return render(request, 'home.html')
