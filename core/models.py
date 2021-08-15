from django.db import models
from django.contrib.auth import get_user_model
from crum import get_current_user

# Create your models here.

User = get_user_model()

class Post(models.Model):
    text = models.CharField(max_length=140, blank=True, null=True)
    image = models.ImageField(upload_to = 'post_images')
    user = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __srt__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user # It will help to take automatically loggedin user.
        super(Post, self).save(*args, **kwargs)

    @property
    def likes_count(self):
        count = self.like_set.count()
        return count

    @property
    def comments_count(self):
        count = self.comment_set.count()
        return count


class Comment(models.Model):
    text = models.CharField(max_length=240)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE, editable=False)
    comment_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __srt__(self):
        return self.text

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(Comment, self).save(*args, **kwargs)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    liked_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __srt__(self):
        return str(self.post.id)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(Like, self).save(*args, **kwargs)

class Follow(models.Model):
    user = models.ForeignKey(User, related_name='follow_follower', on_delete=models.CASCADE, editable=False) #jisne follow kia
    followed = models.ForeignKey(User, related_name='follow_followed', on_delete=models.CASCADE) #jisko follow kia
    followed_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user} --> {self.followed}"

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(Follow, self).save(*args, **kwargs)

class SavedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    saved_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post.pk)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(SavedPost, self).save(*args, **kwargs)
