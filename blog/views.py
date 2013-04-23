#__encoding=utf-8__
import re

from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponseRedirect
from django.template import RequestContext

from blog.models import Author, Blog, Tag
from blog.forms import BlogForm


def blog_list(request, id=''):
    """
    get blog list， paging enabled
    """
    pattern = re.compile('^[1-9]+$')
    if pattern.match(id):
        id_int = int(id)
    else:
        id_int = 1

    all_posts = Blog.objects.all()
    total_count = len(all_posts)
    posts = all_posts[(id_int - 1) * 10:id_int * 10]
    tags = Tag.objects.all()
    pre_page = id_int - 1 if id_int > 1 else 1
    next_page = id_int + 1 if id_int * 10 < total_count else id_int
    return render_to_response("blog/blog_list.html",
                              {"posts": posts, "tags": tags, "pre": pre_page, "next": next_page})


def blog_show(request, id=''):
    """
    Get a blog detail by id
    """
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog/blog_show.html", {"blog": blog})


def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd['caption']
            author = Author.objects.get(id=1)
            content = cd['content']
            blog = Blog(caption=title, author=author, content=content)
            blog.save()
            id = Blog.objects.order_by('-publish_time')[0].id
            return HttpResponseRedirect('/blog/%s' % id)
    else:
        form = BlogForm()
    return render_to_response('blog/blog_add.html',
                              {'form': form}, context_instance=RequestContext(request))

def delete_blog(request, id=''):
    try:
        blog = Blog.objects.get(id=id)
    except Exception:
        raise Http404
    if blog:
        blog.delete()
    return blog_list(request, '1')

