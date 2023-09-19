# Django Imports
from django.http import (
    HttpResponse,
    HttpResponseRedirect
)
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import (
    render,
    get_object_or_404
)

# Local App Imports
from .models import (
    Question,
    Choice,
    Email
)
from .forms import (
    QuestionForm,
    EmailForm
)

def index(request):
    return HttpResponse("You're at index page")


def page(request):
    return HttpResponse("Hello World!")


def question(request):
    return HttpResponse("How are you?")


def html_render(request):
    return render(request, "polls/my_page.html")


def interest_amount(request, amount, months, rate_of_interest):
    total = amount + (amount + months + float(rate_of_interest)) / 100
    return HttpResponse(f"Principle amount: {amount}, Time: {months},"
                        f"Rate of Interest: {rate_of_interest}, Total amount: {total}")


def simple_interest(request, amount, months, rate_of_interest):
    total = amount + (amount + months + float(rate_of_interest)) / 100
    data = {
        "Aadhar": "123456789012",
        "name": "Praveen",
        "p": amount,
        "m": months,
        "r": rate_of_interest,
        "t": total
    }
    return render(request, "polls/simple_interest.html", context=data)

def temp_data(request):
    data = {
        "my_list": ['praveen', 'kumar', ('python', 'django', 'sql'), 'bangalore'],
        "name": 'HCL India pvt. ltd',
        "my_dict":{
            "status": 'active',
            'fname': 'praveen',
            'lname': 'kumar',
            'location': 'bangalore',
            'skills': ['python', 'django', 'sql'],
        },
        'salary': (100000, 120000, 150000, 160000, 145000)
    }

    return render(request, 'my_page.html', {'mydata': data})

def index(request):
    question = Question.objects.all()
    return render(request, "polls/index.html", context={"que": question})

def choices(request, question_id):
    question = Question.objects.get(id=question_id)
    cho = Choice.objects.filter(question=question)
    return render(request, template_name="polls/choices.html",
                  context={'question': question, 'choices': cho})

def create_question(request):
    # import ipdb;ipdb.set_trace()
    if request.method == "POST":
        question = Question.objects.create(
            question_text = request.POST["question"],
            pub_date = timezone.now()
        )
        return HttpResponseRedirect(reverse("polls:questions", args=tuple()))
    else:
        return render(request, template_name="polls/create_question.html")

def create_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        choice = Choice.objects.create(
            question=question,
            choice_text=request.POST["choice"],
            votes=request.POST["votes"]
        )
        return HttpResponseRedirect(reverse("polls:choices", args=(question.pk,)))
    else:
        return render(
            request,
            template_name="polls/create_choice.html",
            context={"question": question})

def question_djforms(request):
    if request.method == "POST":
        form = QuesionForm(request.POST)
        if form.is_valid():
            question = Question.objects.create(
                question_text = form.cleaned_data.get('question'),
                pub_date = timezone.now()
            )
            return HttpResponseRedirect(reverse("polls:question", args=tuple()))
        else:
            return render(request, template_name='polls/df_create_question.html', context={'form': form})
    else:
        return render(request, template_name='polls/df_create_question.html', context={'form': form})

def question_djforms(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question.objects.create(
                question_text=form.cleaned_data.get("question_text"),
                pub_date=timezone.now()
            )
            return HttpResponseRedirect(reverse("polls:index", args=tuple()))
        else:
            return render(request, template_name="polls/df_create_question.html", context={"form": form})
    else:
        form = QuestionForm()
        return render(request, template_name="polls/df_create_question.html", context={"form": form})


# def mail_djforms(request):
#     from .models import MailForm
#     from django.http import HttpResponseRedirect
#     from django.urls import reverse
#
#
#
#     if request.method == 'POST':



"""
from .models import Question
from django.utils import timezone
question = Question.objects.create(question_text="how are you?", pub_data=timezone.now())

from .models import Choice
Choice.objects.create(question=question, choice_text="good") """


def emails(request):
    emails = Email.objects.all()
    return render(request, template_name="email/emails.html", context={"emails": emails})


def create_email(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            # import pdb; pdb.set_trace()
            e = form.save(commit=False)
            return HttpResponseRedirect(reverse("polls:all-emails", args=tuple()))
        else:
            return render(request, template_name="email/create.html", context={"form": form})
    else:
        form = EmailForm()
        return render(request, template_name="email/create.html", context={"form": form})

def email_detail(request, pk):
    email = get_object_or_404(Email, pk=pk)
    return render(request, template_name="email/detail.html", context={"email": email})