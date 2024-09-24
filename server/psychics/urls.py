from django.urls import path
from .views import Start, About, Index, Reliability, Finish

urlpatterns = [
    path('', Start.as_view(), name='start'),
    path('about/', About.as_view(), name='about'),
    path('index/', Index.as_view(), name='index'),
    path('reliability/', Reliability.as_view(), name='reliability'),
    path('finish', Finish.as_view(), name='finish')
]