"""eveside URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from firstapp.apis import video, register, readinfo, video_detail, readvote, postvote, readsave, postsave, comment, comment_list, changeInfo, save_articlelst, searchpageapi, writeArticle, postCmtVote, deleteCmt,commentCmt,endCheck,nicknameEndCheck,my_articlelst,deleteVid, peopleInfo, attention, deAttention, siXin,myGuanZhu,dongTai,pingLun,zan,pingLunZan,articlePingLun

from firstapp.tmps import index, detail, myinfo, searchpage, writeAtc, geRenXingXi
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index,name='index'),
    url(r'^searchpage/', searchpage),
    url(r'^detail/', detail, name="detail"),
    url(r'^myinfo/', myinfo, name="myinfo"),
    url(r'^writeAtc/', writeAtc, name="writeAtc"),
    url(r'^geRenXingXi/', geRenXingXi),


    url(r'^api/video/', video),
    url(r'^api/register/',register),
    url(r'^api/token-auth$',views.obtain_auth_token),
    url(r'^api/theuser/',readinfo),
    url(r'^api/video_detail/(?P<id>\d+)$',video_detail),
    url(r'^api/the_vote/(?P<id>\d+)$',readvote),
    url(r'^api/vote/(?P<id>\d+)$',postvote),
    url(r'^api/the_save/(?P<id>\d+)$',readsave),
    url(r'^api/save/(?P<id>\d+)$',postsave),
    url(r'^api/comment/(?P<id>\d+)$',comment),
    url(r'^api/comment_list/(?P<id>\d+)$',comment_list),
    url(r'^api/changeInfo/(?P<id>\d+)$',changeInfo),
    url(r'^api/save_articlelst/',save_articlelst),
    url(r'^api/peopleInfo/(?P<id>\d+)',peopleInfo),
    url(r'^api/attention/(?P<id>\d+)',attention),
    url(r'^api/deAttention/(?P<id>\d+)',deAttention),
    url(r'^api/siXin/(?P<id>\d+)',siXin),
    url(r'^api/myGuanZhu/',myGuanZhu),
    url(r'^api/dongTai/',dongTai),
    url(r'^api/pingLun/',pingLun),
    url(r'^api/articlePingLun/',articlePingLun),
    url(r'^api/zan/',zan),
    url(r'^api/pingLunZan/',pingLunZan),


    # url(r'^api/likeVote/(?P<id>\d+)$',likeVote),
    url(r'^api/searchpage/',searchpageapi),
    url(r'^api/writeArticle/(?P<id>\d+)',writeArticle),
    url(r'^api/cmtvote/(?P<id>\d+)$',postCmtVote),
    url(r'^api/deleteCmt/(?P<id>\d+)$',deleteCmt),
    url(r'^api/commentCmt/(?P<id>\d+)$',commentCmt),
    url(r'^api/endCheck/',endCheck),
    url(r'^api/nicknameEndCheck/',nicknameEndCheck),
    url(r'^api/my_articlelst/',my_articlelst),
    url(r'^api/deleteVid/(?P<id>\d+)$',deleteVid),
    ]





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
