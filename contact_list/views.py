from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Contact

def contact_list(request):
    contact_ob = Contact.objects.all()
    pagination = Paginator(contact_ob, 8)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num =1
    page = pagination.get_page(page_num)        
    return render(request, 'contact_list/contact_list.html', {'contact_ob':page.object_list, 'page':page, 'pagination':pagination})

    

# Create your views here.
