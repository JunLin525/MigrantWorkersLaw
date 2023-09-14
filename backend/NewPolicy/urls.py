from django.urls import path
from .views import NewPolicyDetailView,NewPolicyListView
urlpatterns=[
    path('list', NewPolicyListView.as_view(), name="PolicyList" ),
]