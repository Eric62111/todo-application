
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm


# Display all tasks
def task_list(request):
    tasks = Todo.objects.all()

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks
    })


# Display one task
def task_detail(request, pk):
    task = get_object_or_404(Todo, pk=pk)

    return render(request, 'tasks/task_detail.html', {
        'task': task
    })


# Create a new task
def task_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')

    else:
        form = TodoForm()

    return render(request, 'tasks/task_form.html', {
        'form': form,
        'action': 'Create'
    })


# Update an existing task
def task_update(request, pk):
    task = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('tasks:task_detail', pk=task.pk)

    else:
        form = TodoForm(instance=task)

    return render(request, 'tasks/task_form.html', {
        'form': form,
        'action': 'Update',
        'task': task
    })


# Delete a task after confirmation
def task_delete(request, pk):
    task = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')

    return render(request, 'tasks/task_confirm_delete.html', {
        'task': task
    })
