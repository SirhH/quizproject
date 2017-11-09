from django.shortcuts import render

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
        'quizzes': quizzes,
    }
    return render(request, 'start.html', context)


def quiz(request, quiz_number):
    context = {
        'quiz': quizzes[quiz_number - 1],
        'quiz_number': quiz_number,
    }
    return render(request, 'quiz.html', context)


def question(request, quiz_number, question_number):
    context = {
        "question_number": question_number,
        "question": "Hur många bultar har ölandsbron?",
        "answer1": "12",
        "answer2": "66400",
        "answer3": "7 428 954",
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
