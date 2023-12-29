from django.http import HttpResponse

def hello_world(response):
    return HttpResponse("Hello, World!")
def name(request):
    return HttpResponse("Akula Sai Sankar")
