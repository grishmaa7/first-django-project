from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("students.urls")),
    path("classes/", include("classes.urls")),
    path("teachers/", include("teacher.urls")),

    # Class 8/9: the API.
    #
    # Two versions of the SAME API run side by side so you can compare them:
    #   /api/apiview/...  -> hand-written APIView    (api/views_apiview.py)
    #   /api/router/...   -> ModelViewSet + router    (api/viewsets.py)
    #   /api/...          -> DRF generic views        (api/views.py)
    #
    # The apiview/ and router/ lines must come FIRST, otherwise those words
    # would be matched as a student id by the /api/ patterns.
   # path("api/apiview/", include("api.urls_apiview")),
    path("api/router/", include("api.urls")),
    #path("api/", include("api.urls")),

    # Class 7: Django's built-in login/logout views.
    # We only had to supply a template for login -- logout needs none.
   # path("login/", auth_views.LoginView.as_view(
      #  template_name="registration/login.html"), name="login"),
   # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]