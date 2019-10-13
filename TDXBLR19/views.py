from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html', {})


def callback(request):
    return render(request, 'main/callback.html', {})

def demo(request):
    return render(request, 'main/LightComp.html', {})
