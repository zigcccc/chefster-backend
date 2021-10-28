from rest_framework import routers

from .views import RecipeViewSet

app_name = "recipes"

router = routers.DefaultRouter()

router.register(app_name, RecipeViewSet, basename=app_name)

urlpatterns = router.urls
