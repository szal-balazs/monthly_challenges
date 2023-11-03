from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': "Do 10 pushups",
    'february': "Do 20 pushups",
    'march': "Do 30 pushups",
    'april': "Do 40 pushups",
    'may': "Do 50 pushups",
    'june': "Do 60 pushups",
    'july': "Do 70 pushups",
    'august': "Do 80 pushups",
    'september': "Do 90 pushups",
    'oktober': "Do 100 pushups",
    'november': "Do 110 pushups",
    'december': "Do 120 pushups"
}

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        'month_list': months
        })


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month': month
        })
    except:
        raise Http404()
        


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound()

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args = [redirect_month])

    return HttpResponseRedirect(redirect_path)
