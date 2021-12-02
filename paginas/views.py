from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'paginas/list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'paginas/task.html', {'task':task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'paginas/addtask.html', {'form': form})

def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'paginas/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'paginas/edittask.html', {'form': form, 'task': task})

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('/')



class PaginaInicial(TemplateView):
    template_name = 'index.html'


def yourName(request, name):
    return render(request, 'paginas/yourname.html', {'name': name})