from user.views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user',UserViewSet)