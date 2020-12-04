#https://docs.djangoproject.com/en/3.1/topics/forms/

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from loginpage.models import  Group, Assignment, UserPic
from viewgroups.forms import UserGroupForm
from django.contrib import messages

@login_required(login_url='/accounts/login')
def groupsPageView(request) :
    #displays only the groups of the logged in user, then sorts by group name
    group_filterList = Group.objects.filter(user = request.user).order_by('group_name')
    
    context = {
        'group_list': group_filterList,
    
        }

    return render(request, 'groups/viewgroups.html', context)


#takes you to the edit groups page, filters by the selected group.
@login_required(login_url='/accounts/login')
def editGroupPageView(request, groupID = None) :
    loggedInUser = User.objects.filter(username = request.user)
    parameter = None
    if request.method == 'POST':
        #if there is a parameter being passed
        if groupID:
            parameter = Group.objects.get(id=groupID)
            if request.POST.get('delete'):
                parameter.delete()
                
            else:
                #initializing a group
                            #initial=request.user sets the default form for the field, and sets the default to the user that is logged in
                form = UserGroupForm(request.POST, instance = parameter)   # ,initial={'user':loggedInUser}
                form.save()
                
               
            return HttpResponseRedirect('/viewgroups')
        else:
            #editing a group, grabs the UserGroupForm
            form = UserGroupForm(request.POST) #, initial={'user':loggedInUser}
            if form.is_valid:
                
                #form.save(commit=false)
                form.save()
              

                return HttpResponseRedirect('/viewgroups')
    else:
        if groupID:
            parameter = Group.objects.get(id = groupID)
            #sends form and loads in the info from the parameter so you can see what you are editing
            form = UserGroupForm(instance = parameter, initial={'user':loggedInUser})

        else: 
            #generates a blank form when you are creating a new group with the logged in user being automatically put into it
            form = UserGroupForm(initial={'user':loggedInUser})
        
        #sends generated form and parameter (if there is one) to webpage
        context = {
            'form': form, 
            'parameter': parameter,
            'loggedInUser': loggedInUser
        }

        return render(request, 'groups/editgroup.html', context)


@login_required(login_url='/accounts/login')
def newGroupView(request, groupID = None):

    parameter = None
    if request.method == 'POST':
        if groupID:
            parameter = Group.objects.get(id=groupID)
            if request.POST.get('delete'):
                parameter.delete()
                
            else:
                
                form = UserGroupForm(request.POST, instance = parameter)
                form.save()
                
               
            return HttpResponseRedirect('/viewgroups')
    else:
        if groupID:
            parameter = Group.objects.get(id = groupID)
            form = UserGroupForm(instance = parameter)

        else: 
            form = UserGroupForm()
        
        context = {
            'form': form, 
            'parameter': parameter
        }

        return render(request, 'groups/editgroup.html', context)
