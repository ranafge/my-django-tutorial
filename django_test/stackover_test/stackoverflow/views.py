from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import generic
from . import models
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class ApplicantListView(ListView):
    model = models.Applicant
    paginate_by = 100
    template_name = 'stackoverflow/applicant_list.html'


def partList(request):
    allparts = models.Part.objects.all()
    allpatterns = models.Pattern.objects.filter(patterns__in=allparts)

    context = {"allparts": allparts, "allpatterns": allpatterns}
    return render(request, 'stackoverflow/partlist.html', context=context)


class PostList(ListView):
    queryset = models.Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


def LikeView(request):
    post = models.Post.objects.get(id=1)
    post.likes.add(request.user)
    return render(request, 'stackoverflow/post-list.html', {'post': post})


class IndexView(generic.View):
    model = models.Comment
    template_name = 'stackoverflow/index.html'
    form_class = forms.CommentForm

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')

    def get_context_data(self, **kwargs):
        context = {}
        context["commentaries"] = self.get_queryset()
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form.errors.as_json()
            return redirect('home:index')


def home(request):
    postings = models.Post.objects.all()

    return render(request, 'stackoverflow/front.html', context={"postings": postings})


def comment_form_view(request):
    form = forms.CommentForm(initial={'name': 'comment name ', 'comment': 'comment body'})
    form.fields['comment'].queryset = models.Comment.objects.filter(comment='x')
    comments = models.Comment.objects.all()
    context = {}
    context['comments'] = comments.values()
    context['form'] = form
    return render(request, 'stackoverflow/comment-form-view.html', context=context)


class SignUpView(CreateView):
    template_name = 'stackoverflow/signup.html'
    form_class = UserCreationForm


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.get(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


def username_exists(request):
    data = {'msg': ''}
    if request.method == 'GET':
        username = request.GET.get('username', None)
        exists = User.objects.filter(username=username).exists()
        print(exists)
        if exists:
            data['msg'] = username + ' already exists.'
        else:
            data['msg'] = username + ' does not exists.'
    return JsonResponse(data)


def ajax_test(request):
    if request.is_ajax():
        message = 'THis is ajax'
    else:
        message = 'Not ajax'
    return HttpResponse(message)


class RoomList(generic.View):
    def get(self, request):
        rooms = list(models.Room.objects.all().values())
        data = dict()
        data['rooms'] = rooms
        return JsonResponse(data)


class RoomDetail(generic.View):
    def get(self, request, pk):
        room = get_object_or_404(models.Room, pk=pk)
        data = dict()
        data['room'] = room
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class RoomCreate(CreateView):
    def post(self, request):
        data = dict()
        form = forms.RoomModelForm(request.POST)
        if form.is_valid():
            room = form.save()
            data['room'] = model_to_dict(room)
        else:
            data['error'] = 'form not valid'
        return JsonResponse(data)


class RoomUpdate(generic.View):
    def post(self, request, pk):
        data = dict()
        room = models.Room.objects.get(pk=pk)
        form = RoomModelForm(instance=room, data=request.POST)
        if form.is_valid():
            room = form.save()
            data['room'] = model_to_dict(room)
        else:
            data['error'] = 'form not valide'
        return JsonResponse(data)


class RoomDelete(generic.View):
    def post(self, request, pk):
        data = dict()
        room = models.Room.objects.get(pk=pk)
        if room:
            room.delete()
            data['message'] = 'Room Deleted'
        else:
            data['message'] = 'Error on delete'
        return JsonResponse(data)


# Readonly filed or disable so that it can't be editable.

def new_item_view(request):
    if request.method == 'POST':
        form = forms.ItemForm(request.POST)
        if form.is_valid():
            form.save()
        # Validate and save
    else:
        form = forms.ItemForm()
    mydict = {"key1": "value1", "key2": "value2"}

    return render(request, 'stackoverflow/skuitem.html', {"form": form, 'mydict': mydict})

# todo new_item_view need to update view


from django.core.exceptions import PermissionDenied

def your_view(request):
    raise PermissionDenied()

def django_divisibleby_test(request):
    posts = models.Post.objects.all()
    return render(request, 'stackoverflow/post_list.html', {'posts':posts})




