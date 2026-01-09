from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    friends = ['setu','x','y','z']
    return JsonResponse(friends,safe=False)