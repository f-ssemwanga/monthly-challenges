from django.urls import path
from . import views

"""
1. Perform a URL config following the steps below
- create a that has has all supported urls and a view function to be triggered using the path() function
- the path() function takes a string describing the url and a pointer to the view function
- the views.py file must be imported here to access the views functions
2. Connect the challenges URL config to the app wide /main global config urls file
"""

"""urlpatterns = [
    # list of all supported urls
    path("january", views.january),
    path("february", views.february),
]"""
# setting up a dynamic path
# month here serves as a key word argument which is passed to the view
urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge),
]
