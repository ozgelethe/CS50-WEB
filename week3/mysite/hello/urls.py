#Inside our new urls.py, we’ll create a list of url patterns 
#that a user might visit while using our website. In order to do this:

# 1. We have to make some imports: 
#from django.urls import path will give us the ability to reroute URLSs, 
#and from . import views will import any functions we’ve created in views.py.
from django.urls import path
from . import views
# "." in upper line means from the current directory

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("brian", views.brian, name="brian"),
    path("mina", views.mina, name="mina")
]
# 2. For each desired URL, add an item to the urlpatterns list that contains 
# a call to the path function with two or three arguments: A string 
# representing the URL path, a function from views.py that we wish to 
# call when that URL is visited, and (optionally) a name for that path,
# in the format name="something".
