from django.urls import path
from . import views
app_name = 'qr_gen'

urlpatterns = [
	path('geo/',views.Geo_code.as_view(), name='geocode'),
	path('qrcode/',views.Qrcode.as_view(), name='qrcode'),
	path('contact/',views.Contactcard.as_view(), name='contactcard'),
	path('image/',views.ImageRender.as_view(), name='image'),
	path('imageqr/<slug>',views.ImageRenderqr.as_view(), name='imageqr'),
	path('audio/',views.AudioRender.as_view(), name='audio'),
	path('pdf/',views.PdfRender.as_view(), name='pdf'),
]



