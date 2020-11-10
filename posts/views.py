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
    url_post = 'https://jsonplaceholder.typicode.com/posts/' + str(post_id)
    response_post = requests.get(url_post)
    post_data = response_post.json()
    url_comment = 'https://jsonplaceholder.typicode.com/posts/' + str(post_id) + '/comments'
    response_comment = requests.get(url_comment)
    comment_data = response_comment.json()
    context = {
        'post': post_data,
        'comments': comment_data,
    }
    return render(request, 'blog-post.html', context)
