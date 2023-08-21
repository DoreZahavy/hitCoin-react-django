from django.urls import path
from .views import AddContactView, RemoveContactView, UserContactsView,UserContactDetailView

urlpatterns = [
    path('add/<int:user_id>/<int:contact_id>', AddContactView.as_view(), name='add-contact'),
    path('remove/<int:user_id>/<int:contact_id>/', RemoveContactView.as_view(), name='remove-contact'),
    path('<int:user_id>/', UserContactsView.as_view(), name='user-contacts'),
    path('<int:user_id>/<int:contact_id>/', UserContactDetailView.as_view(), name='user-contact-detail'),
]