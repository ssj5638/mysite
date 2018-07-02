"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import main.views as mv
import guestbook.views as gv
import board.views as bv
import user.views as uv

urlpatterns = [
    path('guestbook/', gv.list),
    path('guestbook/add', gv.add),
    path('guestbook/deleteform', gv.deleteform),
    path('guestbook/delete', gv.delete),

    path('board/', bv.list),
    path('board/writeform', bv.writeform),
    path('board/write', bv.write),
    path('board/delete', bv.delete),
    path('board/view', bv.view),
    path('board/modifyform', bv.modifyform),
    path('board/modify', bv.modify),
    path('board/search', bv.search),

    path('user/joinform', uv.joinform),
    path('user/joinsuccess', uv.joinsuccess),
    path('user/join', uv.join),     # POST로 보내지는 URL에는 맨끝 /를 넣지 않는다.
    path('user/loginform', uv.loginform),
    path('user/login', uv.login),
    path('user/logout', uv.logout),

    path('', mv.index),
    path('admin/', admin.site.urls),
]
