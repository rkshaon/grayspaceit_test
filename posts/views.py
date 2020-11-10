from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

# POSTS VIEW ENDPOINT
@login_required(login_url='login')
def posts(request):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    post_data = response.json()
    context = {
        'posts': post_data,
    }
    return render(request, 'blog-listing.html', context)

# POST DETAILS VIEW ENDPOINT
@login_required(login_url='login')
def post_details(request, post_id):
    url = 'https://jsonplaceholder.typicode.com/posts/' + str(post_id)
    response = requests.get(url)
    post_data = response.json()
    context = {
        'post': post_data,
    }
    # context = {
    #     'post_id': post_id,
    # }
    return render(request, 'blog-post.html', context)
