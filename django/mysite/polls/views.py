from django import template
from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views import generic

from .models import Question, Choice

# Create your views here.
"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # 也有 get_list_or_404() 函数，工作原理和 get_object_or_404() 一样，
    # 除了 get() 函数被换成了 filter() 函数。如果列表为空的话会抛出 Http404 异常。

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choice.votes += 1
        selected_choice.votes = F('votes') + 1
        # 我们的 vote() 视图代码有一个小问题。代码首先从数据库中获取了 selected_choice 对象，
        # 接着计算 vote 的新值，最后把值存回数据库。如果网站有两个方可同时投票在 同一时间 ，
        # 可能会导致问题。同样的值，42，会被 votes 返回。然后，对于两个用户，新值43计算完毕，
        # 并被保存，但是期望值是44。这个问题被称为 竞争条件 。
        # 如果你对此有兴趣，你可以阅读 使用 F() 避免竞争条件 来学习如何解决这个问题。
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
"""

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choice.votes += 1
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))