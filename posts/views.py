from django.shortcuts import render, redirect
from . import forms

# Create your views here.


def add_post(request):
    # user sending post request to add post
    if request.method == 'POST':
        # create a form instance and populate it with data from the request. (capturing the data from post request.)
        post_form = forms.PostForm(request.POST)
        # check whether it's valid.
        if post_form.is_valid():
            # process the data in form.cleaned_data as required. (saving the data to the database.)
            post_form.save()
            # redirect to a new URL
            return redirect('home')
    else:
        # user sending get request to add post (displaying the form.)
        post_form = forms.PostForm()
    # render the template depending on the request. (displaying the form.)
    return render(request, 'add_post.html', {'post_form': post_form})


def edit_post(request, post_id):
    # get the post from the database
    post = forms.Post.objects.get(pk=post_id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request.
        # here instance means the form is pre-populated with the data from the database.
        # here request.POST and instance=post both are required. so that if user doesn't change anything, it will save the previous data.
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    else:
        # user sending get request to edit post (displaying the form with pre-populated data.)
        post_form = forms.PostForm(instance=post)
    return render(request, 'add_post.html', {'post_form': post_form})


def delete_post(request, post_id):
    # we can use models.Post.objects.get also both are same here.
    post = forms.Post.objects.get(pk=post_id)
    post.delete()
    return redirect('home')
