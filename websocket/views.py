from django.shortcuts import render


def random(request):
    return render(request, 'basic_count.html', context={'text': "hello world"})


def chat(request):
    return render(request, 'basic_count.html', context={'text': "hello world"})
