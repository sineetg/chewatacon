from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'chewata_event/home.html')
    
def about(request):
    return render(request, 'chewata_event/about.html')
 
def schedule(request):
    return render(request, 'chewata_event/schedule.html')
    
def contact(request):
    return render(request, 'chewata_event/contact.html')
    