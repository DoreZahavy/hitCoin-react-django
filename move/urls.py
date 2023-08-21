from django.urls import path
from .views import create_move , MoveListView

urlpatterns = [
    path('', create_move, name='create-move'),
    path('<int:user_id>', MoveListView.as_view(), name='get-moves'),

    # path('remove/<int:user_id>/<int:contact_id>/', RemoveContactView.as_view(), name='remove-contact'),
    # path('', MoveListView.as_view(), name='user-contacts'),
    # path('<int:user_id>/<int:contact_id>/', UserContactDetailView.as_view(), name='user-contact-detail'),
]