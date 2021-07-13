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

    def __srt__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk: #sometimes user gets deleted from DB but is their in request or session so that's why we are doing this check.
            user = None
        if not self.pk: # Here we are doing this because until the super method below is not run we will not get any pk because the model is still not created.
            self.user = user # as we have done Post.user ediatable = False , so now from this it will automatically take logedin user.
        super(Post, self).save(*args, **kwargs) #calling Model's save method(means calling save method of parent from child)


class Comment(models.Model):
    text = models.CharField(max_length=240)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # Now what if the Post class we created was below this comment class then we wouldn't be able to reference it so for that we had to do 'core.Post' .
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
    is_like = models.BooleanField(default=True)
    liked_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __srt__(self):
        return str(self.is_like)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(Like, self).save(*args, **kwargs)

class Follow(models.Model):
    #Reverse access for Follow.user will clash with Follow.follower - This error we will get when we try to run without related_name, it's because here user, follower
    # are accessing the User table but when reverse will happen then we will get an error as when we access the table then a default name is their which is
    # 'The-table-we-are-accessing_set' , so when User will go for Follow table then for both user and follow the name will be Follow_set. That's why related_name is req.
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
