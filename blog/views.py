from django.shortcuts import render
from blog.models import Post, Comment, Headliner, Contacts, Category
from .forms import CommentForm, ContactsCreate, UpdateРоstForm, CommentCreateForm
from django.views import generic
from blog.helper import get_next, get_prev
from django.template import RequestContext
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView
from django.urls import reverse

# class ExtraData:
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['headliners'] = Headliner.objects.all()
#         return context


class BlogView(generic.ListView):
    template_name = 'blog_index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-created_on')[:5]

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        # Add in a QuerySet of all the books
#        context['headliners'] = Headliner.objects.all()
#        return context


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
       "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


# def blog_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     headliners = Headliner.objects.all()
#
#     form = CommentForm()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment(
#                 author=form.cleaned_data["author"],
#                 body=form.cleaned_data["body"],
#                 post=post
#             )
#             comment.save()
#
#     query = Comment.objects.filter(post=post)
#     comments = query[:5]
#     num_comments = query.count()
#     context = {
#         "post": post,
#         "comments": comments,
#         "form": form,
#         "prev_post": get_prev(pk),
#         "next_post": get_next(pk),
#         "headliners": headliners,
#         "num_comments": num_comments
#     }
#
#     return render(request, "blog_detail.html", context)

class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        headliners = Headliner.objects.all()
        query = Comment.objects.filter(post=post)
        comments = query[:5]
        num_comments = query.count()
        #form = CommentForm()

        context = super().get_context_data(**kwargs)
        context['prev_post'] = get_prev(pk)
        context['comments'] = comments
        context['next_post'] = get_next(pk)
        context['headliners'] = headliners
        context['num_comments'] = num_comments
        #context['form'] = form
        #import pdb; pdb.set_trace()
        return context


class ContactCreate(FormView):
    template_name = 'blog_contacts.html'
    form_class = ContactsCreate
    success_url = '/blog/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        Contacts.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone']
        )
        return super().form_valid(form)


def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")


class PostCreate(FormView):
    template_name = 'new_blog.html'
    form_class = UpdateРоstForm
    success_url = '/blog/success/'

    def form_valid(self, form):
        #import pdb; pdb.set_trace()
        #category = Category.objects.get(id=form.cleaned_data['categories'])
        Post.objects.create(
            title=form.cleaned_data['title'],
            body=form.cleaned_data['body'],
            #created_on=form.cleaned_data['created_on'],
            #last_modified=form.cleaned_data['last_modified'],
            categories=form.cleaned_data['categories'],
            memmo=form.cleaned_data['memmo']
        )
        return super().form_valid(form)

    # form = UpdateРоstForm()
    # if request.method == 'POST':
    #     form = UpdateРоstForm(request.POST)
    #     if form.is_valid():
    #          = Comment(
    #             author=form.cleaned_data["author"],
    #             body=form.cleaned_data["body"],
    #             post=post
    #         )
    #         comment.save()


class BlogEditView(UpdateView):
    form_class = UpdateРоstForm
    model = Post
    template_name = "post_form.html"
    success_url = '/blog/success/'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = '/blog/success/'


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = '/blog/success/'

    def get_success_url(self):
        #comment = Comment.objects.get(pk=self.kwargs['pk'])
        comment = self.object
        return reverse('blog_detail', kwargs={'pk': comment.post.id})


class CommentCreate(CreateView):
    template_name = 'new_comment.html'
    form_class = CommentCreateForm
    success_url = '/blog/success/'

    def form_valid(self, form):
        # form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        #comment = Comment.objects.get(pk=self.kwargs['pk'])
        comment = self.object
        return reverse('blog_detail', kwargs={'pk': comment.post.id})

    # def post(self, request, *args, **kwargs):
    #     #self.object = None
    #     import pdb;
    #     pdb.set_trace()
    #     return super().post(request, *args, **kwargs)

