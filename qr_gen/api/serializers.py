from rest_framework import  serializers
from django.contrib.auth.models import User
from ..models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']



class QrcodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Qrcode
		fields = ["name"]


class ImageRenderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Qrfilecode
		fields = ["name","uploads","author",'slug']

class AudioRenderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Qraudiocode
		fields = ["name","uploads","author",'slug']

class PdfRenderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Qrpdfcode
		fields = ["name","uploads","author",'slug']



class GeoCodeSerializer(serializers.Serializer):
	address = serializers.CharField(label='Your address', max_length=500)

class ContactcardSerializer(serializers.Serializer):
	name = serializers.CharField(label='Your name', max_length=500)
	email = serializers.CharField(label='Your email', max_length=500)
	phone = serializers.CharField(label='Your phone', max_length=500)
	url = serializers.CharField(label='Your website', max_length=500)