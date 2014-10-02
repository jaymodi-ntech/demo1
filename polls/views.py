from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from polls.models import *
from django.template import RequestContext, loader
from django.http import Http404
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

# version detail 1 (in this version i have to add try and catch.(it's old tech))
# def detail(request, poll_id):
#     try:
#         poll = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404
#     return render(request, 'polls/detail.html', {'poll': poll})

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    context = {'poll': poll}
    return render(request, 'detail_1.html', context)

# Now here i will add some more functions and then we will convert this whole
# functions to class based and then generic views