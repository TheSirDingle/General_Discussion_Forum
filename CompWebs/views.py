import datetime

import django.urls
from django.shortcuts import render, get_object_or_404, redirect
from .models import GamingTopic, GamingPost
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.views.generic import CreateView
from django.core.paginator import Paginator
from .forms import PostCreationForm
from django.contrib import messages

def index(request):

    return render(request, 'CompWebs/index.html')

def about(request):
    return render(request, 'CompWebs/about.html')

def GameForum(request):

    # # reference to the topic table
    # context = {
    #     "topics": GamingTopic.objects.all()
    # }

    all_topic = GamingTopic.objects.filter().order_by('-Tdate_Created')
    paginator = Paginator(all_topic, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'CompWebs/game_forum_topic.html', {'topics': page_obj})


def Post_Top(request, topic_title, topic_id):

    print(topic_title)
    print(topic_id)

    # print(GamingTopic.objects.filter(pk = topic_id).first())

    form_class = PostCreationForm

    # .order_by('-Pdate_Created') for line under in case
    post_number = GamingPost.objects.filter(Post_Topic__T_Title=topic_title)
    paginator = Paginator(post_number, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():

            needed_data = form.save(commit=False)
            needed_data.Post_Topic = GamingTopic.objects.get(id=topic_id)
            needed_data.author = request.user
            needed_data.Pdate_Created = datetime.datetime.now()
            needed_data.save()

            form.save()

            messages.success(request, f'Your post has been created')
            return redirect(django.urls.reverse('Topic-Post', kwargs={'topic_title': topic_title, 'topic_id': topic_id}))
    else:
        print('stuff')

    context = {
        "form": PostCreationForm(),
        "posts": page_obj,
    }

    return render(request, 'CompWebs/Topic_Post.html', context)


class GamingCreateTopic(LoginRequiredMixin, CreateView):
    model = GamingTopic
    fields = ['T_Title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = '../../GamingDiscussion/'

