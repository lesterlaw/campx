from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^$', views.home, name="home"),
    url(r'^$', views.WishList.as_view(), name='wishlist' ),
    url(r'^info/(?P<pk>[0-9]+)/$', views.WishDetail.as_view(), name='wishdetail' ),
	# url(r'^join/(?P<wishcamp_id>[0-9]+)/$', views.WishJoin, name='wishjoin'),
    url(r'^new/$', 'wishcamps.views.WishNew', name='wishnew'),
    url(r'^edit/(?P<wishcamp_id>[0-9]+)/$', 'wishcamps.views.WishEdit', name='wishedit'),
    url(r'^delete/(?P<wishcamp_id>[0-9]+)/$', 'wishcamps.views.WishDelete', name='wishdelete'),
    url(r'^detail/(?P<wishcamp_id>[0-9]+)/$', 'wishcamps.views.WishJoinDetails', name='wishjoindetails'),
    url(r'^userlist/(?P<pk>[0-9]+)/$', views.userlist.as_view(), name='userlist'),
    url(r'^faq/$', 'wishcamps.views.faq', name='faq'),
]
