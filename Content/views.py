from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from .models import Rate
from .models import Content
from .serializers import ContentSerializer, RateSerializer
from rest_framework import permissions


class ContentListView(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (permissions.AllowAny,)

    # @property
    # def user_score(self):
    #     return Rate.objects.filter(content=self.get_object(), user=self.request.user).values_list('score', flat=True)[
    #                0] or None
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = ContentSerializer(queryset, many=True)
    #     response_list = serializer.data
    #     response_list.append({'user_score': self.user_score})
    #     return Response(response_list)


class RateCreateView(CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = RateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class RateUpdateView(UpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = RateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "successful"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
