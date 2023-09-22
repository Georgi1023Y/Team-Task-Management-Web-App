from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks, Team
from pytz import timezone as pytz_timezone
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.http import Http404
from django.contrib.auth.hashers import make_password

# This function renders index.html page and renders tasks from all_tasks list
def home(request):
    all_tasks = Tasks.objects.all()
    return render(request, 'index.html', {'tasks': all_tasks})

# This function is used to add task
def add_task(request):
    if request.method == 'POST':
        # Gets the title and description on the task user wants to add
        task_title = request.POST.get('title')
        task_description = request.POST.get('description')
         # Define the target timezone (Bulgarian Time - EET)
        target_timezone = pytz_timezone('Europe/Sofia')
        # Get the current date and time in the target timezone
        date = timezone.now().astimezone(target_timezone)
        task = f"{task_title} - {task_description} - {date}"
        # Create a new task instance and save it into the Tasks database
        task_instance = Tasks(name=task_title, description=task_description, time=date)
        task_instance.save()
        return redirect('home')
    return render(request, 'index.html')

def enter_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('teamName')
        password = request.POST.get('password')

        try:
            team = Team.objects.get(name=team_name)
            if check_password(password, team.password):
                # If password is correct it will store team information in the session
                request.session['team_id'] = team.id
                # Sets in_team variable to true
                team.in_team = True
                # Save the updated status
                team.save()
                return redirect('home')
            else:
                messages.error(request, 'Invalid password')
        except Team.DoesNotExist:
            messages.error(request, 'Team not found')

    return render(request, 'teams.html')
            
        
def tasks(request):
    all_tasks = Tasks.objects.all()
    return render(request, 'tasks.html', {'tasks': all_tasks})

def delete_task(request, task_id):
    try:
        task = Tasks.objects.get(pk=task_id)
        task.delete()
        return redirect('home')
    except Tasks.DoesNotExist:
        raise Http404("Task does not exist")
        

def done_task(request, task_id):
    # Retrieve the task by its id
    task = get_object_or_404(Tasks, pk=task_id)

    # Update the task to mark it as done
    task.completed = True
    task.save()

    # Retrieve all tasks
    tasks = Tasks.objects.all()
    
    # Pass the tasks to the template and render it
    return render(request, 'index.html', {'tasks': tasks})

def create_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('create_teamname')
        password = request.POST.get('create_password')

        # Hash and salt the password
        hashed_password = make_password(password)

        # Create a new Team object and save it to the database
        team = Team(name=team_name, password=hashed_password,in_team=True)
        team.save()

        # Redirect to index.html page
        return redirect('home')
    
    else:
         return render(request, 'create_team.html')

    