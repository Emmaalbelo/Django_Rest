from rest_framework import routers
from .api import ProjectviewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectviewSet,'projects')


urlpatterns = router.urls

