from django.shortcuts import render, get_object_or_404, redirect
from .models import News,Comment
from django.db.models import Q
from django.views.generic import (
     CreateView,
     DeleteView,
     DetailView,
     ListView,
     UpdateView,
)
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import NewsForm,CommentForm

# BASE VIEW CLass = VIEW
class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
        
class NewsObjectMixin(object):
    model = News
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj 

class NewsDeleteView(NewsObjectMixin,LoginRequiredMixin, DeleteView):
    template_name = "news/news_delete.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/news/')
        return render(request, self.template_name, context)


class NewsUpdateView(NewsObjectMixin,LoginRequiredMixin, UpdateView):
    template_name = "news/news_update.html" # DetailView
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(News, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = NewsForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = NewsForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)





class NewsListView(ListView):
    template_name = "news/news_list.html"
    queryset = News.objects.all().order_by("-date")

    def get_queryset(self):
            return self.queryset

    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        if query:
            self.queryset = self.queryset.filter(
                Q(title__icontains= query) |
                Q(content__icontains= query) 
                #Q(author__icontains = query) 
                ).distinct()
        context = {'object_list': self.queryset}
        
        return render(request, self.template_name, context)


class NewsDetailView(NewsObjectMixin, DetailView):
    template_name = "news/news_detail.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        obj = self.get_object()
        comments = Comment.objects.filter(post=obj).order_by("-date")
        context = {
            'object': obj ,
            'comments': comments ,
        }
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        # GET method
        obj = self.get_object()
        comments = Comment.objects.filter(post=obj).order_by("-date")
        if obj is not None:
            context = {
                'object': obj ,
                'comments': comments ,
            }
        return render(request, self.template_name, context)
    
    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {})

class NewsCreateView(LoginRequiredMixin,CreateView):
    template_name = "news/news_create.html" # DetailView
    def get(self, request, *args, **kwargs):
        # GET method
        form = NewsForm()
        context = {"form": form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        # POST method
        form = NewsForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            #form.instance.author = self.request.user
            #form.save()
            form = NewsForm()
            return redirect('news:news_list')
        context = {"form": form}
        return render(request, self.template_name, context)


#def post(request, id):
#    post = get_object_or_404(News, id = id)
#    form = CommentForm()
#    if request.method == "POST":
#        form = CommentForm(request.POST, author=request.user, post=post)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(request.path)
#    return render(request, "news/news_detail.html", {"post": post, "form": form})


    

# HTTP METHODS
#def my_fbv(request, *args, **kwargs):
#   print(request.method)
#    return render(request, 'news.html', {})