from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from .models import UserProfile, Video, Ticket, Comment, Save, Cmtticket, CommentCmt, Followers, Followings, SiXin
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        depth = 2



@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def writeArticle(request,id):
    if request.auth:
        canShu=request.GET.get('canShu')
        if canShu=='xiuGai':
            articleXiuGai=Video.objects.get(id=id)
            title = request.POST['title']
            cover = request.FILES['cover']
            content = request.POST['content']
            articleXiuGai.title=title
            articleXiuGai.cover=cover
            articleXiuGai.content=content
            articleXiuGai.save()
            return Response({'msg':'success!'},status=status.HTTP_201_CREATED)
        else:
            followerList=request.user.profile.follower.all()
            for fl in followerList:
                people=UserProfile.objects.get(id=fl.followerId)
                people.dongTaiNum+=1
                people.save()
            title = request.POST['title']
            cover = request.FILES['cover']
            content = request.POST['content']
            newvideo = Video(title=title,owner=request.user.profile,cover=cover,content=content)
            newvideo.save()
            request.user.profile.videoNumber+=1
            request.user.profile.save()
            return Response({'msg':'success!'},status=status.HTTP_201_CREATED)
    else:
        body = {"msg": "登陆后才能写文章"}
        return Response(body, status=status.HTTP_403_FORBIDDEN)

@api_view(['POST','DELETE'])
@authentication_classes((TokenAuthentication,))
def siXin(request,id):
    if request.auth:
        if request.method=='POST':
            content = request.POST['content']
            people = UserProfile.objects.get(id=id)
            people.siXinNum+=1
            people.save()
            newSiXin = SiXin(emiter=request.user.profile,content=content,getter=people)
            newSiXin.save()
            return Response({'msg':'success!'},status=status.HTTP_201_CREATED)
        elif request.method=='DELETE':
            deleteSiXin =SiXin.objects.get(id=id)
            deleteSiXin.delete()
            return Response({'msg':'success!'},status=status.HTTP_201_CREATED)
    else:
        body = {"msg": "登陆后才能发私信"}
        return Response(body, status=status.HTTP_403_FORBIDDEN)

@api_view(['DELETE'])
@authentication_classes((TokenAuthentication,))
def deleteVid(request,id):
    video = Video.objects.get(id=id)
    video.delete()
    request.user.profile.videoNumber-=1
    request.user.profile.save()
    return Response({'msg':'delete comment success'},status=status.HTTP_201_CREATED)
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('cmtuser_tickets','motto', 'edu', 'job', 'nickname', 'motto', 'email', 'sex', 'avatar', 'address','id','followerNumber','followingNumber','follower','following','myGetSixin','myEmitSixin','siXinNum','videoNumber','dongTaiNum','pingLunNum','zanNum')
        depth = 2
class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields = '__all__'
        depth = 1
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def attention(request,id):
    if request.auth:
        people = UserProfile.objects.get(id=id)
        newfollower=Followers(followers=people, followerId=request.user.profile.id)
        newfollower.save()
        people.followerNumber+=1
        people.save()
        newfollowing=Followings(followings=request.user.profile, followingId=id)
        request.user.profile.followingNumber += 1
        request.user.profile.save()
        newfollowing.save()
    return Response({'msg':'success!'},status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@authentication_classes((TokenAuthentication,))
def deAttention(request,id):
    if request.auth:
        people = UserProfile.objects.get(id=id)
        follower = Followers.objects.filter(followers=people, followerId=request.user.profile.id)
        follower.delete()
        people.followerNumber-=1
        people.save()
        following = Followings.objects.filter(followings=request.user.profile, followingId=id)
        following.delete()
        request.user.profile.followingNumber-=1
        request.user.profile.save()
    return Response({'msg':'success!'},status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def myGuanZhu(request):
    if request.auth:
        user=request.user.profile
        print(user.following.all().count())
        peopleList=[UserProfile.objects.get(id=people.followingId) for people in user.following.all()]
        # for people in peopleList:
        #     if Followers.objects.filter(followers=people, followerId=request.user.profile.id):
        #         people.guanZhuOrNot=1
        #         people.save()
        pagerobot = Paginator(peopleList,4)                         #创建分页器，每页限定五篇文章
        page_num = request.GET.get("page")                            #取到当前页数
        try:
            peopleList = pagerobot.page(page_num)                   #一般情况下返回当前页码下的文章
        except EmptyPage:
            peopleList = pagerobot.page(pagerobot.num_pages)        #如果不存在该业，返回最后一页
        except PageNotAnInteger:
            peopleList = pagerobot.page(1)                          #如果页码不是一个整数，返回第一页
        pages = len(peopleList.paginator.page_range)
        peopleList = UserProfileSerializer(peopleList,many=True)
        context={}
        context={
          "pages":pages,
          "peopleList":peopleList.data,
        }
        return Response(context,status=status.HTTP_201_CREATED)
    else:
        Response({"msg": "Auth fail"},status=status.HTTP_403_FORBIDDEN)
def f(x):
    return x.id
# def swap(lst,i,j):
#      tmp = lst[i]
#      lst[i]=lst[j]
#      lst[j] = tmp
# def selection_sort_v2(lst):
#     for i in range(len(lst)):
#         min_index=i
#         for j in range(i+1,len(lst)):
#             if lst[j].createtime<lst[min_index].createtime:
#                 min_index = j
#                 swap(lst,i,min_index)
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def dongTai(request):
    if request.auth:
        user=request.user.profile
        peopleList=[UserProfile.objects.get(id=people.followingId) for people in user.following.all()]
    lst=[]
    for people in peopleList:
        vList=Video.objects.filter(owner=people).order_by("-id")[:10]
        lst.extend(vList)
    lst.sort(key=lambda x:x.id,reverse=True)
    lst=VideoSerializer(lst,many=True)
    return Response(lst.data,status=status.HTTP_201_CREATED)



@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def peopleInfo(request,id):
    if request.auth:
        people = UserProfile.objects.get(id=id)
        if Followers.objects.filter(followers=people, followerId=request.user.profile.id):
            people.guanZhuOrNot=1
        else:
            people.guanZhuOrNot=0
        people.save()
        video_list=Video.objects.filter(owner=people).order_by("-id")
        pagerobot = Paginator(video_list,4)
        page_num = request.GET.get("page")
        try:
            video_list = pagerobot.page(page_num)                   #一般情况下返回当前页码下的文章
        except EmptyPage:
            video_list = pagerobot.page(pagerobot.num_pages)        #如果不存在该业，返回最后一页
        except PageNotAnInteger:
            video_list = pagerobot.page(1)                          #如果页码不是一个整数，返回第一页
        pages = len(video_list.paginator.page_range)                #取总页数

        video_list = VideoSerializer(video_list,many=True)
        people = UserProfileSerializer(people)
        context={}
        context={
          "pages":pages,
          "video_list":video_list.data,
          "people":people.data
        }
        return Response(context,status=status.HTTP_201_CREATED)
    else:
        Response({"msg": "Auth fail"},status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def save_articlelst(request):
    save_ticketlst=Save.objects.filter(saver=request.user, save_choice='saved').order_by('-id')
    video_list=[tkt.video for tkt in save_ticketlst]
    pagerobot = Paginator(video_list,4)                         #创建分页器，每页限定五篇文章
    page_num = request.GET.get("page")                            #取到当前页数
    try:
        video_list = pagerobot.page(page_num)                   #一般情况下返回当前页码下的文章
    except EmptyPage:
        video_list = pagerobot.page(pagerobot.num_pages)        #如果不存在该业，返回最后一页
    except PageNotAnInteger:
        video_list = pagerobot.page(1)                          #如果页码不是一个整数，返回第一页
    pages = len(video_list.paginator.page_range)                #取总页数

    video_list = VideoSerializer(video_list,many=True)

    context={}
    context={
      "pages":pages,
      "video_list":video_list.data
    }
    return Response(context,status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def my_articlelst(request):
    video_list=Video.objects.filter(owner=request.user.profile).order_by("-id")

    pagerobot = Paginator(video_list,4)                         #创建分页器，每页限定五篇文章
    page_num = request.GET.get("page")                            #取到当前页数
    try:
        video_list = pagerobot.page(page_num)                   #一般情况下返回当前页码下的文章
    except EmptyPage:
        video_list = pagerobot.page(pagerobot.num_pages)        #如果不存在该业，返回最后一页
    except PageNotAnInteger:
        video_list = pagerobot.page(1)                          #如果页码不是一个整数，返回第一页
    pages = len(video_list.paginator.page_range)                #取总页数

    video_list = VideoSerializer(video_list,many=True)

    context={}
    context={
      "pages":pages,
      "video_list":video_list.data
    }
    return Response(context,status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def video(request):
    fenLei = request.GET.get("fenLei")
    if fenLei=='new':
        video_list = Video.objects.all().order_by("-id")[:6]
    elif fenLei=='editor':
        video_list = Video.objects.all().order_by("-likes")[:6]
    else:
        video_list = Video.objects.all().order_by("-likes","-id") #取出所有文章
    pagerobot = Paginator(video_list,9)                         #创建分页器，每页限定五篇文章
    page_num = request.GET.get("page")                            #取到当前页数
    try:
        video_list = pagerobot.page(page_num) #一般情况下返回当前页码下的文章


    except EmptyPage:
        video_list = pagerobot.page(pagerobot.num_pages)
          #如果不存在该业，返回最后一页
    except PageNotAnInteger:
        video_list = pagerobot.page(1)     #如果页码不是一个整数，返回第一页

    pages = len(video_list.paginator.page_range)                #取总页数

    video_list = VideoSerializer(video_list,many=True)

    context={}
    context={
      "pages":pages,
      "video_list":video_list.data
    }
    return Response(context,status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def searchpageapi(request):
    if not request.auth:
        Response({"msg": "Auth fail"},status=status.HTTP_403_FORBIDDEN)
    fenLei = request.GET.get("fenLei")
    tag=request.GET.get('q')
    if fenLei=='new':
        video_list = Video.objects.all().filter(content__contains=tag).order_by("-id")[:5]
    elif fenLei=='editor':
        video_list = Video.objects.all().filter(content__contains=tag).order_by("-likes")[:5]
    else:
        video_list = Video.objects.all().filter(content__contains=tag).order_by("-likes","-id") #取出所有文章
    pagerobot = Paginator(video_list,6)                         #创建分页器，每页限定五篇文章
    page_num = request.GET.get("page")                            #取到当前页数
    try:
        video_list = pagerobot.page(page_num)                   #一般情况下返回当前页码下的文章
    except EmptyPage:
        video_list = pagerobot.page(pagerobot.num_pages)        #如果不存在该业，返回最后一页
    except PageNotAnInteger:
        video_list = pagerobot.page(1)                          #如果页码不是一个整数，返回第一页
    pages = len(video_list.paginator.page_range)                #取总页数

    video_list = VideoSerializer(video_list,many=True)

    context={}
    context={
      "pages":pages,
      "video_list":video_list.data
    }
    return Response(context,status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def video_detail(request, id):

    video = Video.objects.get(id=id)
    video.views+=1
    video.save()
    Servideo = VideoSerializer(video)
    return Response(Servideo.data,status=status.HTTP_200_OK)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile', 'username','password','user_saves')
        depth = 2
@api_view(['POST'])
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if len(User.objects.filter(username=username))>0:
        return Response({'msg':'username already exist'}, status=status.HTTP_403_FORBIDDEN)
    else:
        newuser = User(username=username)
        newuser.set_password(password)
        newuser.save()
        newprofile=UserProfile(nickname=newuser.username,belong_to=newuser)
        newprofile.save()
        return Response({'msg':'register success'},status=status.HTTP_201_CREATED)
@api_view(['POST'])
def endCheck(request):
    username = request.POST.get('username')
    if len(User.objects.filter(username=username))>0:
        return Response({'result':0},status=status.HTTP_201_CREATED)
    else:
        return Response({'result':1},status=status.HTTP_201_CREATED)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def nicknameEndCheck(request):
    if request.auth:
        nickname = request.POST.get('nickname')
        if len(UserProfile.objects.filter(nickname=nickname))>0 and request.user.profile.nickname!=nickname:
            return Response({'result':0},status=status.HTTP_201_CREATED)
        else:
            return Response({'result':1},status=status.HTTP_201_CREATED)

class SiXinSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiXin
        fields = ('content', 'createtime','emiter','getter')
        depth = 2

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def readinfo(request):
    if request.auth:
        userProfile = UserProfile.objects.filter(belong_to=request.user)
        for i in userProfile:
            siXin=i.myGetSixin.all().order_by("-id")
            siXin = SiXinSerializer(siXin,many=True)
            info = UserProfileSerializer(i)
        context={}
        context={
            'siXin':siXin.data,
            'info':info.data
        }

        return Response(context,status=status.HTTP_201_CREATED)
    else:
        return Response({"msg": "Auth fail"},status=status.HTTP_403_FORBIDDEN)



@api_view(['POST','PUT'])
@authentication_classes((TokenAuthentication,))
def changeInfo(request,id):
    if not request.auth:
        Response({"msg": "Auth fail"},status=status.HTTP_403_FORBIDDEN)
    if request.method=='POST':
        email=request.POST.get('email')
        nickname=request.POST.get('nickname')
        # address=request.POST.get('address')
        job=request.POST.get('job')
        edu=request.POST.get('edu')
        motto=request.POST.get('motto')
        img = request.FILES.get('img')
        sex=request.POST.get('sex')
        password=request.POST.get('password')
        info=request.user.profile
        info.nickname=nickname
        # info.address=address
        info.job=job
        info.edu=edu
        info.motto=motto
        info.sex=sex
        info.avatar=img
        info.email=email
        info.save()
        if password!="":
            request.user.set_password(password)
            request.user.save()
    if request.method=='PUT':
        people=request.user.profile
        if int(id)==1:
            people.dongTaiNum=0
            people.save()
        elif int(id)==2:
            people.siXinNum=0
            people.save()
        elif int(id)==3:
            people.pingLunNum=0
            people.save()
        else:
            people.zanNum=0
            people.save()
    return Response({'msg':'changeinfo success'},status=status.HTTP_201_CREATED)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        depth = 2

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def readvote(request,id):
    if request.auth:
        voter = request.user.profile
        try:
            user_ticket_for_this_video = Ticket.objects.get(voter=voter, video_id=id)
            serializer = TicketSerializer(user_ticket_for_this_video)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({"msg": "have never vote"}, status=status.HTTP_403_FORBIDDEN)
    else:
        body = {"msg": "Auth fail"}
        return Response(body, status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def postvote(request,id):
    try:
        user_ticket_for_this_video = Ticket.objects.get(voter=request.user.profile, video_id=id)
        vote = request.POST["user_ticket"]
        video=Video.objects.get(id=id)
        if vote=='like':
            if request.user.profile.id!=video.owner_id:
                video=Video.objects.get(id=id)
                video.owner.zanNum+=1
                video.owner.save()
        user_ticket_for_this_video.choice = vote
        user_ticket_for_this_video.save()
        video=Video.objects.get(id=id)
        count=Ticket.objects.filter(choice="like", video=video).count()
        video.likes=count
        video.save()

        return Response({"msg":"vote success"},status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist:
        vote = request.POST["user_ticket"]
        if vote=='like':
            video=Video.objects.get(id=id)
            if request.user.profile.id!=video.owner_id:
                video.owner.zanNum+=1
                video.owner.save()
        new_ticket=Ticket(voter=request.user.profile, video_id=id, choice=vote)
        new_ticket.save()
        video=Video.objects.get(id=id)
        video.likes+=1
        video.save()

        return Response({"msg": "success"},status=status.HTTP_201_CREATED)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def postCmtVote(request,id):
    try:
        user_ticket_for_this_videocmt = Cmtticket.objects.get(voter=request.user.profile, comment_id=id)
        vote = request.POST["usercmt_ticket"]
        user_ticket_for_this_videocmt.choice = vote
        user_ticket_for_this_videocmt.save()
        comment=Comment.objects.get(id=id)
        if vote=='like' and request.user.userinfo.id!=id:
            comment.commenter.zanNum+=1
            comment.commenter.save()
        count=Cmtticket.objects.filter(choice="like", comment=comment).count()
        comment.likes=count
        comment.save()
        return Response({"msg":"vote success"},status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist:
        vote = request.POST["usercmt_ticket"]
        new_cmtticket=Cmtticket(voter=request.user.profile, comment_id=id, choice=vote)
        new_cmtticket.save()
        comment=Comment.objects.get(id=id)
        if vote=='like':
            comment.commenter.zanNum+=1
            comment.commenter.save()
        count=Cmtticket.objects.filter(choice="like", comment=comment).count()
        comment.likes=count
        comment.save()
        return Response({"msg": "success"},status=status.HTTP_201_CREATED)

class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = '__all__'
        depth = 1

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def readsave(request,id):
    if request.auth:
        saver_id = request.user.id
        try:
            user_save_for_this_video = Save.objects.get(saver_id=saver_id, video_id=id)
            serializer = SaveSerializer(user_save_for_this_video)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({"msg": "have no save operation"}, status=status.HTTP_403_FORBIDDEN)
    else:
        body = {"msg": "Auth fail"}
        return Response(body, status=status.HTTP_403_FORBIDDEN)
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def postsave(request,id):
    saver_id = request.user.id
    try:
        user_save_for_this_video = Save.objects.get(saver_id=saver_id, video_id=id)
        user_save_for_this_video.save_choice = request.POST["save_choice"]
        user_save_for_this_video.save()
        return Response({"msg": "success"},status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist:

        new_save=Save(saver_id=saver_id, video_id=id, save_choice=request.POST["save_choice"])
        new_save.save()
        return Response({"msg": "success"},status=status.HTTP_201_CREATED)



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', 'createtime','commenter','belong_to', 'likes','id','under_commentsCmts')
        depth = 2



class CommentCmtSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentCmt
        fields = '__all__'
        depth = 3

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def pingLun(request):
    if request.auth:
        comment_list=Comment.objects.filter(commenter=request.user.profile)
        scomment_lst=[]
        for comment in comment_list:
            for pingLun in comment.under_commentsCmts.all():
                scomment_lst.append(pingLun)
    scomment_lst.sort(key=f,reverse=True)
    scomment_lst=CommentCmtSerializer(scomment_lst[:10],many=True)
    return Response(scomment_lst.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def articlePingLun(request):
    if request.auth:
        article_list=Video.objects.filter(owner=request.user.profile)
        comment_lst=[]
        for article in article_list:
            for pingLun in article.under_comments.all():
                comment_lst.append(pingLun)
    comment_lst.sort(key=f,reverse=True)
    comment_lst=CommentSerializer(comment_lst[:10],many=True)
    return Response(comment_lst.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def zan(request):
    if request.auth:
        myTicketLst=[]
        for video in request.user.profile.videos.all():
            ticket_list=Ticket.objects.filter(choice='like',video=video)
            for ticket in ticket_list:
                if ticket.voter_id!=request.user.profile.id:
                    myTicketLst.append(ticket)
    myTicketLst.sort(key=f,reverse=True)
    myTicketLst=TicketSerializer(myTicketLst[:10],many=True)
    return Response(myTicketLst.data,status=status.HTTP_201_CREATED)

class CmtticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cmtticket
        fields = ('createtime','voter','comment','choice')
        depth = 2
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def pingLunZan(request):
    if request.auth:
        myTicketLst=[]
        for comment in request.user.profile.user_comment.all():
            ticket_list=Cmtticket.objects.filter(choice='like',comment=comment)
            for ticket in ticket_list:
                if ticket.voter_id!=request.user.profile.id:
                    myTicketLst.append(ticket)
    myTicketLst.sort(key=f,reverse=True)
    myTicketLst=CmtticketSerializer(myTicketLst[:10],many=True)
    return Response(myTicketLst.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def comment_list(request, id):
    comment_list=Comment.objects.filter(belong_to_id=id).order_by('-likes')
    # if request.auth:
    #     for comment in comment_list:
    #         if comment.commenter==request.user.profile:
    #             comment.thisCmt=1
    #             comment.thisRpl=0
    #
    #         else:
    #             comment.thisCmt=0
    #             comment.thisRpl=1
    # else:
    #     for comment in comment_list:
    #         comment.thisCmt=0
    #         comment.thisRpl=1
    # if request.auth:
    #     for comment in comment_list:
    #         try:
    #             cmtTicket=Cmtticket.objects.get(voter=request.user.profile, comment=comment)
    #             if cmtTicket.choice=="like":
    #                 comment.thisLike=1
    #                 comment.thisDislike=0
    #                 comment.save()
    #             elif cmtTicket.choice=="dislike":
    #                 comment.thisLike=0
    #                 comment.thisDislike=1
    #                 comment.save()
    #             else:
    #                 comment.thisLike=0
    #                 comment.thisDislike=0
    #                 comment.save()
    #         except ObjectDoesNotExist:
    #             pass
    # else:
    #     for comment in comment_list:
    #         comment.thisLike=0
    #         comment.thisDislike=0
    #         comment.save()
    serializer = CommentSerializer(comment_list,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def comment(request,id):
    comment = request.POST['comment']
    newcomment = Comment(comment=comment,belong_to_id=id,commenter=request.user.profile)
    newcomment.save()
    article=Video.objects.get(id=id)
    article.owner.pingLunNum+=1
    article.owner.save()
    newCmtTichie=Cmtticket(comment=newcomment, voter=request.user.profile, choice="normal")
    newCmtTichie.save()

    return Response({'msg':'comment success'},status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@authentication_classes((TokenAuthentication,))
def deleteCmt(request,id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return Response({'msg':'delete comment success'},status=status.HTTP_201_CREATED)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def commentCmt(request,id):
    comment=Comment.objects.get(id=id)
    comment.commenter.pingLunNum+=1
    comment.commenter.save()
    commentCmt = request.POST['commentCmt']
    newCommentCmt = CommentCmt(comment=commentCmt,belong_to_id=id,commenter=request.user.profile)
    newCommentCmt.save()
    return Response({'msg':'comment success'},status=status.HTTP_201_CREATED)
    # except ObjectDoesNotExist:
    #     newprofile=UserProfile(nickname=request.user.username,belong_to=request.user)
    #     newprofile.save()
    #     commentCmt = request.POST['commentCmt']
    #     newCommentCmt = CommentCmt(comment=commentCmt,belong_to_id=id,commenter=request.user.profile)
    #     newCommentCmt.save()
    #     return Response({'msg':'comment success'},status=status.HTTP_201_CREATED)
