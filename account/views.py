from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.
def register_view(request):
     context = {
         'form': UserCreationForm
     }
     return render(request, 'register.html', context)
