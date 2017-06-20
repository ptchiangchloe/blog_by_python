# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
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
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    queryset = Post.objects.all()
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
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
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
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("list")
