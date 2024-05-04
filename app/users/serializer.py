from app.core.base_serializer import BaseSerializer
from app.organization.models import Organization, Task
from app.users.models import User


class UserOrganizations(BaseSerializer):
    class Meta:
        model = Organization
        read_only_fields = [
            "id",
            "is_active",
            "created_at",
            "modified_at",
            "name",
        ]
        fields = [
            "id",
            "is_active",
            "created_at",
            "modified_at",
            "name",
        ]


class UserTaskSerializer(BaseSerializer):
    class Meta:
        model = Task
        read_only_fields = [
            "id",
            "is_active",
            "created_at",
            "modified_at",
            "name",
            "due_date",
            "order_id",
        ]
        extra_kwargs = {
            "state": {"required": False},
        }
        fields = [
            "id",
            "is_active",
            "created_at",
            "modified_at",
            "name",
            "due_date",
            "order_id",
            "state",
        ]


class UserSerializer(BaseSerializer):
    organization_owners = UserOrganizations(many=True, read_only=True)
    organization_managers = UserOrganizations(many=True, read_only=True)
    organization_developers = UserOrganizations(many=True, read_only=True)
    assigned_task = UserTaskSerializer(many=True, read_only=True)
    review_task = UserTaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        read_only_fields = [
            "id",
            "is_active",
            "created_at",
            "modified_at",
            "username",
            "is_staff",
            "is_active",
            "date_joined",
            "organization_owners",
            "organization_managers",
            "organization_developers",
            "mentions",
        ]
        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "current_state": {"required": False},
            "description": {"required": False},
            "mobile": {"required": False},
            "email": {"required": False},
            "assigned_task": {"required": False},
            "review_task": {"required": False},
        }
        fields = [
            "id",
            "is_active",
            "created_at",
            "modified_at",
            "username",
            "is_staff",
            "is_active",
            "date_joined",
            "organization_owners",
            "organization_managers",
            "organization_developers",
            "mentions",
            "first_name",
            "last_name",
            "current_state",
            "description",
            "mobile",
            "email",
            "assigned_task",
            "review_task",
        ]
