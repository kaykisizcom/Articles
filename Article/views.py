from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from Article.forms import new_user_form, new_users_form
from Article.models import *


def index(request):
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


@login_required
@csrf_exempt
def works(request):
    works_list = Article.objects.filter(user=None)
    return render_to_response('works.html', locals(), context_instance=RequestContext(request))


@login_required
@csrf_exempt
def my_works(request):
    works_list = Article.objects.filter(user=request.user)
    return render_to_response('my_works.html', locals(), context_instance=RequestContext(request))


@login_required
@csrf_exempt
def my_works(request, work_type):
    if work_type == 1:
        works_list = Article.objects.filter(user=request.user, is_finished=False)
    elif work_type == 2:
        works_list = Article.objects.filter(user=request.user, is_approved=False)
    elif work_type == 3:
        works_list = Article.objects.filter(user=request.user, is_approved=True)
    return render_to_response('my_works.html', locals(), context_instance=RequestContext(request))


@login_required
@csrf_exempt
def payments(request):
    payments_list = AccountProcess.objects.filter(user=request.user)
    return render_to_response('payments.html', locals(), context_instance=RequestContext(request))


@login_required
@csrf_exempt
def balance(request):
    user = Users.objects.get(user=request.user)
    article_count = Article.objects.filter(user=request.user, is_approved=True).count()
    total_paid = AccountProcess.objects.filter(user=request.user).aggregate(Avg('was_paid_price'))
    total_earned = Decimal(total_paid.was_paid_price) + Decimal(user.balance)
    last_paid = AccountProcess.objects.filter(user=request.user).last()
    all_paid = AccountProcess.objects.filter(user=request.user).all()
    return render_to_response('balance.html', locals(), context_instance=RequestContext(request))


@login_required
@csrf_exempt
def message(request):
    message_list = Message.objects.filter(user=request.user)
    return render_to_response('message.html', locals(), context_instance=RequestContext(request))


@login_required
@csrf_exempt
def message_content(request):
    message_content_list = Message.objects.filter(user=request.user)
    return render_to_response('message_content.html', locals(), context_instance=RequestContext(request))



@login_required
@csrf_exempt
def profile(request):
    user = User.objects.get(user=request.user)
    users = User.objects.get(user=request.user)
    form_user = new_user_form(instance=user)
    form_users = new_users_form(instance=users)
    if request.method == 'POST' and 'user' in request.POST:
        form = new_user_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/')
            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
                return HttpResponseRedirect('/sorry/')
    elif request.method == 'POST' and 'users' in request.POST:
        form = new_users_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/')
            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
                return HttpResponseRedirect('/sorry/')
    return render_to_response('profile.html', locals(), context_instance=RequestContext(request))


@login_required
@csrf_exempt
def new_message(request):
    user = User.objects.get(user=request.user)
    title =
    return render_to_response('profile.html', locals(), context_instance=RequestContext(request))


@login_required
@csrf_exempt
def profile(request):
    user = User.objects.get(user=request.user)
    users = User.objects.get(user=request.user)
    form_user = new_user_form(instance=user)
    form_users = new_users_form(instance=users)
    if request.method == 'POST' and 'user' in request.POST:
        form = new_user_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/')
            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
                return HttpResponseRedirect('/sorry/')
    elif request.method == 'POST' and 'users' in request.POST:
        form = new_users_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/')
            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
                return HttpResponseRedirect('/sorry/')
    return render_to_response('profile.html', locals(), context_instance=RequestContext(request))


@login_required
@csrf_exempt
def profile(request):
    user = User.objects.get(user=request.user)
    users = User.objects.get(user=request.user)
    form_user = new_user_form(instance=user)
    form_users = new_users_form(instance=users)
    if request.method == 'POST' and 'user' in request.POST:
        form = new_user_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/')
            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
                return HttpResponseRedirect('/sorry/')
    elif request.method == 'POST' and 'users' in request.POST:
        form = new_users_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/')
            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
                return HttpResponseRedirect('/sorry/')
    return render_to_response('profile.html', locals(), context_instance=RequestContext(request))
