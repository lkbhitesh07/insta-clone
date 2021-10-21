from django.urls import path
from core.views import (HomeView, 
                FollowDoneView, 
                UnFollowDoneView, 
                PostCreateView, 
                PostDeleteView, 
                PostDetailView,
                PostLikeView,
                PostUnlikeView,
                PostCommentView,
                PostCommentDeleteView,
                PostSaveView,
                PostUnsaveView,
                ExploredPostsView,
                LikedPostsView,
                SavedPostsView
                )
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('feed/', login_required(HomeView.as_view()), name='home_feed_view'),
    path('follow/done/', login_required(FollowDoneView.as_view()), name='follow_done_view'),
    path('unfollow/done/', login_required(UnFollowDoneView.as_view()), name='unfollow_done_view'),

    # post related urls
    path('post/create/', login_required(PostCreateView.as_view()), name='post_create_view'),
    path('post/delete/<int:id>/', login_required(PostDeleteView.as_view()), name='post_delete_view'),
    path('post/save/<int:id>/', login_required(PostSaveView.as_view()), name='post_save_view'),
    path('post/unsave/<int:id>/', login_required(PostUnsaveView.as_view()), name='post_unsave_view'),
    path('post/detail/<int:id>/', login_required(PostDetailView.as_view()), name='post_detail_view'),
    path('post/like/<int:id>/', PostLikeView.as_view(), name='post_like_view'),
    path('post/unlike/<int:id>/', PostUnlikeView.as_view(), name='post_unlike_view'),
    path('post/comment/<int:id>/', PostCommentView.as_view(), name='post_comment_view'),
    path('post/comment/delete/<int:id>/', PostCommentDeleteView.as_view(), name='comment_delete_view'),
    path('post/liked/', LikedPostsView.as_view(), name='liked_posts_view'),
    path('post/explored/', ExploredPostsView.as_view(), name='explored_posts_view'),
    path('post/saved/', SavedPostsView.as_view(), name='posts_saved_view'),
]