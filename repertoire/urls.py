from django.urls import path
from .views import home, contact_list,about,contact_details,new_contact,edit_contact,delete_contact

urlpatterns = [
    path('',home, name = "index"),
    path('about/' ,about, name = "about"),
    path('contact/',contact_list, name ="contacts"),
    path('contact/new',new_contact, name ="new_contact"),
    path('contact/<int:id>/',contact_details, name ="details"),
    path('contact/edit/<int:id>',edit_contact, name ="edit_contact"),
    path('contact/delete/<int:id>',delete_contact, name ="delete_contact"),
    

    ]
