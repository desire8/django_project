from django.shortcuts import render
from django.template import RequestContext, loader
# Create your views here.
from django.http import HttpResponse
from polls.models import Poll
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

    return HttpResponse("Hello, world.I am here at poll index.")
def detail(request,poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)
def results(request,poll_id):
    return HttpResponse("You are looking at result %s" % poll_id)
def vote(request, poll_id):
    return HttpResponse("You are voting on poll %s" % poll_id)

