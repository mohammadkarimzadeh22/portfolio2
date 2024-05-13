from django.shortcuts import render
from .models import Contact, Project, Skill, Service, Education
from django.http import HttpResponse
import itertools    


# Create your views here.
def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def index(request, *args, **kwargs):
    

    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()

        project = Project.objects.all()
        service = Service.objects.all()
        education = Education.objects.all()
        latest_projects = Project.objects.order_by('-id').all()[:3]
        skill = Skill.objects.all()
        context = {
                'project': my_grouper(1, project),
                'latest_projects': latest_projects,
                'skill': skill,
                'service': service,
                'education': education,
                'message_name': name
                }

        return render(request, 'index.html', context)
    else:

        project = Project.objects.all()
        service = Service.objects.all()
        education = Education.objects.all()
        latest_projects = Project.objects.order_by('-id').all()[:3]
        skill = Skill.objects.order_by('-percentage').all()
        context = {
                'project': my_grouper(1, project),
                'latest_projects': latest_projects,
                'skill': skill,
                'service': service,
                'education': education
                }

        return render(request, 'index.html', context)

    
    