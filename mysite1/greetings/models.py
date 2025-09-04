from django.db import models

class Doctor(models.Model):
	name = models.CharField(max_length=100)
	specialty = models.CharField(max_length=100)
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.name


class Patient(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	gender = models.CharField(
		max_length=10,
		choices=[('Male', 'Male'), ('Female', 'Female')],
		default='Male'
	)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
