from django.urls import include, path

urlpatterns = [
    path("user/", include('src.apps.user.urls'))
]
