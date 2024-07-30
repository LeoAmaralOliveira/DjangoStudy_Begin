from django.shortcuts import render, get_object_or_404
from gallery.models import Photography


def index(request):
    photographies = Photography.objects.order_by("photo_date").filter(published=True)
    return render(request, 'gallery/index.html', {"cards": photographies})


def image(request, photo_id):
    photography = get_object_or_404(Photography, pk=photo_id)
    return render(request, 'gallery/image.html', {"photography": photography})
