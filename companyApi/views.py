from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("Home Page Requested")
    lang = {"language": ["java", "c++", "python", "javascript"]}
    return JsonResponse(lang, safe=False)
