from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import  login_required
from .models import Contact

# Create your views here.

def home(request):

   return render(request,"index.html")


def about(request):
   return render(request,"about.html")

@login_required(login_url="/login")
def contact_list(request):
   user = request.user
   print("User:", user)
   
   contacts = Contact.objects.filter(auteur= user,archive=False)
   return render(request,"contact_list.html",{"contacts":contacts})


@login_required(login_url="/login")

def contact_details(request,id):

   contact = get_object_or_404(Contact,id=id)
   return render (request,"contact_detail.html",{"contact":contact})

@login_required(login_url="/contact/")
def new_contact(request):
   if request.method == "POST":
      auteur= request.user
      nom = request.POST['nom']
      prenom = request.POST['prenom']
      telephone = request.POST['telephone']
      email = request.POST['email']

      contact = Contact.objects.create(
         auteur= auteur,
         nom = nom, 
         prenom = prenom ,
         email= email,
         telephone=telephone)
      contact.save()
      return redirect("/contact/")
   
   return render(request, 'new_contact.html')
   

@login_required(login_url="/contact/")
def edit_contact(request,id):
   contact = get_object_or_404(Contact, id=id)
   if request.method == "POST":

      nom = request.POST['nom']
      prenom = request.POST['prenom']
      telephone = request.POST['telephone']
      email = request.POST['email']

      contact_to_update = Contact.objects.filter(pk=id).update(
         nom = nom, 
         prenom = prenom ,
         email= email,
         telephone=telephone )
      return redirect("/contact/")

   return render(request,'edit_contact.html',{'contact':contact})

@login_required(login_url="/contact/")
def delete_contact(request,id):
   contact = get_object_or_404(Contact, id=id)
   if request.method == "POST":

      contact_to_update = Contact.objects.filter(pk=id).update(
         archive= True)
      return redirect("/contact/")

   return render(request,'delete_contact.html',{'contact':contact})



