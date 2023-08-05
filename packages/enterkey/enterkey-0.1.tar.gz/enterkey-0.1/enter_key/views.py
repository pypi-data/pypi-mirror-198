from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

def key(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        if key == "":
            return redirect('/')
        print('Key entered is',key)
        url = reverse('param') + f'?key={key}'
        return HttpResponseRedirect(url)
    return render(request, 'home.html')