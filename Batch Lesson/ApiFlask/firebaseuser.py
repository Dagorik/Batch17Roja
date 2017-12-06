import pyrebase
import random

class FirebaseUser():
	firebase = ""
	def __init__(self):
		config = {
		  "apiKey": "AIzaSyAAuCtEPR77fg9z8w4Ed0iRexU_uqQ8unA",
		  "authDomain": "batch15android.firebaseapp.com",
		  "databaseURL": "https://batch15android.firebaseio.com",
		  "storageBucket": "batch15android.appspot.com"
		}

		firebase = pyrebase.initialize_app(config)

		self.firebase = firebase

	def createUser(self,data):
		db = self.firebase.database()
		id_user = random.randint(0, 9)
		db.child("user").child(id_user).set(data)
		return db.child("user").child(id_user).get().val()

	def getallusers(self):
		db = self.firebase.database()
		return db.child("users").get().val()
