import json
import uuid

from django.core.serializers import serialize
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from django.utils.safestring import mark_safe
from django.utils import timezone

from server.models import ChatRoom, Message, User
from server.serializers import MessageSerializer


def __get_user(request: HttpRequest) -> User:
    user_name = request.headers["username"]
    return User.objects.filter(username=user_name)[0]


def index(request):
    return render(request, "chat/index.html", {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def login(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()
    username = uuid.uuid4().hex[:8]
    response["username"] = username
    user = User(username=username)
    user.save()
    return response

def logout(request: HttpRequest):
    user = __get_user(request)
    user.last_seen = timezone.now()
    requested_room = request.headers["room"]
    room = ChatRoom.objects.filter(name=requested_room)[0]
    user.last_room = room
    user.save()
    return HttpResponse("")


def get_rooms_list(request: HttpRequest) -> JsonResponse:
    all_names = ChatRoom.objects.all().values_list("name", flat=True)
    return JsonResponse(list(all_names), safe=False)


def get_messages(request: HttpRequest):
    try:
        user = __get_user(request)
        room = user.last_room
        new_messages = room.message_set.filter(timestamp__gte=user.last_seen)
        data = [message.to_str() for message in new_messages]
        # return JsonResponse(MessageSerializer(new_messages, many=True).data, safe=False)
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(e)
        raise Http404()


def send_message(request: HttpRequest):
    try:
        user = __get_user(request)
        text = str(request.body())
        message = Message(text=text, room=user.last_room)
        message.save()
        return HttpResponse("Done.")
    except:
        raise Http404()
