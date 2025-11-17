from django.shortcuts import render
from .forms import ExampleForm

def form_example(request):
    form = ExampleForm()
    return render(request, 'form_example.html', {'form': form})
