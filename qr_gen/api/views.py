from rest_framework import generics
from .serializers import *
from ..models import *
from ..views import *
from qr_gen.form import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

class Geo_code(generics.GenericAPIView):
	serializer_class = GeoCodeSerializer
	def post(self, request):
		geolocator = GoogleV3(api_key=env("GOOGLEAPI"))
		address = request.data["address"]
		location = geolocator.geocode(address)
		qr = helpers.make_geo(location.latitude,location.longitude).png_data_uri(scale=10)
		res = {'img':qr}
		return Response(res,status=status.HTTP_200_OK)

class Qrcode(generics.GenericAPIView):
	serializer_class = QrcodeSerializer
	def post(self, request):
		qr = segno.make_qr(request.data["name"]).png_data_uri(scale=10)
		res = {'img':qr}
		return Response(res,status=status.HTTP_200_OK)

class Contactcard(generics.GenericAPIView):
	serializer_class = ContactcardSerializer
	def post(self,request):
		name = request.data['name']
		email = request.data['email']
		phone = request.data['phone']
		url = request.data['url']
		qr = helpers.make_mecard(name=name,email=email,phone=phone,url=url).png_data_uri(scale=10)
		res = {'img':qr}
		return Response(res,status=status.HTTP_200_OK)

class ImageRender(generics.ListCreateAPIView):
	queryset = Qrfilecode.objects.all()
	serializer_class = ImageRenderSerializer
	permission_classes = [IsAuthenticated]
	
	

class ImageRenderqr(generics.RetrieveAPIView):
	queryset = Qrfilecode.objects.all()
	serializer_class = ImageRenderSerializer
	permission_classes = [IsAuthenticated]
	lookup_field = 'slug'


class AudioRender(generics.ListCreateAPIView):
	queryset = Qraudiocode.objects.all()
	serializer_class = AudioRenderSerializer
	permission_classes = [IsAuthenticated]

class PdfRender(generics.ListCreateAPIView):
	queryset = Qrpdfcode.objects.all()
	serializer_class = PdfRenderSerializer
	permission_classes = [IsAuthenticated]
	





# def post(self,request):
# 		Q = get_object_or_404(Qrfilecode,slug='slug')
# 		queryset = Qrfilecode.objects.all()
# 		try:
# 			from urlparse import urlparse
# 		except ImportError:
# 			from urllib.parse import urlparse
# 		frontend_url = request.META.get('HTTP_REFERER')
# 		url = urlparse(frontend_url)
# 		k = f"{url.scheme}://{url.netloc}{url.path}1/{slug}"
# 		qr = segno.make_qr(k).png_data_uri(scale=10)
# 		res = {'img':qr}
# 		return Response(res,status=status.HTTP_200_OK)






