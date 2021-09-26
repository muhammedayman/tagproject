from django.db import router
from rest_framework import routers
from django.urls import path
from .views import TagView, home
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register(r'snippet', TagView, basename='snippet')
urlpatterns=[
  
    path('tag/<int:pk>/',TagView.as_view({"get":"tag"}),name="tag"),
    path('tag/',TagView.as_view({"get":"tag"}),name="tag-list"),
    path('token',TokenObtainPairView.as_view(),name="token"),
    path('refresh',TokenRefreshView.as_view(),name="refresh"),
    path('',home,name="home")
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls