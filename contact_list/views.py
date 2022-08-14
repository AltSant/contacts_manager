from django.shortcuts import render
from .models import Contact

def contact_list(request):
    contact_ob = Contact.objects.all()
    return render(request, 'contact_list/contact_list.html', {'contact_ob':contact_ob})

# Create your views here.
