from rest_framework import generics
from .models import NewPolicy
from .serializers import NewPolicySerializer
from .permissions import IsAuthorOrReadOnly
from django_filters import rest_framework as filters
# Create your views here.


## filter here
class NewPolicyFilter(filters.FilterSet):
    Title = filters.CharFilter(field_name='Title',  lookup_expr='icontains')
    class Meta:
        model = NewPolicy
        fields =['Title']


class NewPolicyListView(generics.ListAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=NewPolicy.objects.all()
    serializer_class= NewPolicySerializer
    filter_backends=(filters.DjangoFilterBackend,)
    filterset_class=NewPolicyFilter

class NewPolicyDetailView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    permission_classes= (IsAuthorOrReadOnly, )
    queryset=NewPolicy.objects.all()
    serializer_class=NewPolicySerializer
