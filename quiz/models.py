from django.db import models

class Quiz(models.Model):
	quiz_number = models.PositiveIntegerField()
	name = models.CharField(max_length=100)
	description = models.TextField()
	def __str__(self):
		return self.name

class Question(models.Model):
	question = models.TextField()
	answer1 = models.CharField(max_length=100)
	answer2 = models.CharField(max_length=100)
	answer3 = models.CharField(max_length=100)
	answer4 = models.CharField(max_length=100)
	answer5 = models.CharField(max_length=100)
	answer6 = models.CharField(max_length=100)
	answer7 = models.CharField(max_length=100)
	answer8 = models.CharField(max_length=100)
	answer9 = models.CharField(max_length=100)
	answer10 = models.CharField(max_length=100)
	answer11 = models.CharField(max_length=100)
	answer12 = models.CharField(max_length=100)
	answer13 = models.CharField(max_length=100)
	answer14 = models.CharField(max_length=100)
	answer15 = models.CharField(max_length=100)
	answer16 = models.CharField(max_length=100)
	answer17 = models.CharField(max_length=100)
	answer18 = models.CharField(max_length=100)
	answer19 = models.CharField(max_length=100)
	answer20 = models.CharField(max_length=100)
	correct = models.PositiveIntegerField()
	quiz = models.ForeignKey(Quiz, related_name="questions")
	def __str__(self):
		return self.quiz.name + " / " + self.question

