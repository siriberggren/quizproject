from django.shortcuts import render
from quiz.models import Quiz
from django.shortcuts import redirect

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
    quiz = Quiz.objects.get(quiz_number=quiz_number)
    questions = quiz.questions.all()
    question = questions[int(question_number) - 1]
    islastpage = False,
    num_questions = quiz.questions.count()
    if int(question_number) == num_questions:
        islastpage = True
    context = {
        "question_number": question_number,
        "question": question.question,
        "answer1": question.answer1,
        "answer2": question.answer2,
        "answer3": question.answer3,
        "answer4": question.answer4,
        "answer5": question.answer5,
        "answer6": question.answer6,
        "answer7": question.answer7,
        "answer8": question.answer8,
        "answer9": question.answer9,
        "answer10": question.answer10,
        "answer11": question.answer11,
        "answer12": question.answer12,
        "answer13": question.answer13,
        "answer14": question.answer14,
        "answer15": question.answer15,
        "answer16": question.answer16,
        "answer17": question.answer17,
        "answer18": question.answer18,
        "answer19": question.answer19,
        "answer20": question.answer20,
        "islastpage": islastpage,
        "quiz": quiz,
        "quiz_number": quiz_number,
        "islastpage": islastpage,
    }
    return render(request, "quiz/question.html", context)

def answer(request, quiz_number, question_number):
    saved_answers = request.session.get(quiz_number, {})
    answer = int(request.POST["answer"])
    saved_answers[question_number] = answer
    request.session[quiz_number] = saved_answers

    question_number = int(question_number)
    quiz = Quiz.objects.get(quiz_number=quiz_number)
    num_questions = quiz.questions.count()
    num_correct_answers = 0
    if num_questions <= question_number:
        return redirect("results_page", quiz_number)
    else:
        return redirect("question_page", quiz_number, question_number + 1)

def results(request, quiz_number):
    quiz = Quiz.objects.get(quiz_number=quiz_number)
    questions = quiz.questions.all()
    saved_answers = request.session.get(quiz_number, {})
    num_correct_answers = 0
    for question_number, answer in saved_answers.items():
        correct_answer = questions[int(question_number) - 1].correct
        if correct_answer == answer:
            num_correct_answers += 1
    context = {
        "correct": num_correct_answers,
        "total": questions.count(),
    }
    return render(request, "quiz/results.html", context)