from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import (
    reverse,
)  # allows paths to be created by referring to the names of the URLs

# from django.template.loader import render_to_string


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
def index(request):
    """This will be the home page
    returns a list of months as a clickable link
    """
    # generate clickable links for each month using code
    # using a for loop to generate html code for a  <ul></ul> tag with list items
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalised_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalised_month}</a></li>'
    # the above results in "<li>...</li><li> ... </li>"
    # inject the list_items string into the <ul></ul>
    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


# setting up a dynamic  view
def monthly_challenge(request, month):
    # text passed to the view would depend on the requested month
    # could also use a try and except with the HttpResponseNotFound appearing in the except part
    try:
        challenge_text = monthly_challenges[month]
        # returning some form of HTML
        return render("challenges/challenge.html")
    except:
        return HttpResponseNotFound(f"<h1>This month is not supported!</h1>")


def monthly_challenge_by_number(request, month):
    # forward redirect requests to a url
    months = list(monthly_challenges.keys())  # list of months
    try:
        redirect_month = months[month - 1]  # choose the actual month
        # removing the hard coded url using reverse
        redirect_path = reverse(
            "month-challenge", args=[redirect_month]
        )  # figures how to correctly build a full url

        return HttpResponseRedirect(redirect_path)  # redirect path
    except IndexError:
        return HttpResponseNotFound("That was not a recognised month")
