from django.shortcuts import render
from quiz.models import Quiz

def start(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/start.html", context)


def quiz(request, quiz_number):
	context = {
		"quiz": Quiz.objects.get(quiz_number=quiz_number),
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
		"question_number": question_number,
	    "question": "Hur många bultar har ölandsbron?",
		"answer1": "12",
	   	"answer2": "66 400",
	    "answer3": "7 428 954",
	    "quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)

def results(request, quiz_number):
	context = {
	    "correct": 1,
	    "total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/results.html", context)