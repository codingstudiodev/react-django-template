from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet as Generic


class GenericViewSet(Generic):
    model = None
    filterset_class = None
    filterset_fields = []
    search_fields = []
    serializers = {}

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])

    def get_queryset(self):
        return self.model.objects.all().order_by("-pk")

    def get_object(self, pk) -> model:
        return get_object_or_404(self.model, pk=pk)

    def get_context_data(self, **kwars):
        context = super().get_context_data(**kwars)
        context["filter"] = self.filterset_class(
            self.request.GET,
            queryset=self.get_queryset(),
        )
        return context
