from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# global variables
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 min every day",
    "march": "Do an activity with the children for at least 10 minutes",
    "april": "Walk for at least 20 min every day",
    "may": "Learn a new language",
    "june": "Play guitar",
    "july": "Go some place nice",
    "august": "spend a day a week on the beech",
    "september": "seriously look for a new job",
    "october": "Treat my self to something nice",
    "november": "Do more exercises than usual",
    "december": "Learn a new song on a guitar",
}
# Create your views here.


# setting up a dynamic  view
def monthly_challenge(request, month):
    # text passed to the view would depend on the requested month
    # could also use a try and except with the HttpResponseNotFound appearing in the except part
    challenge_text = monthly_challenges.get(
        month, HttpResponseNotFound("This month is not supported!")
    )
    return HttpResponse(challenge_text)


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)
