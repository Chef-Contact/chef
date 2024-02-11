from django.shortcuts import render
from apps.host import models

# Create your views here.
def becomeahost(request):
    become = models.BecomeaHost.objects.latest("id")
    free_all = models.Free.objects.all()
    guests_all = models.Guests.objects.all()
    receive_all = models.Receive.objects.all()
    end_all = models.BecomeEnd.objects.all()
    blog_active = models.BlogActive.objects.all()
    blog_all= models.Blog.objects.all()
    return render(request, 'becomeahost.html', locals())