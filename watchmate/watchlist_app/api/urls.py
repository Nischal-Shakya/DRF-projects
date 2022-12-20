from django.urls import path, include
# from watchlist_app.api.views import movie_list,movie_details
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (WatchListAV,WatchDetailsAV,StreamPlatformAV,
                                     StreamDetailsAV, ReviewList,ReviewDetail,StreamPlatformVS,ReviewCreate)


router = DefaultRouter()
router.register('stream',StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name = 'movie_list'),
    path('<int:pk>/', WatchDetailsAV.as_view(), name = 'movie_details'),
    
    # path('stream/', StreamPlatformAV.as_view(), name = 'stream'),
    # path('stream/<int:pk>/', StreamDetailsAV.as_view(), name = 'stream_details'),
    
    path('',include(router.urls)),
    
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(),name = 'review_create'),
    path('stream/<int:pk>/review/', ReviewList.as_view(),name = 'review_list'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(),name = 'review_detail'),
]