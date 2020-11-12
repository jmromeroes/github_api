from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('github/public/', include('public_github_scrapper.urls'))
    path('admin/', admin.site.urls)
]
