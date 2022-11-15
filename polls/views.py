from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import loader
from .models import Question


def index(request):
    # return HttpResponse("Hello world! polls#index")

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }

    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # return HttpResponse("Question %s" % question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    return HttpResponse("Results of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("Voting on question %s" % question_id)