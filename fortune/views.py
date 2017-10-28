from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .utils import getTimeline
from .forms import UserForm

# Create your views here.
def HomeView(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/fortune/')
	else:
		form = UserForm()
	return render(request, 'home.html', {'form': form, 'tweets': getTimeline('dhruvak_')})

def FortuneView(request):
	if request.method == 'POST':
		username = getTimeline(request.POST)
	else: 
		return HttpResponseNotFound('<p>ERROR</p>')
	return render(request, 'fortune.html', {'tweets': username})