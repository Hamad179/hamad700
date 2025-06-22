from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasts/tasks_list.html', {'tasks': tasks})


def add_task(request):
    # إضافة مهمة جديدة
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # يمكن تغييره إلى redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasts/taks1.html', {'form': form})
