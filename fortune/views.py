from django.shortcuts import render
from .utils import getTimeline

# Create your views here.
def HomeView(request):
	return render(request, 'home.html', {'tweets': getTimeline('dhruvak_')})