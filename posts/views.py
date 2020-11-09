from django.shortcuts import render


# POSTS VIEW ENDPOINT
def posts(request):
    return render(request, 'blog-listing.html')


# POST DETAILS VIEW ENDPOINT
def post_details(request):
    return render(request, 'blog-post.html')