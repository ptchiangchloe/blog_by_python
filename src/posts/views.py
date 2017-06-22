# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from urllib import quote_plus
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        print form.cleaned_data.get("title")
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Successfully Created")

    # if request.method == "POST":
        # print request.POST.get("content")
        # print request.POST.get("title")
    context = {
        "form": form,
    }
    return render(request, 'post_form.html', context)

def post_detail(request, id=None):
    # instance = Post.objects.get(id=1)
    instance = get_object_or_404(Post, id=id)
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

    page = request.GET.get('abc')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    if request.user.is_authenticated():
        context = {
            "object_list": queryset,
            "title":"My User List"
        }
    else:
        context = {
            "title":"List"
        }
    return render(request, 'post_list.html', context)

def post_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')

        return HttpResponseRedirect(instance.get_absolute_url())

    # instance = Post.objects.get(id=1)
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, 'post_form.html', context)

def post_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("list")
