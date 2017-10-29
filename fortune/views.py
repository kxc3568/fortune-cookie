from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .utils import getTimeline
from .forms import UserForm

# Create your views here.
def HomeView(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			#return HttpResponseRedirect('/fortune/')
			return render(request, 'fortune.html', {'tweets': getTimeline(username)})
		else:
			#errors
			pass
	else:
		form = UserForm()
	return render(request, 'home.html', {'form': form})

# def FortuneView(request):
# 	return render(request, 'fortune.html', {'tweets': username})