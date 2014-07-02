from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import redis

def index(request):
	print type(request)
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        r.set('foo1', 'bar1')
	print r.get("foo1")
	print r.get("foo")
	return HttpResponse("Hello , this first page..")

def login(request):
	template = loader.get_template('polls/html/login.html')
	context = RequestContext(request, {
    	})
	return HttpResponse(template.render(context))        


# Create your views here.
