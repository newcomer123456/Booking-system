from django.urls import path
from booking import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('rooms-list', views.rooms_list, name="rooms-list"),
    path('bookroom', views.book_room, name="bookroom"),
    path('booking-details/<int:pk>', views.booking_details, name="booking-details"),
    path('delete_user_bookings', views.delete_user_bookings, name="delete_user_bookings"),
    path('delete_user_booking', views.delete_user_booking, name="delete_user_booking"),
    path('bookings_list', views.bookings_list, name="bookings_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
