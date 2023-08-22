from django_filters import rest_framework as filters
from server.apps.users.models import User


class UsersFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ["is_active", "roles"]
