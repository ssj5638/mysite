from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'board/list.html')


def write(request):
    return render(request, 'board/write.html')