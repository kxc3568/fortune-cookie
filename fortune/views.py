from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .utils import *
from .forms import UserForm

# Create your views here.
def HomeView(request):
	form = UserForm()
	return render(request, 'home.html', {'form': form})

def FortuneView(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			if len(api.GetUserTimeline(screen_name=username))==0:
				return HttpResponse('<h1>You have no tweets</h1>')
			return render(request, 'fortune.html', {'fortune': getFortune(username)})
		else:
			return HttpResponse('<h1>Please enter a valid username</h1>')
	else:
		return render(request, 'nofortune.html')
	return render(request, 'fortune.html', {'tweets': username})	