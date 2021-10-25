from django.shortcuts import render,get_object_or_404
from . models import *
from .form import *
import io
from io import BytesIO
import segno
from segno import helpers
import PIL
import qrcode
import qrcode.image.svg
from django.core.files.base import ContentFile,File
from geopy.geocoders import GoogleV3
from django.contrib.auth.decorators import login_required
# from PIl import Image, ImageDraw
# Create your views here.


def qrgen(request):
	qrgen = Qrcode.objects.filter(name='name')
	if request.method == 'POST':
		form = Qrform(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			qr = segno.make_qr(name).png_data_uri(scale=10)
			return render(request,'thanks.html',{'form':form,'qr':qr,'name':name})
	else:
		form = Qrform()
	return render(request,'qr.html',{'form':form})


def imageRender(request):
	Q = Qrfilecode.objects.filter(author=request.user)
	Q = Q
	if request.method == 'POST':
		form = Qrfileform(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data['name']
			image = form.cleaned_data['uploads']
			form.save()
			m = Qrfilecode.objects.filter(uploads=image)
		return render(request,'imageRender.html',{'form':form,'name':name,'image':image,'Q':Q})
	else:			
		form = Qrfileform()    
	return render(request, "renderForm.html",{'form':form})

def qrDisplay(request,slug):
	Q = get_object_or_404(Qrfilecode, slug=slug)
	try:
		from urlparse import urlparse
	except ImportError:
		from urllib.parse import urlparse
	frontend_url = request.META.get('HTTP_REFERER')
	url = urlparse(frontend_url)
	print (url)
	print (f"{url.scheme}://{url.netloc}{url.path}1/{slug}")
	k = f"{url.scheme}://{url.netloc}{url.path}1/{slug}"
	qr = segno.make_qr(k).png_data_uri(scale=10)
	return render(request, 'qrDisplay.html',{'Q':Q,'qr':qr})

def qraudioDisplay(request,slug):
	Q = get_object_or_404(Qraudiocode, slug=slug)
	try:
		from urlparse import urlparse
	except ImportError:
		from urllib.parse import urlparse
	frontend_url = request.META.get('HTTP_REFERER')
	url = urlparse(frontend_url)
	print (url)
	print (f"{url.scheme}://{url.netloc}{url.path}1/{slug}")
	k = f"{url.scheme}://{url.netloc}{url.path}1/{slug}"
	qr = segno.make_qr(k).png_data_uri(scale=10)
	return render(request, 'qrDisplay.html',{'Q':Q,'qr':qr})

def qrpdfDisplay(request,slug):
	Q = get_object_or_404(Qrpdfcode, slug=slug)
	try:
		from urlparse import urlparse
	except ImportError:
		from urllib.parse import urlparse
	frontend_url = request.META.get('HTTP_REFERER')
	url = urlparse(frontend_url)
	print (url)
	print (f"{url.scheme}://{url.netloc}{url.path}1/{slug}")
	k = f"{url.scheme}://{url.netloc}{url.path}1/{slug}"
	qr = segno.make_qr(k).png_data_uri(scale=10)
	return render(request, 'qrDisplay.html',{'Q':Q,'qr':qr})

def pdfRender(request):
	Q = Qrpdfcode.objects.filter(author=request.user)
	Q = Q
	if request.method == 'POST':
		form = Qrpdfform(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data['name']
			image = form.cleaned_data['uploads']
			form.save()
			m = Qrfilecode.objects.filter(uploads=image)
		return render(request,'pdfrender.html',{'form':form,'name':name,'image':image,'Q':Q})
	else:
		form = Qrfileform()    
	return render(request, "renderForm.html",{'form':form})


def audioRender(request):
	Q = Qraudiocode.objects.filter(author=request.user)
	Q = Q
	if request.method == 'POST':
		form = Qraudioform(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data['name']
			image = form.cleaned_data['uploads']
			form.save()
			m = Qrfilecode.objects.filter(uploads=image)
		return render(request,'audiorender.html',{'form':form,'name':name,'image':image,'Q':Q})
	else:
		form = Qrfileform()    
	return render(request, "renderForm.html",{'form':form})


def geoCode(request):
	if request.method == 'GET':
		form = Geoform(request.GET)
		if form.is_valid():
			geolocator = GoogleV3(api_key='AIzaSyCLS-HC02aGxuQ5ehulKf03bqEYt11iAU4')
			address = form.cleaned_data['address']
			location = geolocator.geocode(address)
			print((location.latitude))
			print((location.longitude))
			qr = helpers.make_geo(location.latitude,location.longitude).png_data_uri(scale=10)
			return render(request, "geoRender.html",{'qr':qr})
		else:
			form = Geoform()
	return render(request, "geoRenderform.html",{'form':form})


def contactcard(request):
	if request.method == 'GET':
		form = ContactCard(request.GET)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']
			url = form.cleaned_data['url']
			qr = helpers.make_mecard(name=name,email=email,phone=phone,url=url).png_data_uri(scale=10)
			return render(request, "contactRender.html",{'qr':qr})

		else:
			form = ContactCard()
	return render(request,'contactRenderform.html',{'form':form})


@login_required
def dashboard(request):
	logged_in_user = request.user
	print(logged_in_user)
	return render(request,'dashboard.html',{})

def content(request):
	Q = Qrfilecode.objects.filter(author=request.user)
	R = Qraudiocode.objects.filter(author=request.user)
	S = Qrpdfcode.objects.filter(author=request.user)
	return render(request, 'content.html',{'Q':Q, 'R':R, 'S':S})

