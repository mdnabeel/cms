from django.shortcuts import render
from django.http import HttpResponse
from .models import FaultDetail
from django.shortcuts import redirect

# Create your views here.


# def index(request):
#     return render(request, 'cms/index.html')


def index(request):
    odisputedcount = FaultDetail.objects.filter(status_id="Disputed").count()
    return render(request, '/home.html', {'odisputedcount': odisputedcount})


def disputed(request):
    disputedfault = FaultDetail.objects.filter(status_id="Disputed")
    disputedcount = FaultDetail.objects.filter(status_id="Disputed").count()
    return render(request, 'cms/details.html', {'disputedfault': disputedfault, 'disputedcount': disputedcount})


def regfault(request):
    return HttpResponse('/admin')


def pending(request):
    pendfault = FaultDetail.objects.filter(status_id="Pending")
    pendcount = FaultDetail.objects.filter(status_id="Pending").count()
    return render(request, 'cms/details.html', {'pendfault': pendfault, 'pendcount': pendcount})


def rectified(request):
    rectify = FaultDetail.objects.filter(status_id="Rectified")
    rectifycount = FaultDetail.objects.filter(status_id="Rectified").count()
    return render(request, 'cms/details.html', {'rectify': rectify, 'rectifycount': rectifycount})


def observation(request):
    observe = FaultDetail.objects.filter(status_id="Under Observation")
    observecount = FaultDetail.objects.filter(
        status_id="Under Observation").count()
    return render(request, 'cms/details.html', {'observe': observe, 'observecount': observecount})


def azadpur(request):
    azpfaults = FaultDetail.objects.filter(station_id="Azadpur")
    azppendcount = FaultDetail.objects.filter(
        station_id="Azadpur", status_id="Pending").count()
    azprectcount = FaultDetail.objects.filter(
        station_id="Azadpur", status_id="Rectify").count()
    azpdisputecount = FaultDetail.objects.filter(
        station_id="Azadpur", status_id="Disputed").count()
    azpundrobscount = FaultDetail.objects.filter(
        station_id="Azadpur", status_id="Under Observation").count()
    return render(request, 'cms/details.html', {'azpfaults': azpfaults, 'azppendcount': azppendcount,
                                                'azprectcount': azprectcount, 'azpdisputecount': azpdisputecount,
                                                'azpundrobscount': azpundrobscount})


def shalimar(request):
    slmfaults = FaultDetail.objects.filter(station_id="Shalimar Bagh")
    slmpendcount = FaultDetail.objects.filter(
        station_id="Shalimar Bagh", status_id="Pending").count()
    slmrectcount = FaultDetail.objects.filter(
        station_id="Shalimar Bagh", status_id="Rectify").count()
    slmdisputecount = FaultDetail.objects.filter(
        station_id="Shalimar Bagh", status_id="Disputed").count()
    slmundrobscount = FaultDetail.objects.filter(
        station_id="Shalimar Bagh", status_id="Under Observation").count()
    return render(request, 'cms/details.html', {'slmfaults': slmfaults, 'slmpendcount': slmpendcount,
                                                'slmrectcount': slmrectcount, 'slmdisputecount': slmdisputecount,
                                                'slmundrobscount': slmundrobscount})


def nsp(request):
    nspfaults = FaultDetail.objects.filter(station_id="Netaji Subhash Place")
    nsppendcount = FaultDetail.objects.filter(
        station_id="Netaji Subhash Place", status_id="Pending").count()
    nsprectcount = FaultDetail.objects.filter(
        station_id="Netaji Subhash Place", status_id="Rectify").count()
    nspdisputecount = FaultDetail.objects.filter(
        station_id="Netaji Subhash Place", status_id="Disputed").count()
    nspundrobscount = FaultDetail.objects.filter(
        station_id="Netaji Subhash Place", status_id="Under Observation").count()
    return render(request, 'cms/details.html', {'nspfaults': nspfaults, 'nsppendcount': nsppendcount,
                                                'nsprectcount': nsprectcount, 'nspdisputecount': nspdisputecount,
                                                'nspundrobscount': nspundrobscount})


def naraina(request):
    naifaults = FaultDetail.objects.filter(station_id="Naraina Vihar")
    naipendcount = FaultDetail.objects.filter(
        station_id="Naraina Vihar", status_id="Pending").count()
    nairectcount = FaultDetail.objects.filter(
        station_id="Naraina Vihar", status_id="Rectify").count()
    naidisputecount = FaultDetail.objects.filter(
        station_id="Naraina Vihar", status_id="Disputed").count()
    naiundrobscount = FaultDetail.objects.filter(
        station_id="Naraina Vihar", status_id="Under Observation").count()
    return render(request, 'cms/details.html', {'naifaults': naifaults, 'naipendcount': naipendcount,
                                                'nairectcount': nairectcount, 'naidisputecount': naidisputecount,
                                                'naiundrobscount': naiundrobscount})


def bms(request):
    bmsfaults = FaultDetail.objects.filter(department_id="BMS")
    bmspendcount = FaultDetail.objects.filter(
        department_id="BMS", status_id="Pending").count()
    bmsrectcount = FaultDetail.objects.filter(
        department_id="BMS", status_id="Rectify").count()
    bmsdisputecount = FaultDetail.objects.filter(
        department_id="BMS", status_id="Disputed").count()
    bmsundrobscount = FaultDetail.objects.filter(
        department_id="BMS", status_id="Under Observation").count()
    return render(request, 'cms/details.html', {'bmsfaults': bmsfaults, 'bmspendcount': bmspendcount,
                                                'bmsrectcount': bmsrectcount, 'bmsdisputecount': bmsdisputecount,
                                                'bmsundrobscount': bmsundrobscount})


def elect(request):
    electfaults = FaultDetail.objects.filter(department_id="Electrical")
    electpendcount = FaultDetail.objects.filter(
        department_id="Electrical", status_id="Pending").count()
    electrectcount = FaultDetail.objects.filter(
        department_id="Electrical", status_id="Rectify").count()
    electdisputecount = FaultDetail.objects.filter(
        department_id="Electrical", status_id="Disputed").count()
    electundrobscount = FaultDetail.objects.filter(
        department_id="Electrical", status_id="Under Observation").count()
    return render(request, 'cms/details.html', {'electfaults': electfaults, 'electpendcount': electpendcount,
                                                'electrectcount': electrectcount, 'electdisputecount': electdisputecount,
                                                'electundrobscount': electundrobscount})


def ecs(request):
    ecsfaults = FaultDetail.objects.filter(department_id="ECS")
    ecspendcount = FaultDetail.objects.filter(
        department_id="ECS", status_id="Pending").count()
    ecsrectcount = FaultDetail.objects.filter(
        department_id="ECS", status_id="Rectify").count()
    ecsdisputecount = FaultDetail.objects.filter(
        department_id="ECS", status_id="Disputed").count()
    ecsundrobscount = FaultDetail.objects.filter(
        department_id="ECS", status_id="Under Observation").count()
    return render(request, 'cms/details.html', {'ecsfaults': ecsfaults, 'ecspendcount': ecspendcount,
                                                'ecsrectcount': ecsrectcount, 'ecsdisputecount': ecsdisputecount,
                                                'ecsundrobscount': ecsundrobscount})


def tvs(request):
    tvsfaults = FaultDetail.objects.filter(department_id="TVS")
    tvspendcount = FaultDetail.objects.filter(
        department_id="TVS", status_id="Pending").count()
    tvsrectcount = FaultDetail.objects.filter(
        department_id="TVS", status_id="Rectify").count()
    tvsdisputecount = FaultDetail.objects.filter(
        department_id="TVS", status_id="Disputed").count()
    tvsundrobscount = FaultDetail.objects.filter(
        department_id="TVS", status_id="Under Observation").count()
    return render(request, 'cms/details.html', {'tvsfaults': tvsfaults, 'tvspendcount': tvspendcount,
                                                'tvsrectcount': tvsrectcount, 'tvsdisputecount': tvsdisputecount,
                                                'tvsundrobscount': tvsundrobscount})


def linked(request):
    return redirect("https://www.linkedin.com/in/mohammad-nabeel-2a759695/")
