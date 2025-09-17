from http.client import responses

from django.shortcuts import render, get_object_or_404

from blog.models import Blog


def blog_list(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog_list.html', context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog': blog}

    return render(request, 'blog_detail.html', context)

    # visits = int(request.COOKIES.get('visits', 0)) + 1
    #
    # request.session['count'] = request.session.get('count', 0) + 1
    # 'count': request.session['count'],
    # responses = render(request, 'blog_list.html', context)
    #
    # responses.set_cookie('visits', visits)