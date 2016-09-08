from django.shortcuts import render

# Create your views here.
def start(request):
	return render(request, "quiz/start.html")

def quiz(request):
	return render(request, "quiz/quiz.html")

def question(request):
	return render(request, "quiz/question.html")

def results(request):
	return render(request, "quiz/results.html")