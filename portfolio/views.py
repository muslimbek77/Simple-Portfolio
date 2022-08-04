from django.shortcuts import render
from portfolio.models import Home,About,Project,Services
from portfolio.forms import ContactForm
# Create your views here.


def index(request):
    home = Home.objects.all()[0]
    about = About.objects.all()[0]
    projects = Project.objects.all()
    services = Services.objects.all()
    
    form = ContactForm(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        is_success = True
        form.save()
        form = ContactForm()

    
    
    content = {'homes':home,
               'about':about,
               'projects':projects,
               'form': form,
        'is_success': is_success,
        'services':services}
    return render(request,'index.html',content)
