from django.shortcuts import render, redirect
from booking.models import Room, Booking, RoomType, User, Availability, Hotel
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        "render_string": "Hello, world!"
    }
    return render(request, template_name="booking/index.html", context=context)

def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }
    return render(request, template_name="booking/rooms_list.html", context=context)

def book_room(request):
    if request.method == 'POST':
        hotel_name = request.POST.get('hotel')
        room_number = request.POST.get('room-number')
        start_time = request.POST.get('start-time')
        end_time = request.POST.get('end-time')

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
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return HttpResponse(
                "User doesn't exist!",
                status=404
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