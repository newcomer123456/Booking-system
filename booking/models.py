from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Додаємо related_name
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Додаємо related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.username

class RoomType(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    name = models.CharField(max_length=100) 
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)


class Room(models.Model):
    number = models.IntegerField()
    type = models.ForeignKey('RoomType', on_delete=models.CASCADE)  
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, null=True,)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.number} ({self.type.name})"
    
    class Meta: 
        ordering = ['number']

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"

class Availability(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Availability for {self.room.number} on {self.date}"