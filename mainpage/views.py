from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Dogovor, KT
from .forms import DogovorForm
import datetime, os, io
from mailmerge import MailMerge
from datetime import timedelta, datetime
from django.core.mail import send_mail


# Create your views here.
def index(request):
    dogovori = Dogovor.objects.all()
    return render(request, 'mainpage/index.html', {'title': 'Таблица договоров', 'dogovori': dogovori})


def add(request):
    error = ''
    if request.method == 'POST':
        form = DogovorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма'

    form = DogovorForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainpage/add.html', context)


def delete_dogovor(request, dogovor_id):

    el = Dogovor.objects.get (id = dogovor_id)
    el.delete()

    return redirect('home')


def contacts(request):
    return render(request, 'mainpage/contacts.html')


def detail(request, dogovor_id):
    try:
        el = Dogovor.objects.get (id = dogovor_id)
    except:
        raise Http404("Договор не найден")

    comments = el.comment_set.order_by('id')
    kts = el.kt_set.order_by('id')
    for k in kts:
        d0 = datetime.now().date()
        d1 = k.kt_end
        delta = d0 - d1
        k.prosrochka = int(str(delta.days))
        # if k.prosrochka > 0:
        #     send_mail('Просрочка', 'Добрый день! У вас просрочка контрольной точки, зайдите на сайт.', 'tartemm1@gmail.com', ['tartem-98@mail.ru'], fail_silently=False)
    return render(request, 'mainpage/detail.html', {'dogovor': el, 'comments': comments, 'kts': kts})


def leave_comment(request, dogovor_id):
    try:
        el = Dogovor.objects.get (id = dogovor_id)
    except:
        raise Http404("Договор не найден")

    el.comment_set.create(author = request.POST['author'], comment_text = request.POST['comment_text'])
    return HttpResponseRedirect(reverse ('detail', args = (el.id,)))


def new_kt(request, dogovor_id):
    try:
        el = Dogovor.objects.get (id = dogovor_id)
    except:
        raise Http404("Договор не найден")

    el.kt_set.create(kt_name = request.POST['kt_name'], kt_status = request.POST['kt_status'], kt_start = request.POST['kt_start'], kt_end = request.POST['kt_end'])
    return HttpResponseRedirect(reverse ('detail', args = (el.id,)))


def pretenzia(request, dogovor_id):
    try:
        el = Dogovor.objects.get (id = dogovor_id)
    except:
        raise Http404("Договор не найден")

    if el.type == 'postavka':
        template = os.path.join(os.path.dirname(__file__), 'docs/Pretenzia.docx')
    elif el.type == 'uslugi':
        template = os.path.join(os.path.dirname(__file__), 'docs/uslugi.docx')
    elif el.type == 'perevoz':
        template = os.path.join(os.path.dirname(__file__), 'docs/perevozka.docx')
    elif el.type == 'stroitelny':
        template = os.path.join(os.path.dirname(__file__), 'docs/podryad.docx')

    document = MailMerge(template)

    document.merge(flag="tut nado vstavit text",)

    f = io.BytesIO()
    document.write(f)
    length = f.tell()
    f.seek(0)
    response = HttpResponse(f.getvalue(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=pretenzia.docx'
    response['Content-Length'] = length

    return response
    return HttpResponseRedirect(reverse ('detail', args = (el.id,)))
