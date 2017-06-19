from django.template.loader import get_template
from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Post

# Create your views here.
def homepage(request):
    template=get_template('index.html')
    posts=Post.objects.all()
    now=datetime.now()
    html=template.render(locals())#locals()会把当前所有局部变量用字典类型打包
    return HttpResponse(html)


def showpost(request,slug):
    template=get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        if post !=None:
            html=template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')