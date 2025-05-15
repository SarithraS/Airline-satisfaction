from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class UserPredictModel(models.Model):
    Gender = models.CharField(max_length=100)
    Customer_Type = models.CharField(max_length=100)  # Assuming this corresponds to 'Customer Type'
    Age = models.IntegerField()
    Type_of_Travel = models.CharField(max_length=100)  # Assuming this corresponds to 'Type of Travel'
    Class = models.CharField(max_length=100)
    Inflight_wifi_service = models.IntegerField()  # Assuming this corresponds to 'Inflight wifi service'
    Food_and_drink = models.IntegerField()  # Assuming this corresponds to 'Food and drink'
    Online_boarding = models.IntegerField()  # Assuming this corresponds to 'Online boarding'
    Seat_comfort = models.IntegerField()  # Assuming this corresponds to 'Seat comfort'
    Inflight_entertainment = models.IntegerField()  # Assuming this corresponds to 'Inflight entertainment'
    Onboard_service = models.IntegerField()  # Assuming this corresponds to 'On-board service'
    Leg_room_service = models.IntegerField()  # Assuming this corresponds to 'Leg room service'
    Baggage_handling = models.IntegerField()  # Assuming this corresponds to 'Baggage handling'
    Checkin_service = models.IntegerField()  # Assuming this corresponds to 'Checkin service'
    Inflight_service = models.IntegerField()  # Assuming this corresponds to 'Inflight service'
    Cleanliness = models.IntegerField()
    Departure_Delay_in_Minutes = models.IntegerField()
    satisfaction = models.CharField(max_length=100)  # This will store the prediction result

    def __str__(self):
        return f"Prediction: {self.satisfaction}"
    


class Chatbot(models.Model):
    message = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.message