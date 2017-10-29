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
			return render(request, 'fortune.html', {'fortune': getFortune(username)})
		else:
			#errors
			pass
	else: 
		#???
		pass
	return render(request, 'fortune.html', {'tweets': username})	