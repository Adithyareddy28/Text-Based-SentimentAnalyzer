from django.shortcuts import render
from .utils import classify_sentiment

def sentiment_analysis(request):
    result = None
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if text:
            result = classify_sentiment(text)
        else:
            result = "No text provided"
    return render(request, 'home.html', {'result': result})
