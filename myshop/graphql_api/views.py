"""Custom GraphQL view enforcing staff-only access to analytics queries."""

from __future__ import annotations

from django.http import HttpRequest, HttpResponse, JsonResponse
from graphene_django.views import GraphQLView


class StaffGraphQLView(GraphQLView):
    """Allow only authenticated staff users to access the GraphQL analytics endpoint."""

    def dispatch(self, request: HttpRequest, *args: object, **kwargs: object) -> HttpResponse:
        if not request.user.is_authenticated or not request.user.is_staff:
            return JsonResponse(
                {"errors": [{"message": "Staff authentication is required for analytics access."}]},
                status=403,
            )
        return super().dispatch(request, *args, **kwargs)
