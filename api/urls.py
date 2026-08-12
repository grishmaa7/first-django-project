from rest_framework.routers import DefaultRouter

from api.views import (
    StudentViewSet,
    TeacherViewSet,
    ClassViewSet,
)

router = DefaultRouter()

router.register("students", StudentViewSet, basename="student")
router.register("teachers", TeacherViewSet, basename="teacher")
router.register("classes", ClassViewSet, basename="class")


urlpatterns = router.urls