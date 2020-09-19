from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
	# {} is a context dictionary. Front end to backend
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		#Do stuff
		#Find this under form
		message_name = request.POST['message-name']
		message_email= request.POST['message-email']
		message = request.POST['message']

		# Send email
		send_mail(
			message_name, #subject
			message, #message
			message_email, # from email;
			['richiechia@gmail.com'], # to email
			fail_silently= False,
			)


		return render(request, 'contact.html', {'message_name' : message_name})

	else:
		# Return the page
		return render(request, 'contact.html', {})