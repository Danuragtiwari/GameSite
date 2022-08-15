import random
from builtins import range, locals, int, str

from django.shortcuts import render, redirect, HttpResponse

import numpy as np
from main.models import Sudoku, User


# Create your views here.
def sudoku(request):
    try:
        userName = request.session['user']
        print(userName)
    except:
        userName = ""

    loop = range(0, 9)
    randomID = random.randint(1, 100000)
    sudoku = Sudoku.objects.get(id=randomID)
    question = sudoku.question
    solution = sudoku.solution
    questionArray = [[0] * 9 for i in range(0, 9)]
    solutionArray = [[0] * 9 for i in range(0, 9)]
    for x in range(0, 9):
        for y in range(0, 9):
            questionArray[x][y] = int(question[x * 9 + y])
            solutionArray[x][y] = int(solution[x * 9 + y])

    return render(request, 'sudoku.html', locals())

def loginUser(request):
    userName = request.GET.get('userName', '')
    request.session['user'] = userName

    return HttpResponse("login success")

def rank(request):
    userName = request.GET.get('userName', '')
    score = request.GET.get('score', '')
    score = int(score)

    top10User = None
    if User.objects.count() < 10:
        top10User = User.objects.order_by('bestScore')
    else:
        top10User = User.objects.order_by('bestScore')[:10]

    if score == 0:
        return render(request, 'rank.html', locals())

    userList = User.objects.all()

    if not userList.filter(username=userName).exists():
        newUser = User.objects.create(username=userName, bestScore=0, solvedQuestion=0)
        newUser.save()

    user = User.objects.get(username=userName)
    scoreStr = str(score//60) + "分" + str(score%60) + "秒"
    if user.bestScore == 0 or score < user.bestScore:
        user.bestScore = score
        user.bestTime = scoreStr

    user.solvedQuestion += 1
    user.save()

    context = {
        'userName': userName,
        'scoreStr': scoreStr,
        'top10User': top10User
    }

    return render(request, 'rank.html', locals())


def changeRankType(request):
    userName = request.session['user']
    sortType = request.GET.get('sortType', '')

    if sortType == 'speed':
        top10User = User.objects.order_by('bestScore')[:10]
    else:
        top10User = User.objects.order_by('-solvedQuestion')[:10]

    context = {
        'userName': userName,
        'top10User': top10User
    }

    return render(request, 'rankTable.html', context)

def saveQuestion(request):

    try:
        test_valid = Sudoku.objects.get(id=1)
    except:
        test_valid = None
    
    if test_valid:
        print("Data already exists")

        return redirect("/sudoku/")

    quizzes = np.load('main/sudoku_quizzes.npy')  # shape = (1000000, 9, 9)
    solutions = np.load('main/sudoku_solutions.npy')  # shape = (1000000, 9, 9)

    for x in range(0, 100000, 1):
        tmp = ""
        tmp2 = ""
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                tmp = tmp + str(quizzes[x][i][j])
                tmp2 = tmp2 + str(solutions[x][i][j])
        sudoku = Sudoku(question=tmp, solution=tmp2)
        sudoku.save()
        print("save number:" + str(x))

    print("Complete save data")

    return redirect("/sudoku/")