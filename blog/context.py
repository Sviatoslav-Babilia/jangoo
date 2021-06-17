from .models import Headliner


def headliners(request):
    return {
       'headliners': Headliner.objects.all()
    }