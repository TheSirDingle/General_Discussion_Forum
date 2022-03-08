from django.shortcuts import render, get_object_or_404
from .models import GamingTopic, GamingPost


def index(request):

    return render(request, 'CompWebs/index.html')

def about(request):
    return render(request, 'CompWebs/about.html')

def GameForum(request):

    # reference to the topic table
    context = {
        "topics": GamingTopic.objects.all()
    }

    return render(request, 'CompWebs/game_forum_topic.html', context)

def Post_Top(request, topic_title):

    print(topic_title)

    context = {
        "posts": GamingPost.objects.filter(Post_Topic__T_Title=topic_title),
    }
    return render(request, 'CompWebs/Topic_Post.html', context)
