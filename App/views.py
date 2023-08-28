from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CandidateForm

def home(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your request was successful")
            return redirect('/')
        else:
            messages.error(request, "Something went wrong, please try again")
        context = {'form': form}
        
        return render(request, "home.html", context)
    else:
        form = CandidateForm()
        return render(request, "home.html", {'form': form})
