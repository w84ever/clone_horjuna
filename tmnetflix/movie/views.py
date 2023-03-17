from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView, YearArchiveView
from .models import Movie, MainBanner, Banner


class HomeView(ListView):
    model = Movie
    template_name = 'movie/home.html'

    def get_context_data(self , **kwargs):
        context = super(HomeView , self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_watched'] = Movie.objects.filter(status='MW')
        context['recently_added'] = Movie.objects.filter(status='RA') 
        context['slider_banner'] = Banner.objects.all()
        context['first_banner'] = MainBanner.objects.first()
        return context
    

class MovieList(ListView):
    model = Movie
    paginate_by = 2

class MovieDetail(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetail , self).get_object()
        object.views_count += 1
        object.save()
        return object

    def get_context_data(self , **kwargs):
        context = super(MovieDetail , self).get_context_data(**kwargs)
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category)#.order_by['created'][0:6]
        return context


class MovieCategory(ListView):
    model = Movie
    paginate_by = 2

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)

    def get_context_data(self , **kwargs):
        context = super(MovieCategory , self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context



class MovieLanguage(ListView):
    model = Movie
    paginate_by = 2

    def get_queryset(self):
        self.language = self.kwargs['lang']
        return Movie.objects.filter(language=self.language)

    def get_context_data(self , **kwargs):
        context = super(MovieLanguage , self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context




class MovieSearch(ListView):
    model = Movie
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        
        else:
            object_list = self.model.objects.none()

        return object_list

class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True

    print(queryset)

