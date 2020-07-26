from django.urls import path, include
from .views import home, contact_list,about,contact_details,new_contact,edit_contact,delete_contact
from rest_framework.routers import DefaultRouter
from .api import ContactViewset

router = DefaultRouter()
router.register(r'contacts',ContactViewset,basename="contact")

urlpatterns = [
    path("api/",include(router.urls)),
    path('',home, name = "index"),
    path('about/' ,about, name = "about"),
    path('contact/',contact_list, name ="contacts"),
    path('contact/new',new_contact, name ="new_contact"),
    path('contact/<int:id>/',contact_details, name ="details"),
    path('contact/edit/<int:id>',edit_contact, name ="edit_contact"),
    path('contact/delete/<int:id>',delete_contact, name ="delete_contact"),
    

    ]
