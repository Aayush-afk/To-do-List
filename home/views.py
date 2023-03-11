from multiprocessing import context
from django.shortcuts import render, HttpResponse
from home.models import Tasks

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":

        title = request.POST['title']
        description = request.POST['description']
        ins = Tasks(task_title=title, task_desc = description)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html', context)

def task(request):
    all_tasks = Tasks.objects.all()
    context = {'tasks': all_tasks}
    return render(request, 'task.html', context)