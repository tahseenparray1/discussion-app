from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('link/<int:pk>',views.link,name='link'),
    path('link/<int:pk>/delete',views.delLink,name='del_link'),
    path('link/<int:pk>/edit',views.editLink,name='edit_link'),
    path('link/<int:pk>/addcomment',views.addComment,name='add_comment'),
    path('link/<int:pk>/delcomment',views.delComment,name='del_comment'),
    path('link/<int:pk>/editcomment',views.editComment,name='edit_comment'),
    path('link/add', views.addLink,name='add_link'),
    path('login',views.logIn,name='log_in'),
    path('signin',views.signIn,name='sign_in'),
    path('logout',views.logOut,name='log_out'),
    path('link/<int:pk>/upvote',views.upvote,name='upvote'),
    path('link/<int:pk>/downvote',views.downvote,name='downvote'),
    path('link/<int:pk>/upvoters',views.upvoters,name='upvoters'),
    path('link/<int:pk>/downvoters',views.downvoters,name='downvoters'),

    
]