from django.shortcuts import render
from django.http import HttpResponse
from polls.models import *
from django.template import RequestContext, loader
# Create your views here.

# version 1
# def index(request):
#     latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#     output = ', '.join([p.question for p in latest_poll_list])
#     return HttpResponse(output)

# version 2
# def index(request):
#     latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(request, {
#         'latest_poll_list': latest_poll_list,
#     })
#     return HttpResponse(template.render(context))

# version 3
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'index_1.html', context)

