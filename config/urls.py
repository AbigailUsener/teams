from django.contrib import admin
from django.urls import path
from app.views import info
from app.views import team_

urlpatterns = [
    path("admin/", admin.site.urls),
    path("<thing>", info, name="info"),
    path("", team_, name="team_"),
]
