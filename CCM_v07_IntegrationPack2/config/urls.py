
from django.urls import include, path

urlpatterns = [
    path("", include("apps.core.urls")),
    path("members/", include("apps.members.urls")),
    path("reception/", include("apps.reception.urls")),
    path("attendance/", include("apps.attendance.urls")),
    path("pottery/", include("apps.pottery.urls")),
    path("finance/", include("apps.finance.urls")),
]
