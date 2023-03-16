from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=64)

    def __str__(self):
        return self.categoryName

class Listing(models.Model):
    title = models.CharField(max_length=64, default="some string")
    description = models.CharField(max_length=300)
    imageUrl = models.CharField(max_length=1000)
    price = models.FloatField()
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchList = models.ManyToManyField(User, blank=True, null=True, related_name="listingWatchList")
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userComment")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listingComment")
    message = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.author} comment on {self.listing}"

