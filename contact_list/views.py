from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.db.models import Q
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    
    search_contact = request.GET.get('search')
   
    if search_contact:
         contact_ob= Contact.objects.filter(Q(full_name__icontains=search_contact))
    else:
        contact_ob = Contact.objects.all()
    pagination = Paginator(contact_ob, 8)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num =1
    page = pagination.get_page(page_num)
    
    return render(request, 'contact_list/contact_list.html', {'contact_ob':page.object_list, 'page':page, 'pagination':pagination})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact_list/contact_detail.html', {'contact':contact})

def contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            contact.save()
            return redirect('contact_detail', pk=contact.pk) 
    else:    
        form = ContactForm()
       
    return render(request, 'contact_list/contact_edit.html', {'form':form})

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            contact.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_list/contact_edit.html', {'form': form}) 
    
def contact_delete(request, pk):
    try:
        contact = get_object_or_404(Contact, pk=pk)
        contact.delete()
        return redirect('contact_list')
    except Contact.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")    

def contact_search(request):
    search_contact = request.GET.get('search')
    contacts_find = Contact.objects.filter(Q(full_name__icontains=search_contact))
    return render(request, 'contact_list/contact_list.html', {'contact_ob':contacts_find} )

    

# Create your views here.
