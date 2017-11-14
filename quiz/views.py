from django.shortcuts import render
from quiz.models import Quiz
from django.shortcuts import redirect
from django.http import Http404

# Create your views here.


def startpage(request):
    context = {
        'quizzes': Quiz.objects.all(),
    }
    return render(request, 'start.html', context)


def quiz(request, quiz_number):
    try:
        l_quiz = Quiz.objects.get(quiz_number=quiz_number)
    except Quiz.DoesNotExist:
        raise Http404
    if quiz_number > l_quiz.quiz_number:
        raise Http404
    context = {
        'quiz': l_quiz,
        'quiz_number': quiz_number,

    }
    return render(request, 'quiz.html', context)


def question2(request, quiz_number, question_number):
    try:
        l_quiz = Quiz.objects.get(quiz_number=quiz_number)
    except Quiz.DoesNotExist:
        raise Http404
    if question_number > l_quiz.questions2.count():
        raise Http404
    l_questions = l_quiz.questions2.all()
    l_question = l_questions[quiz_number - 1]
    last_question_number = l_questions.count()
    context = {
        'quiz_name': l_quiz.name,
        'question_number': question_number,
        'question': l_question.question,
        'answer1': l_question.answers[0],
        'answer2': l_question.answers[1],
        'answer3': l_question.answers[2],
        'quiz_number': quiz_number,
        'last_question_number': last_question_number,
    }
    return render(request, 'question.html', context)


def question(request, quiz_number, question_number):

    try:
        l_quiz = Quiz.objects.get(quiz_number=quiz_number)
        l_questions = l_quiz.questions.all() if l_quiz.questions.all() else l_quiz.questions2.all()

    except Quiz.DoesNotExist:
        raise Http404
    if question_number > l_questions.count():
        raise Http404

    l_question = l_questions[question_number - 1]
    last_question_number = l_questions.count()

    if l_quiz.questions.all():
        l_answer1 = l_question.answer1
        l_answer2 = l_question.answer2
        l_answer3 = l_question.answer3
    else:
        l_answers = l_question.answers.all()
        l_answer1 = l_answers[0]
        l_answer2 = l_answers[1]
        l_answer3 = l_answers[2]

    context = {
        'quiz_name': l_quiz.name,
        'question_number': question_number,
        'question': l_question.question,
        'answer1': l_answer1,
        'answer2': l_answer2,
        'answer3': l_answer3,
        'quiz_number': quiz_number,
        'last_question_number': last_question_number,
    }
    return render(request, 'question.html', context)


def completed(request, quiz_number):
    l_quiz = Quiz.objects.get(quiz_number=quiz_number)
    l_questions = list(l_quiz.questions.all())
    saved_answers = request.session.get(str(quiz_number), {})

    num_correct_answers = 0
    for question_number, l_answer in saved_answers.items():
        correct_answer = l_questions[int(question_number) - 1].correct
        if correct_answer == l_answer:
            num_correct_answers += 1
    num_questions = l_quiz.questions.count()
    context = {
        "correct": num_correct_answers,
        "total": num_questions,
        "quiz_number": quiz_number,
        'quiz_name': l_quiz.name,
    }
    return render(request, 'results.html', context)


def answer(request, quiz_number, question_number):
    l_answer = request.POST['answer']
    saved_answers = request.session.get(str(quiz_number), {})
    saved_answers[question_number] = int(l_answer)
    request.session[quiz_number] = saved_answers

    l_quiz = Quiz.objects.get(quiz_number=quiz_number)
    num_questions = l_quiz.questions.count()
    if num_questions <= question_number:
        return redirect('result_page', quiz_number)

    return redirect('question_page', quiz_number, question_number + 1)

