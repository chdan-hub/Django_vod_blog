from http.client import responses

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import BlogForm
from blog.models import Blog
from django.urls import reverse


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog_list.html', context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog': blog}

    return render(request, 'blog_detail.html', context)

@login_required()
def blog_create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        return redirect(reverse('blog-detail', kwargs={'pk': blog.pk}))


    context = {'form': form}
    return render(request, 'blog_create.html', context)

    # visits = int(request.COOKIES.get('visits', 0)) + 1
    #
    # request.session['count'] = request.session.get('count', 0) + 1
    # 'count': request.session['count'],
    # responses = render(request, 'blog_list.html', context)
    #
    # responses.set_cookie('visits', visits)