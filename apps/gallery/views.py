from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.gallery.models import Photography
from apps.gallery.forms import PhotographyForms


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')

    photographies = Photography.objects.order_by("photo_date").filter(
        published=True
    )
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

    photographies = Photography.objects.order_by("photo_date").filter(
        published=True
    )

    if "search" in request.GET:
        name_to_search = request.GET["search"]
        if name_to_search:
            photographies = photographies.filter(
                name__icontains=name_to_search
            )

    return render(request, 'gallery/index.html', {"cards": photographies})


def new_image(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = PhotographyForms
    if request.method == 'POST':
        form = PhotographyForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')

    return render(request, 'gallery/new_image.html', {'form': form})


def edit_image(request, photo_id):
    photography = Photography.objects.get(id=photo_id)
    form = PhotographyForms(instance=photography)

    if request.method == 'POST':
        form = PhotographyForms(
            request.POST, request.FILES, instance=photography
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')

    return render(
        request,
        'gallery/edit_image.html',
        {'form': form, 'photo_id': photo_id},
    )


def delete_image(request, photo_id):
    photography = Photography.objects.get(id=photo_id)
    photography.delete()
    messages.success(request, 'Fotografia deletada com sucesso!')
    return redirect('index')


def filter(request, category):
    photographies = Photography.objects.order_by("photo_date").filter(
        published=True, category=category
    )
    return render(request, 'gallery/index.html', {"cards": photographies})
