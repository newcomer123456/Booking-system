from django.contrib import admin
from .models import User, RoomType, Room, Booking, Availability, Hotel

# Register your models here.
admin.site.register(User)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Availability)
admin.site.register(Hotel)
