from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from loginpage.models import  Group, Assignment, UserPic
from viewgroups.forms import UserGroupForm, AssignmentForm
from django.contrib import messages

@login_required(login_url='/accounts/login')
def assignPageView(request, groupID) :
    #displays only the assignments of the specific group, and orders the assignments by date from closest to furthest
    assign_filterList = Assignment.objects.filter(group_id = groupID).order_by('-assign_duedate')
    group = Group.objects.get(id = groupID)

    context = {
        'assign_list': assign_filterList,
        'group': group
        }

    return render(request, 'classes/viewassignments.html', context)


#takes you to the edit Assignments page, filters by the selected Assignment.
@login_required(login_url='/accounts/login')
def editAssignPageView(request, assignID = None, groupID = None) :
    #loggedInUser = User.objects.filter(username = request.user)
    parameter = None
    #are we posting data?
    if request.method == 'POST':
            
            #Is there an assignment parameter and group parameter? IE you are either editing an existing record, or deleting a record
            if assignID and groupID:
                parameter = Assignment.objects.get(id=assignID)
                #if we are deleting the record
                if request.POST.get('delete'):
                    parameter.delete()
                    
                else:
                #otherwise save the form with the data passed (edit)
                    form = AssignmentForm(request.POST, instance = parameter)   
                    #if an incorrect date is entered, the system will skip the assignment and reroute you back to the assigments page
                    try: form.save()
                    except ValueError :   
                        pass
                    return HttpResponseRedirect(f'/viewassignments/{groupID}/')
                
                return HttpResponseRedirect(f'/viewassignments/{groupID}/')
            #New groups being created will follow this path because they don't leave edit page view with an assignment ID
            else:
                form = AssignmentForm(request.POST)
                #if an incorrect date is entered, the system will skip the assignment and reroute you back to the assigments page
                try: form.save()
                except ValueError :   
                    pass
                return HttpResponseRedirect(f'/viewassignments/{groupID}/')
    else:
        if assignID:
            parameter = Assignment.objects.get(id = assignID)
            #creates form and loads in the info from the parameter so you can see what you are editing --- only activates when there is an assignID being passed
            form = AssignmentForm(instance = parameter, initial={'group': groupID})

        else: 
            #generates a blank form when you are creating a new Assignment -- only activates when NO assignID is being passed (when we are making a new assignment)
            parameter = Group.objects.get(id=groupID)
            form = AssignmentForm(initial={'group': groupID})
        
        #sends generated form and parameter (if there is one) to webpage
        context = {
            'assignID': assignID,
            'groupID':groupID,
            'form': form, 
            'parameter': parameter
        }

        return render(request, 'classes/editassignment.html', context)