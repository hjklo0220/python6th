import logging

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from polls.models import Question, Choice

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')
    context = {'latest_question_list': latest_question_list,
               "value": "Hello \nword",
               "value2": "동해물과 백두산이 마으로 닳도록 하느님이 보우하사 우리 나라 만세",
               "value3": ['1', '2', '3'],
               "value4": False,
               "value5": "<strong>Hello world</strong>",
               }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    logger.debug('debug')
    logger.info('info')
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})