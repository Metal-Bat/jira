from datetime import datetime, timedelta

from django.db.models import Prefetch, Q
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from app.common.comment.models import Comment
from app.organization.models import Organization, Task
from app.users import serializer
from app.users.models import User


class UserInfoApi(APIView):

    @swagger_auto_schema(
        responses={
            200: serializer.UserSerializer,
        },
    )
    def get(self, request):
        """
        user information and active tasks and last day until now mentions

        """
        print(request.user)
        assigned_task = Prefetch(
            lookup="assigned_task",
            queryset=Task.objects.filter(
                is_active=True,
                state__in=[
                    Task.TaskState.PEND,
                    Task.TaskState.TO_DEVELOP,
                    Task.TaskState.DEVELOPING,
                ],
            ).order_by("order_id"),
        )
        review_task = Prefetch(
            lookup="review_task",
            queryset=Task.objects.filter(is_active=True).order_by("order_id"),
        )
        organization_owners = Prefetch(
            lookup="organization_owners",
            queryset=Organization.objects.filter(is_active=True),
        )
        organization_managers = Prefetch(
            lookup="organization_managers",
            queryset=Organization.objects.filter(is_active=True),
        )
        organization_developers = Prefetch(
            lookup="organization_developers",
            queryset=Organization.objects.filter(is_active=True),
        )
        yesterday = datetime.today() - timedelta(1)

        mentions = Prefetch(
            lookup="mentions",
            queryset=Comment.objects.filter(
                is_active=True,
            )
            .filter(
                Q(created_at__gte=yesterday) | Q(modified_at__gte=yesterday),
            )
            .order_by(
                "-modified_at",
                "-created_at",
            ),
        )
        user = (
            User.objects.filter(id=request.user.id)
            .prefetch_related(
                assigned_task,
                review_task,
                organization_owners,
                organization_managers,
                organization_developers,
                mentions,
            )
            .last()
        )

        serialized_data = serializer.UserSerializer(user)
        print(request.user)
        return Response(serialized_data.data)

    @swagger_auto_schema(
        request_body=serializer.UserSerializer,
        responses={
            200: serializer.UserSerializer,
        },
    )
    @csrf_exempt
    def put(self, request):
        print(request.user)
        serializer_data = serializer.UserSerializer(request.user, data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)
        return Response(serializer_data.errors)
