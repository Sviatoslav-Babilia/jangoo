from blog.models import Post


def get_next(pk):
    posts = list(Post.objects.order_by('-pk'))
    #import pdb; pdb.set_trace()
    next_post = posts[-1]
    for post in posts:
        if post.pk == pk:
            break
        next_post = post
    return next_post


def get_prev(pk):
    posts = list(Post.objects.order_by('pk'))
    #import pdb; pdb.set_trace()
    prev_post = posts[-1]
    for post in posts:
        if post.pk == pk:
            break
        prev_post = post
    return prev_post