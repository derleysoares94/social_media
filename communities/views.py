from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Community, Post, Membership, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
    
def home(request):
    context = {
        'communities': Community.objects.all(),
    }
    return render(request, 'communities/home.html', context)

## Communities classes.
class CommunityListView(ListView):
    model = Community
    template_name = 'communities/home.html'
    context_object_name = 'communities'
    ordering = ['-created_at']
    paginate_by = 5

class CommunityCreateView(LoginRequiredMixin, CreateView):
    model = Community
    fields = ['name', 'image', 'description']
    success_url = reverse_lazy('communities-home')
    
    #Overriding form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user 
        response = super().form_valid(form) 
        Membership.objects.create(user=self.request.user, community=self.object)
        return response

class CommunityDetailView(DetailView):
    model = Community
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(community=self.object)
        context['member_count'] = self.object.member_count()
        return context
    
class CommunityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Community
    fields = ['name', 'image', 'description']
    
    #Overriding form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
    def test_func(self):
        community = self.get_object()
        return self.request.user == community.author

class CommunityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Community
    success_url = "/"
    
    def test_func(self):
        community = self.get_object()
        return self.request.user == community.author
   
@login_required
def subscribe(request, community_id):
    community = get_object_or_404(Community, id=community_id)
    Membership.objects.get_or_create(user=request.user, community=community)
    return redirect('community-detail', pk=community.id)

@login_required
def unsubscribe(request, community_id):
    community = get_object_or_404(Community, id=community_id)
    membership = Membership.objects.filter(user=request.user, community=community)
    if membership.exists():
        membership.delete()
    return redirect('community-detail', pk=community.id)
    
## Posts classes.

class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context

def post_create(request, community_id):
    community = get_object_or_404(Community, id=community_id)
    
    if not Membership.objects.filter(user=request.user, community=community).exists():
            return redirect('community-detail', pk=community.id)
        
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.community = community
            post.save()
            return redirect('community-detail', pk=community.id)
    else:
        form = PostForm()
    return render(request, 'community_detail.html', {'form': form, 'community': community})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    #Overriding form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('community-detail', kwargs={'pk': self.object.community.id})
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    
    def get_success_url(self):
        return reverse_lazy('community-detail', kwargs={'pk': self.object.community.id})
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if not Membership.objects.filter(user=request.user, community=post.community).exists():
            return redirect('community-detail', pk=post.community.id)
        
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.id)
    else:
        form = PostForm()
    return render(request, 'post_detail.html', {'form': form, 'post': post})