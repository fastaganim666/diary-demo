from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPurpose.as_view(), name='purpose_main'),
    path('create/', CreatePurpose.as_view(), name='purpose_create'),
    path('<int:pk>/', DetailPurpose.as_view(), name='purpose_detail'),
    path('delete/<int:pk>/', DeletePurpose.as_view(), name='purpose_delete'),
    path('edit/<int:pk>/', EditPurpose.as_view(), name='purpose_edit'),
    path('steps/add/<int:pk>/', CreateStep.as_view(), name='step_add'),
    path('step/delete/<int:pk>/', DeleteStep.as_view(), name='step_delete'),
    path('step/done/<int:pk>/', step_done, name='step_done'),
    path('step/not_done/<int:pk>/', not_step_done, name='not_step_done'),

    path('constraints/add/<int:pk>/', CreateConstraint.as_view(), name='constraint_add'),
    path('constraint/delete/<int:pk>/', DeleteConstraint.as_view(), name='constraint_delete'),
    path('constraint/done/<int:pk>/', constraint_done, name='constraint_done'),
    path('constraint/not_done/<int:pk>/', not_constraint_done, name='not_constraint_done'),

    path('skills/add/<int:pk>/', CreateSkill.as_view(), name='skill_add'),
    path('skill/delete/<int:pk>/', DeleteSkill.as_view(), name='skill_delete'),
    path('skill/done/<int:pk>/', skill_done, name='skill_done'),
    path('skill/not_done/<int:pk>/', not_skill_done, name='not_skill_done'),

    path('question/create/<int:pk>/', CreateQuestion.as_view(), name='question_create'),
    path('question/delete/<int:pk>/', DeleteQuestion.as_view(), name='question_delete'),
    path('question/update/<int:pk>/', EditQuestion.as_view(), name='question_edit'),

    path('comment/delete/<int:pk>/', DeleteComment.as_view(), name='comment_delete'),

]