from django.shortcuts import render,redirect
from . import models
from . import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
def home(request):
    return render(request,'core/links.html',{'links':models.Link.objects.all().order_by('-score')})
def link(request,pk):
    link_instance = models.Link.objects.get(id=pk)
    return render(request,'core/link.html',{'link':link_instance,'comments':link_instance.comments.all()}) # type: ignore
def delLink(request,pk):
    if request.method == 'POST':
        models.Link.objects.get(id=pk).delete()
        return redirect('home')
    else:
        return render(request,'core/dellink.html',{'id':models.Link.objects.get(id=pk).id}) # type: ignore
def editLink(request,pk):
    link = models.Link.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.CreateLink(request.POST,instance=link)
        if form.is_valid():
            form.save()
            return redirect('link',pk=link.id) # type: ignore
    else:
        form = forms.CreateLink(instance=link)
    return render(request,'core/editlink.html',{'form':form})
def addComment(request,pk):
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.submitter = request.user
            comment.link =  models.Link.objects.get(id=pk)
            comment.save()
            return redirect('link',pk=comment.link.id) # type: ignore
    else:
        form = forms.CreateComment()
    return render(request,'core/addcomment.html',{'form':form})
def delComment(request,pk):
    link_id = models.Comment.objects.get(id=pk).link.id # type: ignore
    if request.method == 'POST':
        models.Comment.objects.get(id=pk).delete()
        return redirect('link',pk=link_id)
    else:
        link_id = models.Comment.objects.get(id=pk).link.id # type: ignore
        return render(request,'core/delcomment.html',{'id':link_id})
def editComment(request,pk):
    comment = models.Comment.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.CreateComment(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            return redirect('link',pk=comment.link.id) # type: ignore
    else:
        form = forms.CreateComment(instance=comment)
    return render(request,'core/editcomment.html',{'form':form})
def signIn(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request,'core/signin.html',{'form':form})
def logIn(request):
    if request.method == 'POST':
        form =  AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('home')
    else:
        form =  AuthenticationForm()
    return render(request,'core/login.html',{'form':form})
def logOut(request):
    logout(request)
    return redirect('home')

def addLink(request):
    if request.method == 'POST':
        form = forms.CreateLink(request.POST)
        if form.is_valid():
            link = form.save(commit = False)
            link.submitter = request.user
            link.save()
            return redirect('home')
    else:
        form = forms.CreateLink()
    return render(request,'core/addlink.html',{'form':form})
def upvote(request,pk):
    link = models.Link.objects.get(id=pk)
    if request.user in link.downvoters.all():
        link.downvoters.remove(request.user)
    else:
        link.upvoters.add(request.user)
    link.score = link.upvoters.all().count()-link.downvoters.all().count()
    link.save()
    return redirect('link',pk=link.id)  # type: ignore

def downvote(request,pk):
    link = models.Link.objects.get(id=pk)
    if request.user in link.upvoters.all():
        link.upvoters.remove(request.user)
    else:
        link.downvoters.add(request.user)
    link.score = link.upvoters.all().count()-link.downvoters.all().count()
    link.save()
    return redirect('link',pk=link.id)  # type: ignore
def upvoters(request,pk):
    return render(request,'core/voters.html',{'voters':models.Link.objects.get(id=pk).upvoters.all(),'type':'Up'})

def downvoters(request,pk):
    return render(request,'core/voters.html',{'voters':models.Link.objects.get(id=pk).downvoters.all(),'type':'Down'})