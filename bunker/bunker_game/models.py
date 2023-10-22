from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    premium = models.BooleanField()


class Card(models.Model):
    card_type = models.CharField(max_length=15)
    card_text_ru = models.CharField(max_length=50)
    card_text_en = models.CharField(max_length=50)
    profession_ability = models.CharField(max_length=50)
    card_photo = models.CharField(max_length=50)
    card_rating = models.SmallIntegerField()
    premium = models.BooleanField()


class Room(models.Model):
    room_link = models.CharField(max_length=50)
    premium = models.BooleanField()


class Player(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
