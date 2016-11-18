from django.shortcuts import render, redirect
from . import models
from .models import Users, Books, Authors, Reviews
import bcrypt
from django.contrib import messages



# Create your views here.


#### ALL THE HTML PAGES
def index(request):
	return render(request, 'book_review/index.html')


def home(request):
	thisuser = models.Users.objects.get(id = request.session['user_id'])

	allthebooks = models.Reviews.objects.order_by('-id')
	context={
		'thisuser' : thisuser,
		'reviews' : allthebooks
	}

	return render(request, 'book_review/home.html', context)


def addbook(request):


	return render(request, 'book_review/addbook.html')


def displaybook(request, id):
	if models.Books.objects.filter(id=id):
		thisbook = models.Books.objects.get(id=id)
		reviews = models.Reviews.objects.filter(book=thisbook)
		context={
			'thisbook' : thisbook,
			'reviews' : reviews
		}
		return render(request, 'book_review/displaybook.html', context)
	else:
		redirect('/home')

def userprofile(request, id):
	if models.Users.objects.filter(id=id):
		thisuser = models.Users.objects.get(id=id)
		reviews = models.Reviews.objects.filter(commenter=thisuser)

		context={
			"thisuser" : thisuser,
			"reviews" : reviews,
			'total' : len(reviews)
		}

		return render(request, 'book_review/profile.html', context)
	else:
		redirect('/home')


####ALL THE PROCESSING

def login(request):
	email=request.POST.get('email')
	password=request.POST.get('password')
	
	#check if existing user or input error
	existuser = models.Users.objects.loginvalid(request,email, password)
	if existuser == True:
		user_id = models.Users.objects.get(email = email).id
		request.session['user_id'] = user_id
		context = {
			'username' : email,
			'status' : "logged in"
		}
		return redirect('/home')
	##DISPLAY MSGED TO SHOW ERROR
	messages.error(request, existuser)
	return redirect('/')

def register(request):
	#GET USER INPUT
	first_name=request.POST.get('first_name')
	last_name=request.POST.get('last_name')
	email=request.POST.get('email')
	alias=request.POST.get('alias')
	password=request.POST.get('password')
	repassword=request.POST.get('re_password')
	newuser = models.Users.objects.registervalid(first_name, last_name, alias, email, password, repassword)

	if not newuser:
		hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
		newuser = models.Users.objects.create(first_name=first_name, last_name=last_name, alias=alias, email=email, hashedpw=hashed)
		user_id = models.Users.objects.get(email = email).id
		request.session['user_id'] = user_id
		return redirect('/home')

	for ind in range (0, len(newuser)):
		messages.error(request, newuser[ind])
	return redirect('/')


def addbookprocess(request):
	if request.method == "POST":
		print "lets process this added book"
		info = request.POST

		##create an author instance
		if models.Authors.objects.filter(name= info['author']):
			author = models.Authors.objects.get(name= info['author'])
		else:
			author = models.Authors.objects.create(name=info['author'])
		##create the review instance
		print "user id", request.session['user_id']
		thisuser = models.Users.objects.get(id=request.session['user_id'])
		print thisuser, thisuser.first_name
		
		book = models.Books.objects.create(title=info['title'], description=info['description'], author=author, reviewer=thisuser)
		thisuser = models.Users.objects.get(id=request.session['user_id'])
		if info['review']:
			review = models.Reviews.objects.create(content=info['review'], rating=int(info['rating']), book=book, commenter=thisuser)
		else:
			review = NULL

		return redirect('/home')

def addreviewprocess(request):
	if request.method =="POST":
		info = request.POST
		print info['comment']
		if len(info['comment']) > 0:
			thisbook = models.Books.objects.get(id=info['book_id'])
			thisuser = models.Users.objects.get(id=request.session['user_id'])
			review = models.Reviews.objects.create(content=info['comment'], rating=int(info['rating']), book=thisbook, commenter= thisuser)


		return redirect('/display/', info["book_id"])



