from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def indexPageView(request) :
    return render(request, 'account/index.html')

#def createaccountPageView(request) :
    #return render(request, 'account/createaccount.html')

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':   
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'account/register.html', context)

