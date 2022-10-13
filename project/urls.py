"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required
from sales.views import home, orders
from loginAndRegister.views import signUp
from admins.views import admins
from documents.views import myDocuments
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", LoginView.as_view(template_name="signIn.html"), name="signIn"),
    path("accounts/logout/", logout_then_login, name="logout"),
    path("register/", signUp, name="signUp"),
    path("", login_required(home), name="home"),
    path("history/", login_required(orders), name="history"),
    path("admins/", login_required(admins), name="admins"),
    path('myDocuments/', login_required(myDocuments), name="myDocuments"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
