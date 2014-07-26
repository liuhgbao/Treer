from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Article, Tag, Author , Category , Works , Language

def blog_list(request):
    blist = Article.objects.all().order_by('-publish_time')

    return render_to_response('blog.html',{"blist":blist}, context_instance=RequestContext(request))

def code_list(request):
    clist = Works.objects.all().order_by('-publish_time')

    return render_to_response('code.html',{"clist":clist},context_instance=RequestContext(request))

# Create your views here.

