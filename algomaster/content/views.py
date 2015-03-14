from django.shortcuts import render
from django.views.generic import ListView, DetailView
from content.models import Content, Resource

def landing(request):
    context = {}
    return render(request, 'content/index.html', context)


class AlgoListView(ListView):
	model = Content
	queryset = Content.objects.all()
	template_name = 'content/list.html'


class AlgoDetailed(DetailView):
	model = Content
	template_name = 'content/concept.html'
