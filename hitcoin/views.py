from django.shortcuts import render
def index(request):
    print('getting index html')
    return render(request , 'index.html')