from rest_framework import generics
from .serializers import *
from ..models import *
from ..views import *
from qr_gen.form import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.sites.shortcuts import get_current_site

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
        qr = helpers.make_geo(location.latitude, location.longitude).png_data_uri(
            scale=10
        )
        res = {"img": qr}
        return Response(res, status=status.HTTP_200_OK)


class Qrcode(generics.GenericAPIView):
    serializer_class = QrcodeSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        qr = segno.make_qr(request.data["name"]).png_data_uri(scale=10)
        res = {"img": qr}
        return Response(res, status=status.HTTP_200_OK)


class Contactcard(generics.GenericAPIView):
    serializer_class = ContactcardSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        name = request.data["name"]
        email = request.data["email"]
        phone = request.data["phone"]
        url = request.data["url"]
        qr = helpers.make_mecard(
            name=name, email=email, phone=phone, url=url
        ).png_data_uri(scale=10)
        res = {"img": qr}
        return Response(res, status=status.HTTP_200_OK)


class ImageRender(generics.GenericAPIView):
    queryset = Qrfilecode.objects.all()
    serializer_class = ImageRenderSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Qrfilecode.objects.filter(author=request.user)
        filesl = ImageRenderSerializer(queryset, many=True)
        return Response(filesl.data, status=status.HTTP_200_OK)

    def post(self, request):
        domain = get_current_site(request).domain
        name = request.data["name"]
        uploads = request.data["uploads"]
        author = request.user
        img = Qrfilecode.objects.get_or_create(
            name=name, uploads=uploads, author=author
        )

        j = f"{domain}/media/{img[0].uploads}"
        print(j)
        qr = segno.make_qr(j).png_data_uri(scale=10)
        return Response(qr, status=status.HTTP_200_OK)


class ImageRenderqr(generics.RetrieveAPIView):
    queryset = Qrfilecode.objects.all()
    serializer_class = ImageRenderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"


class AudioRender(generics.ListCreateAPIView):
    queryset = Qraudiocode.objects.all()
    serializer_class = AudioRenderSerializer
    permission_classes = [IsAuthenticated]


# class PdfRender(generics.ListCreateAPIView):
#     queryset = Qrpdfcode.objects.all()
#     serializer_class = PdfRenderSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


class PdfRender(generics.GenericAPIView):
    serializer_class = PdfRenderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Qrpdfcode.objects.all()

    def get(self, request):
        queryset = Qrpdfcode.objects.filter(author=request.user)
        filesl = PdfRenderSerializer(queryset, many=True)
        return Response(filesl.data, status=status.HTTP_200_OK)

    def post(self, request):
        domain = get_current_site(request).domain
        name = request.data["name"]
        uploads = request.data["uploads"]
        author = request.user
        pdf = Qrpdfcode.objects.get_or_create(name=name, uploads=uploads, author=author)
        print(pdf[0].uploads)
        j = f"{domain}/media/{pdf[0].uploads}"
        qr = segno.make_qr(j).png_data_uri(scale=10)
        return Response(qr, status=status.HTTP_200_OK)


#  serializer_class = ContactcardSerializer

#     def post(self, request):
#         name = request.data["name"]
#         email = request.data["email"]
#         phone = request.data["phone"]
#         url = request.data["url"]
#         qr = helpers.make_mecard(
#             name=name, email=email, phone=phone, url=url
#         ).png_data_uri(scale=10)
#         res = {"img": qr}
#         return Response(res, status=status.HTTP_200_OK)
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
