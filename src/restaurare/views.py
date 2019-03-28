from django.shortcuts import render

def restaurare_main(request):
	return render(request,'restaurare.html')

def lemn(request):
	return render(request,'lemn.html')

def piatra(request):
	return render(request,'piatra.html')