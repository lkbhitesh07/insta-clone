from django.http import request
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView, View
from django.contrib.auth import get_user_model
from core.models import Comment, Follow, Post, Like, SavedPost
from core.forms import PostCreationForm
from django.db.models import Count

User = get_user_model()

# Create your views here.
class HomeView(View):
    form_class = PostCreationForm
    template_name = 'core/feed.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        all_posts = Post.objects.all()
        context = {'form': form, 'all_posts': all_posts}
        return render(request, self.template_name, context=context)

class PostCreateView(View):
    template_name = 'core/feed.html'
    form_class = PostCreationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home_feed_view')

        else:
            context = {'form': form}
            return render(request, self.template_name, context=context)

class PostDeleteView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        try:
            post_obj = Post.objects.get(pk=post_id)
        except Exception as e:
            pass
        if request.user == post_obj.user:
            post_obj.delete()

        return redirect(request.META.get('HTTP_REFERER'))

class PostSaveView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')

        #checking if the post exists
        try:
            post_obj = Post.objects.get(pk=post_id)
        except:
            pass

        #saving the post
        try:
            SavedPost.objects.create(post_id=post_id)
        except:
            pass
        
        return redirect(request.META.get('HTTP_REFERER'))

class PostUnsaveView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        try:
            saved_obj = SavedPost.objects.get(user=request.user, post_id=post_id)
            saved_obj.delete()
        except:
            pass
        return redirect(request.META.get('HTTP_REFERER'))

class PostDetailView(View):
    template_name = 'core/post_detail.html'
    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        try:
            post_obj = Post.objects.get(pk=post_id)
        except:
            return redirect(request.META.get('HTTP_REFERER'))

        #checking if the post is liked by the user
        try:
            Like.objects.get(user=request.user, post_id=post_id)
            liked_this_post = True
        except Exception as e:
            liked_this_post = False

        #checking if the post is saved by the user
        try:
            SavedPost.objects.get(user=request.user, post_id=post_id)
            post_saved = True
        except Exception as e:
            post_saved = False

        context = {'post': post_obj, 
            'liked_this_post':liked_this_post,
            'post_saved':post_saved,
            }

        return render(request, self.template_name, context=context)

class PostLikeView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        try:
            Like.objects.get(user=request.user, post_id=post_id)
        except:
            Like.objects.create(user=request.user, post_id=post_id)
        return redirect(request.META.get('HTTP_REFERER'))

class PostUnlikeView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        try:
            like_obj = Like.objects.get(user=request.user, post_id=post_id)
            like_obj.delete()
        except:
            pass
        return redirect(request.META.get('HTTP_REFERER'))

class PostCommentView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        comment_text = request.POST.get('comment_text')
        Comment.objects.create(post_id=post_id, text=comment_text)
        return redirect(request.META.get('HTTP_REFERER'))

class PostCommentDeleteView(View):
    def post(self, request, *args, **kwargs):
        comment_id = kwargs.get('id')
        try:
            comment_obj = Comment.objects.get(pk=comment_id)
        except Exception as e:
            pass
        if request.user == comment_obj.user:
            comment_obj.delete()

        return redirect(request.META.get('HTTP_REFERER'))


class FollowDoneView(View):
    def post(self, request, *args, **kwargs):
        followed_user_id = request.POST.get('followed_user_id')
        followed_user_obj = User.objects.get(pk=followed_user_id)

        try:
            Follow.objects.get(user=request.user, followed=followed_user_obj)
        except Exception as e:
            follow_obj = Follow.objects.create(followed=followed_user_obj)

        return redirect(request.META.get('HTTP_REFERER'))

class UnFollowDoneView(View):
    def post(self, request, *args, **kwargs):
        unfollowed_user_id = request.POST.get('unfollowed_user_id')
        unfollowed_user_obj = User.objects.get(pk=unfollowed_user_id)

        try:
            follow_obj = Follow.objects.get(user=request.user, followed=unfollowed_user_obj)
            follow_obj.delete()
        except Exception as e:
            pass

        return redirect(request.META.get('HTTP_REFERER'))

class LikedPostsView(View):
    template_name = 'core/liked_posts.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ExploredPostsView(View):
    template_name = 'core/posts_explore.html'
    def get(self, request, *args, **kwargs):
        all_posts = Post.objects.annotate(count=Count('like')).order_by('-count')
        context = {'all_posts':all_posts}
        return render(request, self.template_name, context=context)

class SavedPostsView(View):
    template_name = 'core/saved_posts.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
