from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.gallery.models import Photography


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')

    photographies = Photography.objects.order_by("photo_date").filter(published=True)
    return render(request, 'gallery/index.html', {"cards": photographies})


def image(request, photo_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')

    photography = get_object_or_404(Photography, pk=photo_id)
    return render(request, 'gallery/image.html', {"photography": photography})


def search(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')

    photographies = Photography.objects.order_by("photo_date").filter(published=True)

    if "search" in request.GET:
        name_to_search = request.GET["search"]
        if name_to_search:
            photographies = photographies.filter(name__icontains=name_to_search)

    return render(request, 'gallery/search.html', {"cards": photographies})