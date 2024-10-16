from django.shortcuts import render, redirect, get_object_or_404
from .models import TakoyakiMenu
from .forms import TakoyakiMenuForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q 

def homepage(request):
    return render(request, 'homepage/index.html')


def about(request):
    return render(request, 'homepage/about.html')

# READ Menu
def menu_index(request):
    menus = TakoyakiMenu.objects.all()
    return render(request, 'menu/index.html', {'menus': menus})

# CREATE Menu
def menu_create(request):
    if request.method == 'POST':
        form = TakoyakiMenuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu Takoyaki berhasil dibuat!')
            return redirect('menu_index')
    else:
        form = TakoyakiMenuForm()
    return render(request, 'menu/create.html', {'form': form})

# Update Menu
def menu_update(request, menu_id):
    menu = get_object_or_404(TakoyakiMenu, id=menu_id)
    if request.method == 'POST':
        form = TakoyakiMenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu Takoyaki berhasil diubah!')
            return redirect('menu_index')
    else:
        form = TakoyakiMenuForm(instance=menu)
    return render(request, 'menu/update.html', {'form': form, 'menu': menu})

# Delete Menu
def menu_delete(request, menu_id):
    if request.method == 'POST':
        menu = get_object_or_404(TakoyakiMenu, id=menu_id)
        menu.delete()
        messages.success(request, 'Menu Takoyaki berhasil dihapus!')
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

# Search Menu
def menu_index(request):
    query = request.GET.get('q')
    if query:
        menus = TakoyakiMenu.objects.filter(
            Q(item_name__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        menus = TakoyakiMenu.objects.all()
    return render(request, 'menu/index.html', {'menus': menus, 'query': query})