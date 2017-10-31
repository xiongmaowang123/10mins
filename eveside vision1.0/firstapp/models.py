from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    zanNum = models.IntegerField(default=0)
    pingLunNum = models.IntegerField(default=0)
    dongTaiNum = models.IntegerField(default=0)
    siXinNum = models.IntegerField(default=0)
    # guanZhuOrNot = models.IntegerField(default=0)
    videoNumber = models.IntegerField(null=True, blank=True,default=0)
    followingNumber = models.IntegerField(null=True, blank=True,default=0)
    followerNumber = models.IntegerField(null=True, blank=True,default=0)
    motto = models.CharField(max_length=50, null=True, blank=True)
    edu = models.CharField(max_length=20, null=True, blank=True)
    job = models.CharField(max_length=20, null=True, blank=True)
    nickname = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    SEX_CHOICES = {
        ('boy', '男'),
        ('girl', '女'),
        ('secret', '保密'),
    }
    sex = models.CharField(choices=SEX_CHOICES,max_length=10, blank=True)
    avatar = models.ImageField(upload_to='profile_image',default="profile_image\default.png",null=True, blank=True)
    belong_to = models.OneToOneField(to=User, related_name='profile',null=True, blank=True)
    # attentioner = models.ManyToManyField(to=UserProfile, related_name="myAttention", null=True, blank=True)
    def __str__(self):
        return str(self.nickname)

class Followers(models.Model):
    followers =  models.ForeignKey(to=UserProfile, related_name='follower',null=True, blank=True)
    followerId = models.IntegerField(default=0)
    def __str__(self):
        return str(self.followers)
class Followings(models.Model):
    followings = models.ForeignKey(to=UserProfile, related_name='following',null=True, blank=True)
    followingId = models.IntegerField(default=0)
    def __str__(self):
        return str(self.following)
class Video(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    content = models.TextField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True,default=0)
    views = models.IntegerField(null=True, blank=True,default=0)
    cover = models.FileField(upload_to='cover_image', null=True)
    editors_choice = models.BooleanField(default=False)
    owner = models.ForeignKey(to=UserProfile, related_name='videos')
    createtime = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    likes = models.IntegerField(null=True, blank=True,default=0)
    comment = models.TextField(null=True, blank=True)
    createtime = models.DateField(auto_now_add=True)
    commenter = models.ForeignKey(to=UserProfile, related_name="user_comment", null=True, blank=True)
    # loginer = models.ForeignKey(to=User, related_name="loginer_comments", null=True, blank=True)
    belong_to = models.ForeignKey(to=Video, related_name="under_comments", null=True, blank=True)
    def __str__(self):
        return str(self.id)

class Cmtticket(models.Model):
    createtime = models.DateField(auto_now=True)
    voter = models.ForeignKey(to=UserProfile, related_name="cmtuser_tickets")
    comment = models.ForeignKey(to=Comment, related_name="comment_tickets")

    ARTICLE_CHOICES = {
        ("like", "like"),
        ("dislike", "dislike"),
        ("normal", "normal")
    }
    choice = models.CharField(choices=ARTICLE_CHOICES, max_length=10)

    def __str__(self):
        return str(self.id)

class CommentCmt(models.Model):
    comment = models.TextField(null=True, blank=True)
    createtime = models.DateField(auto_now_add=True)
    commenter = models.ForeignKey(to=UserProfile, related_name="user_commentCmt", null=True, blank=True)
    # loginer = models.ForeignKey(to=User, related_name="loginer_comments", null=True, blank=True)
    belong_to = models.ForeignKey(to=Comment, related_name="under_commentsCmts", null=True, blank=True)
    def __str__(self):
        return self.commenter.nickname

class SiXin(models.Model):
    content = models.TextField(null=True, blank=True)
    createtime = models.DateField(auto_now_add=True)
    emiter = models.ForeignKey(to=UserProfile, related_name="myEmitSixin", null=True, blank=True)
    getter = models.ForeignKey(to=UserProfile, related_name="myGetSixin", null=True, blank=True)
    def __str__(self):
        return self.emiter.nickname

class Ticket(models.Model):
    createtime = models.DateField(auto_now=True)
    voter = models.ForeignKey(to=UserProfile, related_name="user_tickets")
    video = models.ForeignKey(to=Video, related_name="video_tickets")

    ARTICLE_CHOICES = {
        ("like", "like"),
        ("dislike", "dislike"),
        ("normal", "normal")
    }
    choice = models.CharField(choices=ARTICLE_CHOICES, max_length=10)

    def __str__(self):
        return str(self.id)

class Save(models.Model):
    createtime = models.DateField(auto_now=True)
    saver = models.ForeignKey(to=User, related_name="user_saves")
    video = models.ForeignKey(to=Video, related_name="video_saves")
    SAVE_CHOICES = {
        ("save", "save"),
        ("saved", "saved")
    }
    save_choice = models.CharField(choices=SAVE_CHOICES, max_length=10)

    def __str__(self):
        return str(self.saver.username)
