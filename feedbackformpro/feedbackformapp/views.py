from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedbackForm

import datetime as dt
date1 = dt.datetime.now()

def feedback_view(request):
    if request.method=="POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name','')
            rating = request.POST.get('rating','')
            location = request.POST.get('location','')
            feedback = request.POST.get('feedback','')

            data = FeedbackData(
                name=name.capitalize(),
                rating=rating,
                date=date1,
                location=location,
                feedback=feedback
            )
            data.save()
            fform = FeedbackForm()
            feedbacks = FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform':fform,'feedbacks':feedbacks})
    else:
        feedbacks = FeedbackData.objects.all()
        fform = FeedbackForm()
        return render(request,'feedback.html',{'fform':fform,'feedbacks':feedbacks})