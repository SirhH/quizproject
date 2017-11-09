from django.shortcuts import render
from quiz.models import Quiz
from django.shortcuts import redirect

# Create your views here.
quizzes = [
    {
        'quiz_number': 1,
        'name': 'Let me guess your favourite color',
        'description': 'Jag tror att jag vet vilken färg du gillar'
    },
    {
        'quiz_number': 2,
        'name': 'Are you in a good mood?',
        'description': 'See if you are having a good day'
    },
    {
        'quiz_number': 3,
        'name': 'Guess my card',
        'description': 'I am thinking of a card, can you find out?'
    },
    {
        'quiz_number': 4,
        'name': 'Let me guess your card',
        'description': 'Can I guess what card you are thinking of?'
    },
]


def startpage(request):
    context = {
        'quizzes': Quiz.objects.all(),
    }
    return render(request, 'start.html', context)


def quiz(request, quiz_number):
    context = {
        'quiz': Quiz.objects.get(quiz_number=quiz_number),
        'quiz_number': quiz_number,
    }
    return render(request, 'quiz.html', context)


def question(request, quiz_number, question_number):
    l_quiz = Quiz.objects.get(quiz_number=quiz_number)
    l_questions = l_quiz.questions.all()
    l_question = l_questions[question_number - 1]

    context = {
        "question_number": question_number,
        "question": l_question.question,
        "answer1": l_question.answer1,
        "answer2": l_question.answer2,
        "answer3": l_question.answer3,
        "quiz_number": quiz_number,
    }
    return render(request, 'question.html', context)


def completed(request, quiz_number):
    context = {
        "correct": 12,
        "total": 20,
        "quiz_number": quiz_number,
    }
    return render(request, 'results.html', context)


def answer(request, quiz_number, question_number):
    l_answer = request.POST['answer']
    saved_answers = request.session.get(str(quiz_number), {})
    saved_answers[question_number] = int(l_answer)
    request.session[question_number] = saved_answers
    return redirect('question_page', quiz_number, question_number + 1 )

