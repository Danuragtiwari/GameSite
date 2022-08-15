# from django.contrib import admin
from django.urls import path,include
# from .views import *
from .views import sudoku, rank, changeRankType, saveQuestion, loginUser
app_name="home"
urlpatterns = [
    path('',sudoku),
    path('sudoku/',sudoku),
    path('sudoku/loginUser/',loginUser),
    path('sudoku/rank/', rank),
    path('changeRankType/', changeRankType),
    path('sudoku/saveQuestion/', saveQuestion)
]