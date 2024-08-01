from django.urls import path
from booking import views


urlpatterns = [
    path('', views.index, name="index"),
    path('rooms-list', views.rooms_list, name="rooms-list"),
    path('bookroom', views.book_room, name="bookroom"),
    path('booking-details/<int:pk>', views.booking_details, name="booking-details"),
    path('delete_user_bookings', views.delete_user_bookings, name="delete_user_bookings"),
]