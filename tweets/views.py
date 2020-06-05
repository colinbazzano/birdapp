from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

# we do .models because we are in the directory with tweet in it
from .models import Tweet
# Create your views here.


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")


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
