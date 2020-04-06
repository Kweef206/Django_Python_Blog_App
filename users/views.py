from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Creates forms to be passed to template
def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})