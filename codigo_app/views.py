from django.shortcuts import render, redirect, HttpResponse
from .models import SignupForm, Blog, Comment
from django.contrib import auth
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

@login_required(login_url='/loginform')
def index(request):
    tag = request.GET.get('tag')
    title = request.GET.get('title')
    blog_list = Blog.objects.all()
    if tag:
        blog_list = blog_list.filter(tags__name__icontains=tag)
    if title:
        blog_list = blog_list.filter(title__icontains=title)

    paginator = Paginator(blog_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})


def user_signup(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("confirm-password")
        if password == cpassword:
            user = SignupForm.objects.create_user(username=email, first_name=first_name, last_name=last_name, name=first_name+' '+ last_name, email=email, password=password)
            auth.login(request, user)
            return redirect(index)
        else:
            return render(request,"user_signup.html", {"message":"Password and confirm password Does not match"})
    return render(request,"user_signup.html")

@login_required(login_url='/loginform')
def logout(request):
    auth.logout(request)
    return redirect(index)

def loginform(request):
    if request.method == "POST":
        email = request.POST.get("uname")
        password = request.POST.get("psw")
        user = auth.authenticate(request, username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(index)  # Redirect to the user's profile page or any other desired page
        else:
            return render(request, 'loginform.html', {'error_message': 'Invalid login credentials'})
    return render(request,"loginform.html")


def blog_detail(request, id):
    share = request.GET.get('share')
    if not share:
        if not request.user.is_authenticated:
            return redirect('/loginform')

    blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(blog=blog)
    if request.method == 'POST':
        text = request.POST.get('text')
        Comment.objects.create(blog=blog, user=request.user, comment=text)
        return redirect('blog_detail', id=id)
    return render(request, 'blog.html', {'page_obj': blog, 'comments': comments})

def share_blog(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        id = request.POST.get("id")
        if email:
            url = f'http://localhost:8000/blog-deatail/{id}?share=True'
            subject = 'Blog shared'
            message = 'This is a test email sent from Django.'
            from_email = 'website.uxuistudio@gmail.com'
            recipient_list = [email]
            send_mail(subject, url, from_email, recipient_list)
            return redirect('blog_detail', id=id)
        else: 
            return HttpResponse("Email not provided")
    else: 
        return HttpResponse("Method not allowed")

