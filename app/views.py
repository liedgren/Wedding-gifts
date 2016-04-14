from django.shortcuts import *
from django.template import *
from .models import *
from urllib.request import urlopen
from .forms import *
from bs4 import BeautifulSoup
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.views.decorators.csrf import csrf_exempt

#NEED TO INSTALL Beautfiul soup

def index(request):
	qs = Gift.objects.all()
	gifts = []
	for gift in qs:
		gifts.append([gift.name, gift.number, gift.bought, getMetaData(gift.link), gift.link, gift.pk, (gift.number - gift.bought)])
	dict = {'gifts':gifts}
	return render_to_response("index.html", dict, context_instance=RequestContext(request)) 

def user_login(request):
	dict = {}
	return render_to_response("index.html", dict, context_instance=RequestContext(request))  

def user_logout(request):
	dict = {}
	return render_to_response("index.html", dict, context_instance=RequestContext(request))  

def getMetaData(url):
	page = urlopen(url).read()
	soup = BeautifulSoup(page)
	img_link = soup.find_all(attrs={"property":"og:image"})
	try:
		return img_link[0]['content'].encode('utf-8')
	except:
		return "/static/img/default.png"

@csrf_exempt
def decrease(request):
	if request.method == 'POST':
		id = request.POST.get('gift_id',0)
		if int(id) > 0:
			g = Gift.objects.get(pk = id)
			if g.bought < g.number:
				nr = g.bought + 1
				g.bought = nr
				g.save()

	return HttpResponseRedirect("/")	