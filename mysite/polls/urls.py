from django.urls import path
from .views import temp_data
from . import views
app_name = 'polls'

urlpatterns = [
    # path('index/', views.index, name='info'),
    # path('question/', views.question, name='questions'),
    # path('page/', views.page, name="html_page"),
    # path('html/', views.html_render),
    # path('calculate/<int:amount>/<int:months>/<str:rate_of_interest>/', views.interest_amount),
    # path('interest/<int:amount>/<int:months>/<str:rate_of_interest>/', views.simple_interest),
    # path("prav/", temp_data),
    # models
    path("url/", views.index, name="index"),
    path("question/<int:question_id>/choices/", views.choices, name="choices"),

    path("create/question/", views.create_question, name="create-question"),
    path("create/<int:question_id>/choice/", views.create_choice, name="create-choice"),
    path("create/df/question/", views.question_djforms, name='df-create-question'),

    # email
    path("emails/", views.emails, name="all-emails"),  # email listing page
    path("email/create", views.create_email, name="create-email"),
    path("email/<int:pk>/", views.email_detail, name="detail-email"),
]

