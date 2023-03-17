from .models import Banner


def slider_movies(request):
    # banners = Banner.objects.all().order_by('created')[0:3]
    movies = Banner.objects.last()
    return {'slider_banner' : movies}