from django.contrib import admin
from .models import RoomType, Hotel, Room, Booking

# Реєстрація моделі RoomType
@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

# Реєстрація моделі Hotel
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'description')
    search_fields = ('name', 'location')
    list_filter = ('location',)

# Реєстрація моделі Room
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'type', 'hotel', 'capacity', 'price', 'location')
    search_fields = ('number', 'type__name', 'hotel__name')
    list_filter = ('type', 'hotel', 'capacity')
    list_editable = ('price', 'capacity')

# Реєстрація моделі Booking
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'hotel', 'start_time', 'end_time', 'confirmed')
    search_fields = ('user__username', 'room__number', 'hotel__name')
    list_filter = ('confirmed', 'start_time', 'end_time')
    date_hierarchy = 'start_time'

