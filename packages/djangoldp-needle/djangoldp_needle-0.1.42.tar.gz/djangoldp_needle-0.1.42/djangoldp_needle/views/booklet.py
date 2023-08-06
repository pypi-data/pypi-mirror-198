from djangoldp.views import LDPViewSet

from django.db.models import Q

class BookletViewset(LDPViewSet):
    def perform_create(self, serializer, **kwargs):
        booklet = super().perform_create(serializer, **kwargs)
        booklet.owners.add(self.request.user)

        return booklet

    def get_queryset(self, *args, **kwargs):
        from ..models import Booklet

        if self.request.user.is_anonymous:
            return []

        user = self.request.user
        return Booklet.objects.filter(Q(owners__in=[user]) | Q(contributors__in=[user]))
