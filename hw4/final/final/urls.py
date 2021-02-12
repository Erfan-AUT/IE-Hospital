from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from doctor.views import *
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

from doctor.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView


router = routers.DefaultRouter()
# router.register(r'doctor', DoctorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('doctor/', DoctorViewSet.as_view(), name='doctor'),
    path('patient/', PatientViewSet.as_view(), name='patient'),
    path('comment/', CommentViewSet.as_view(), name='comment'),
    path('spec/', SpecViewSet.as_view(), name='spec'),

    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
