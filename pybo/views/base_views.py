from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
from django.db.models import Q, Count

def index(request):
    """
    pybo 목록 출력
    """
    3/0
    #입력 인자
    page=request.GET.get('page','1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')

    #정렬
    if so == 'recommended':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        question_list = Question.objects.order_by('-create_date')

    #조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw)|
            Q(content__icontains=kw)|
            Q(author__username__icontains=kw)|
            Q(answer__author__username__icontains=kw)
        ).distinct()

    paginator=Paginator(question_list, 10)
    page_obj=paginator.get_page(page)
    context={'question_list': page_obj, 'page':page, 'kw':kw, 'so':so}
    #return HttpResponse("안녕하세요 pybo에 오신 것을 환영합네다")
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    print(request)
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)
