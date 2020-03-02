from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from accounts.models import Profile
from api.serializers import ProfileSerializer

class ProfileList(ListCreateAPIView):
        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer



