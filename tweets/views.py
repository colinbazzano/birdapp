import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

# we do .models because we are in the directory with tweet in it
from .models import Tweet
from .forms import TweetForm
# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    # init tweet form class with data, or not!
    form = TweetForm(request.POST or None)
    # checking if the form is valid
    if form.is_valid():
        # if it IS valid, we save it, or we can do other form related logic
        obj = form.save(commit=False)
        # save it to the database
        obj.save()
        # reinit the form as a blank form
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})


def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    consume by JavaScript
    return json data
    """
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content,
                    "likes": random.randint(0, 1000)} for x in qs]
    data = {
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    # print(args, kwargs)
    """
    REST API VIEW
    consume by JavaScript
    return json data
    """
    data = {
        "id": tweet_id,
        # "content": obj.content
        # "image_path": obj.image.url
    }
    status = 200
    try:
        # get the tweet with the specified id
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    # obj.content is from our models. it's the tweet's content

    # json.dumps content_type='application/json'
    return JsonResponse(data, status=status)
    # return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}</h1>")
