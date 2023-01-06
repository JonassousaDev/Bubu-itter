from django.shortcuts import render
from .models import tweet
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class Tweetlistview(LoginRequiredMixin,ListView):
    model= tweet
    template_name= 'feed/home.html'
    ordering = ['-datetime']


class Tweetcreateview(LoginRequiredMixin,CreateView):
    model = tweet
    # template_name= 'feed/bubu_form.html'
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)


class TweetUpdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = tweet
    # template_name= 'feed/bubu_form.html'
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tweet = self.get_object()
        if(self.request.user == tweet.uname):
            return True
        return False



class TweetDeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = tweet
    fields = ['text']
    success_url = '/'

    # def form_valid(self, form):
    #     form.instance.uname = self.request.user
    #     return super().form_valid(form)

    def test_func(self):
        tweet = self.get_object()
        if(self.request.user == tweet.uname):
            return True
        return False