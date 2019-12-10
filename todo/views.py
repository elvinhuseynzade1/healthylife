from django.shortcuts import render

# Create your views here.
def TemplateView(request):

    print('user',request.user)
    return render(request, "index.html")