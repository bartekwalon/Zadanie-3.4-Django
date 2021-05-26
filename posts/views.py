from django.shortcuts import render
from django.contrib import messages
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm
from django.views.generic import ListView

def posts_list(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            Post.objects.get_or_create(**form.cleaned_data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Nowy post został utworzony!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = PostForm()
    posts = Post.objects.all()
    title = 'Posty'
    return render(
        request=request,
        template_name="posts/list.html",
        context={"posts": posts, "title": title, "form": form}
    )


def post_details(request, id):
    post = Post.objects.get(id=id)
    title = 'Szczegóły postu'
    return render(
        request=request,
        template_name="posts/details.html",
        context={"post": post, 'title': title}
    )


def author_list(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowego autora!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = AuthorForm()
    authors = Author.objects.all()
    title = 'Autorzy'
    return render(
        request=request,
        template_name="posts/authors.html",
        context={"authors": authors, "title": title, "form": form}
    )


def author_details(request, id):
    author = Author.objects.get(pk=id)
    return render(
        request=request,
        template_name="posts/author.html",
        context={'author': author}
    )


class PostsList(ListView):
    model = Post
    template_name = "posts/list.html"
    form_class = PostForm
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostForm()
        return context