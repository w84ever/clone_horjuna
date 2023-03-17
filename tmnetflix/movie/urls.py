from django.urls import path
from .views import MovieList, MovieDetail, MovieCategory, MovieLanguage, MovieSearch, MovieYear, HomeView

app_name = 'movie'

urlpatterns = [
    path('', HomeView.as_view()),
    path('category/<str:category>', MovieCategory.as_view() , name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view() , name='movie_language'),
    path('search/', MovieSearch.as_view() , name='movie_search'),
    path('<slug:slug>', MovieDetail.as_view() , name='movie_detail'),
    path('year/<int:year>', MovieYear.as_view() , name='movie_year'),

    path('', MovieList.as_view(), name='movie_list'),
]