from django.shortcuts import render,get_object_or_404, redirect
from .models import Formation,UE
from .forms import UEForm


# Create your views here.


def about(request):
    return render(request,"uo/about.html")


def formation_detail(request, n):
    formation = get_object_or_404(Formation, pk=n)
    ues = formation.ue_set.all()  

    return render(request, 'uo/formation_detail.html', {'formation': formation, 'ues': ues})

def ue_detail(request, m):
    ue = get_object_or_404(UE, id=m)
    formations = ue.formations.all()

    return render(request, 'uo/ue_detail.html', {'ue': ue, 'formations': formations})

def formation_list(request):
    formations = Formation.objects.all()
    return render(request, 'uo/formation_list.html', {'formations': formations})

def ue_list(request):
    ues = UE.objects.all()
    return render(request, 'uo/ue_list.html', {'ues': ues})

def ue_add(request):
    if request.method == 'POST':
        form = UEForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ue_list')
    else:
        form = UEForm()
    return render(request, 'uo/ue_add.html', {'form': form})

def home(request):
    return render(request, 'uo/home.html')