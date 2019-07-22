from django.shortcuts import render,HttpResponse,get_object_or_404,reverse,HttpResponseRedirect
from .models import Question,Choice
from django.views import generic
# Create your views here.
# def index(request):
#     question_list = Question.objects.order_by('-pubDate')[:3]
#     #str = ','.join([q.questionText for q in question_list])
#     return render(request,'index.html',{'question_list':question_list})

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pubDate')[:3]

# def details(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'details.html',{'question':question})
class DetailsView(generic.DetailView):
    model = Question
    template_name = 'details.html'
def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'results.html',{'question':question})

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'details.html',{"question":question,"errormsg":'你没有选中项目'})
    else:
        choice.vote+=1
        choice.save()
        return HttpResponseRedirect(reverse("polls:result",args=(question_id,)))

def date(request,year,month,day):
    return HttpResponse('%s-%s-%s'%(year,month,day))