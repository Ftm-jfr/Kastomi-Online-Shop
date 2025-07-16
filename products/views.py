from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from products.models import Favorite


def home(request):
    return render(request,'../templates/home-page.html')

@login_required
def favorites_view(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('product')
    print(favorites)
    return render(request, 'user-profile.html', {'favorites': favorites})

