from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'profanity_text_api/index.html')