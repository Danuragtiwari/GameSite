# from django.contrib import admin
from django.urls import path,include
from .views import *
from .views import sudoku, rank, changeRankType, saveQuestion, loginUser
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('sudoku/', sudoku),
    path('sudoku/loginUser/', loginUser),
    path('sudoku/rank/', rank),
    path('changeRankType/', changeRankType),
    path('sudoku/saveQuestion/', saveQuestion)
]