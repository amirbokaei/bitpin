from django.urls import path
from .views import ContentListView, RateCreateView, RateUpdateView

urlpatterns = [
    path('list/', ContentListView.as_view()),
    path('rate/', RateCreateView.as_view()),
    path('rate-update/', RateUpdateView.as_view()),

]
