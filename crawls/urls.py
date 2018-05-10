# -*- coding: utf-8 -*-
from django.urls import path

from . import views

'''
用這個方法嘗試做一個自己的網址過濾器
class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value
register_converter(converters.FourDigitYearConverter, 'yyyy')
urlpatterns = [
    path('articles/<yyyy:year>/', views.year_archive),
]
'''

app_name = 'crawls'
urlpatterns = [
    path('facebook', views.FanPageView.as_view(), name='facebook_index'),
    path('facebook/add', views.add, name='facebook_add'),
    path('facebook/<int:pk>', views.DetailView.as_view(), name='facebook_detail'),
    path('facebook/<int:fanpage_id>/crawl',
         views.crawl, name='facebook_crawl'),
    path('facebook/<int:fanpage_id>/delete', views.delete_crawled_data,
         name='facebook_delete_crawled_data'),
    path('facebook/<int:fanpage_id>/delete2',
         views.delete_fanpage, name='facebook_delete_fanpage'),
    path('ptt', views.BoardView.as_view(), name='ptt_index'),
    #path('ptt/<int:pk>', views.PTTDetailView.as_view(), name='ptt_detail'),
    path('ptt/<int:board_id>', views.show_article, name='ptt_detail'),
    path('ptt/<int:board_id>/crawl', views.crawl_ptt_data, name='ptt_crawl'),
    path('ptt/<int:board_id>/delete', views.delete_ptt_data,
         name='ptt_delete_crawled_data'),
    path('ptt/<int:board_id>/delete2',
         views.delete_board, name='ptt_delete_board'),
    path('ptt/add', views.add_ptt_board, name='ptt_add'),
]
