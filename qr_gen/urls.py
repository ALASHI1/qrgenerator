from django.urls import path
from .views import qrgen,imageRender,qrDisplay,pdfRender,audioRender,geoCode,contactcard,dashboard,qrpdfDisplay,qraudioDisplay,content
qrpdfDisplay
urlpatterns = [
    path ('',qrgen, name='qrgen'),
    path ('imageRender',imageRender, name='image'),
    path ('pdf',pdfRender, name='pdf'),
    path ('audio',audioRender, name='audio'),
    path ('geoCode',geoCode, name='geoCode'),
    path ('contactcard',contactcard, name='contactcard'),
    path ('dashboard',dashboard, name='dashboard'),
    path ('index1/<slug:slug>',qrDisplay, name='qrDisplay'),
    path ('index2/<slug:slug>',qraudioDisplay, name='qraudioDisplay'),
    path ('index3/<slug:slug>',qrpdfDisplay, name='qrpdfDisplay'),
    path ('content',content, name='content'),

]
