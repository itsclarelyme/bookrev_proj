from __future__ import unicode_literals

from django.db import models
import re, bcrypt

# Create your models here.
class UserManager(models.Manager):
	def loginvalid(self, request, email, password):
		print "login valid!"
		print email
		print password
		error = []
		
		if email:
			user = Users.objects.filter(email=email)
			if user:
				user = Users.objects.get(email = email)
				print user.hashedpw
				if bcrypt.hashpw(password.encode('utf-8'), user.hashedpw.encode('utf-8')) == user.hashedpw:
					return True
				else:
					error.append("Password incorrect")
			else:
				error.append("User does not exist")
		else:
			error.append("Please enter an email")
		return error


	def registervalid(self, first, last, alias, email, password, repass):
		print "register valid!"
		error = []

		#Check all field is filled
		if first and last and email and password and repass and alias:
			print "good job everything is filled in"

			if Users.objects.filter(email=email):
				error.append("User already exist! Please login instead!")
				return error

			if re.search(r'^[a-zA-Z]+$', first) == False or len(first)<2:
				print "letter thing:", re.search(r'^[a-zA-Z]+$', first)
				print "length thing:", len(first)
				error.append("First name invalid! Must be at least 8 characters long and consist of only letters")

			if re.search(r'^[a-zA-Z]+$', first) == False or len(first)<2:
				error.append("Last name invalid! Must be at least 8 characters long and consist of only letters")

			if Users.objects.filter(email=email):
				error.append("User already exist! Please login instead!")

			if re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email) == None:
				error.append("Email invalid")

			if len(password) < 8:
				error.append("Password must be longer than 8 character!")

			if repass != password:
				error.append("Password entries do not match")

		else:
			print "dude fill it in"
			error.append("Please fill in all the blanks")

		return error

		
		


class Users(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	alias = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	hashedpw = models.CharField(max_length=225)
	created_at = models.DateTimeField(auto_now_add = True)

	objects = UserManager()

class Books(models.Model):
	title = models.CharField(max_length=45)
	description = models.TextField(max_length=500, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	reviewer = models.ForeignKey('Users', models.DO_NOTHING, related_name="bookreviewer")
	author = models.ForeignKey('Authors', models.DO_NOTHING, related_name="bookauthor", null=True)


class Authors(models.Model):
	name = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
	content = models.CharField(max_length=225)
	rating = models.DecimalField(max_digits=1, decimal_places=0)
	created_at = models.DateTimeField(auto_now_add=True)
	book = models.ForeignKey('Books', models.DO_NOTHING, related_name="commentbook")
	commenter = models.ForeignKey('Users', models.DO_NOTHING, related_name="commentuser")

	






