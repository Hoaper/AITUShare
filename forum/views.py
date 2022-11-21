from django.shortcuts import render, HttpResponse, Http404, redirect, reverse
from django import forms
from .models import *
from .forms import *


def forum_index(request):

    main_topics = MainTopic.objects.all()
    topics = []
    for i in main_topics:
        topics.append(Topic.objects.filter(main_topic=i))

    return render(request, 'forum_index.html', {
        # "main_topics": main_topics,
        "topics": topics,
        "login": bool(request.session.get('login', False)),
        "first_name": request.session.get('first_name', ''),
        "last_name": request.session.get('last_name', ''),
        "email": request.session.get('email', '')})


def forum_person(request,  topic_id):

    if request.method == "GET":
        try:
            topic = Topic.objects.get(id__exact=topic_id)
        except:
            raise Http404()

        comments = Comment.objects.filter(topic__exact=topic)
        if len(comments) == 0:
            comments = []
        form = SendComment(label_suffix=None)
        return render(request, 'forum_person.html', {"comments": comments, "topic": topic,
                                                     "login": bool(request.session.get('login', False)),
                                                     "first_name": request.session.get('first_name', ''),
                                                     "last_name": request.session.get('last_name', ''),
                                                     "email": request.session.get('email', ''),
                                                     "form": form})
    else:
        form = SendComment(request.POST)
        if form.is_valid():
            Comment.objects.create(
                topic=Topic.objects.get(id__exact=topic_id),
                author=Profile.objects.get(login__exact=request.session.get('login')),
                text=form.clean().get("text")
            ).save()

        return redirect(reverse('forum_index') + f'/{topic_id}')


def forum_create_topic(request):

    if request.method == "GET":
        main_topics = MainTopic.objects.all()
        form = CreateTopic()
        return render(request, 'create.html', {"main_topics": main_topics,
                                                "login": bool(request.session.get('login', False)),
                                                "first_name": request.session.get('first_name', ''),
                                                "last_name": request.session.get('last_name', ''),
                                                "email": request.session.get('email', ''),
                                                "form": form})

    else:
        wcom = MainTopic.objects.get(name__exact='Welcome')
        form = CreateTopic(request.POST)
        if form.is_valid():
            Topic.objects.create(
                main_topic=wcom,
                title=form.clean().get('tittle'),
                text=form.clean().get('text'),
                author=Profile.objects.get(login__exact=request.session['login']),
                accepted=True
            ).save()
        return redirect('forum_index')

