from django.shortcuts import render, redirect
from booking.models import Room, Booking, RoomType, Hotel
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.dateparse import parse_date 
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    context = {}
    return render(request, template_name="booking/index.html", context=context)

def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }
    return render(request, template_name="booking/rooms_list.html", context=context)

@login_required
def book_room(request):
    if request.method == 'POST':
        hotel_name = request.POST.get('hotel')
        room_number = request.POST.get('room-number')
        start_time = request.POST.get('start-time')
        end_time = request.POST.get('end-time')
        start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M') 
        end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M') 
        start_time = timezone.make_aware(start_time , timezone.get_current_timezone()) 
        end_time = timezone.make_aware(end_time , timezone.get_current_timezone()) 

        try:
            hotel = Hotel.objects.get(name=hotel_name)
        except Hotel.DoesNotExist:
            return HttpResponse(
                "This hotel doesn't exist!",
                status=404
            )

        try:
            room = Room.objects.get(number=room_number, hotel=hotel)
        except Room.DoesNotExist:
            return HttpResponse(
                "This room number doesn't exist!",
                status=404
            )

        try:
            user = get_user_model().objects.get(id=request.user.id)
        except get_user_model().DoesNotExist:
            return HttpResponse(
                "User doesn't exist!",
                status=404
            )
        bookings = Booking.objects.filter(room=room)
        for book in bookings:
            if book.start_time >= end_time or book.end_time <= start_time:
                pass
            else:
                return HttpResponse(
                "This room is booked for the same hour.",
                status=400
                )

        booking = Booking.objects.create(
            user=user,
            hotel=hotel,
            room=room,
            start_time=start_time,
            end_time=end_time
        )
        return redirect('booking-details', pk=booking.id)
    else:
        return render(request, template_name='booking/booking_form.html')
    
def booking_details(request, pk):
    try:
        booking = Booking.objects.get(id=pk)
        context = {
            "booking": booking
        }
        return render(request, template_name='booking/booking_details.html', context=context)
    except Booking.DoesNotExist:
        return HttpResponse(
            "This booking doesn't exist!",
            status=404,
        )
    
@login_required
def delete_user_bookings(request):
    if request.method == 'POST':
        user = request.user
        Booking.objects.filter(user=user).delete()
        messages.success(request, 'All your bookings have been deleted.')
        return redirect('index')
    
    return render(request, 'booking/delete_bookings_confirm.html')

@login_required
def delete_user_booking(request):
    if request.method == 'POST':
        user = request.user
        booking_id = request.POST.get('booking_id')
        try:
            booking = Booking.objects.get(id=booking_id)
            if booking.user == user:
                booking.delete()
                messages.success(request, 'This booking has been deleted.')
            else:
                messages.error(request, 'This booking cannot be deleted because you do not own it.')
        except Booking.DoesNotExist:
            messages.error(request, 'Booking not found.')
        return redirect('index')
    
    booking_id = request.GET.get('booking_id')
    context = {'booking_id': booking_id}
    return render(request, 'booking/delete_booking_confirm.html', context)

def bookings_list(request):
    user = request.user
    user_bookings = Booking.objects.filter(user=user)
    context = {
        'user_bookings': user_bookings
    }
    return render(request, 'booking/bookings_list.html', context)

