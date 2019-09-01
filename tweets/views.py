from django.shortcuts import render,redirect,get_object_or_404
from .models import Tweet
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .forms import TweetForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class TweetListView(ListView):
    model = Tweet
    template_name = 'list_view.html'
    


class TweetDetailView(DetailView):
    model = Tweet
    template_name = 'tweet_detail.html'

class TweetCreateView(LoginRequiredMixin,CreateView):
    model = Tweet
    form_class = TweetForm

    template_name = 'create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save() 
        return super().form_valid(form)


class TweetUpdateView(LoginRequiredMixin,UpdateView):
    model = Tweet
    template_name = 'update_view.html'
    fields=['content']
    login_url='/admin/login'