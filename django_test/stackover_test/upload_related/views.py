from django.views.generic.edit import CreateView
from . import forms
from django.urls import reverse_lazy
from django.shortcuts import render
from . import models
from django.http import HttpResponse

def index(request):
    return HttpResponse('url form UploadCreate class base view')
# Create your views here.
def uploadView(request):
    if request.method == 'POST':
        form = forms.DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = models.Document(docfile = request.FILES['docfile']
                                     )
            newdoc.save()
    else:
        form = forms.DocumentForm()

    documents = models.Document.objects.all()

    return render(request, 'upload_related/doclist.html', {"form":form, "documents": documents})



class UploadView(CreateView):
    model = models.Document
    template_name = 'upload_related/doclist.html'
    fields = ['docfile']
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = models.Document.objects.all()
        return context


