from django.http import JsonResponse
from django.core import serializers
from .forms import RepoForm
from .models import Repository
from django.shortcuts import render

def indexView(request):
    form = RepoForm()
    repos = Repository.objects.all()
    return render(request, "index.html", {"form": form, "repos": repos})

def checkRepoName(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        repo_name = request.GET.get("repo_name", None)
        # check for the nick name in the database.
        if Repository.objects.filter(repo_name = repo_name).exists():
            # if repo_name found return not valid new friend
            return JsonResponse({"valid":False}, status = 200)
        else:
            # if repo_name not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)

def postRepo(request):
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
