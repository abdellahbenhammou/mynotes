# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
import datetime
from models import Notes
import json
from django.contrib.auth.forms import UserCreationForm
import re

def home(request):
    if request.user.is_authenticated():
        print 'in'
        notes = Notes.objects.filter(user=request.user).order_by('-date')
        return render_to_response("home.html",{'username': request.user.username, 'notes': notes}, context_instance=RequestContext(request))
    else:
        print 'not in'
        return render_to_response("home.html", {'username': request.user.username})


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    elif request.method == 'GET':
        c = {}
        c.update(csrf(request))
        return render_to_response("registration.html", c)

    else:
        user_form = UserCreationForm(request.POST or None)
        if request.method == 'POST':
            print 'those are the values: ' + request.POST['username'] + ' ** ' + request.POST['email'] + ' ** ' + request.POST['password']
            user = User.objects.create_user(username=request.POST.get('username'), email=request.POST.get('email'), password=request.POST.get('password'))
            user.save()
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                auth.login(request, user)
                print 'done'
                return render_to_response("home.html", {'username': user.username}, context_instance=RequestContext(request))
            else:
                c = {}
                c.update(csrf(request))
                print 'login 1'
                return render_to_response("login.html", c)

        else:
            print 'login 2'
            c = {}
            c.update(csrf(request))
            return render_to_response("login.html", c)


def registration(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("registration.html", c)


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    c = {}
    c.update(csrf(request))
    return render_to_response("login.html", c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def logout(request):
    auth.logout(request)
    return render_to_response("home.html",{'username': request.user.username}, context_instance=RequestContext(request))

@csrf_exempt
def addnote(request):
    print 'before'
    if request.method == 'POST':
        print 'post'
        if request.user.is_authenticated():
            print 'auth'
            note = str(request.POST.get('note', ''))
            if note.__len__() == 0:
                notes = Notes.objects.filter(user = request.user)
                return render_to_response("home.html", {'username': request.user.username, 'notes': notes, 'error': 'Empty Note'}, context_instance=RequestContext(request))
            l = []
            l = re.findall(r"#(\w+)", note)
            tags = ""
            for i in l:
                print 'tag: ' + str(i)
                tags = tags + str(i) + ','
            #note = re.sub(r'#(\w+)', r'<a href="test/\1">\2</a>', note)
            #   print 'heeere: ' + re.sub(r"#(\w+)", r'<a href="test/\1">\2</a>', note)
            print 'this is the new note: ' + note
            #tags = note.sp
            time = datetime.datetime.now()

            l = note.split()
            for i in l:
                if '#' in i:
                    j = '<a id="tag" href="test/t="'+i+'>'+i+'</a>'
                    #print j
                    note = note.replace(i, j)
                #print note
            print note

            new_note = Notes.objects.create(note=note, date=time, user=request.user, tags=tags)
            c = {}
            c.update(csrf(request))
            new_note.save()
            print 'new note: ' + new_note.note
            return HttpResponse(json.dumps({'note': new_note.note, 'id': new_note.id}))
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
            #new_note.save()

def delete_note(request):
    print 'deleting.. ' + str(request.GET.keys())
    if request.GET and request.is_ajax() and request.user.is_authenticated:
        note = Notes.objects.filter(id=request.GET.get('data', ''), user=request.user)
        note_id = request.GET.get('data', '')
        note.delete()
        print 'yes: ' + note_id
        return HttpResponse(json.dumps({'note': note_id}))
    else:
        print 'no'
        return HttpResponse(json.dumps({'note': 'none'}))
