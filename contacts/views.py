
from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, 'index.html')   

def show(request):
    if(request.method == 'POST'):
        persons = Contact.objects.all()
        con = {'persons':persons}
        return render(request, 'contacts.html', con)
    else:
        return render(request, 'contacts.html')


def insert(request):
    if(request.method == 'POST'):
        person = Contact()
        person.firsname = request.POST['txtname']
        person.lastname =  request.POST['txtfamily']
        person.tell = request.POST['telephone']
        person.email =  request.POST['email']
        person.save()

        return render(request, 'register.html', {'successful': 'Insert new contact successfully'})

    else:
        return  render(request, 'register.html')