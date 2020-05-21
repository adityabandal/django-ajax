from django.http import JsonResponse
from django.core import serializers
from .forms import RepoForm
from .models import Repository
from django.shortcuts import render

def indexView(request):
    form = RepoForm()
    friends = Repository.objects.all()
    return render(request, "index.html", {"form": form, "friends": friends})

def postFriend(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = RepoForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)
