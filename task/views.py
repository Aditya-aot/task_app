
from django.shortcuts import render
from .models import task_model
from .forms import TaskForm
# Create your views here.

def home(request):
    form = TaskForm()
    task_data = task_model.objects.all()

    context = { 'form':form ,
                'task_data' : task_data

    }


    return render(request, 'home.html', context)

