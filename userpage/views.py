from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, BlogPostForm
from django.contrib import messages
from .models import BlogPost
from django.views.generic import ListView, DetailView
def index(request):
    return render(request, 'index.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)  
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 'P':
                return redirect('login')  # Replace 'patient_dashboard' with the actual URL name
            elif user.user_type == 'D':
                return redirect('login')  # Replace 'doctor_dashboard' with the actual URL name
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if user.user_type == 'P':
                    return redirect('patient_page')  # Replace 'patient_dashboard' with the actual URL name
                elif user.user_type == 'D':
                    return redirect('doctor_page')  # Replace 'doctor_dashboard' with the actual URL name
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def patient_page(request):
    patient_data = request.user
    blog_posts = BlogPost.objects.filter().exclude(draft=True)
    context = {
        'patient_data': patient_data,
        'blog_posts': blog_posts,
    }
    return render(request, 'patient_page.html', context)

def doctor_page(request):
    doctor_data = request.user
    blog_posts = BlogPost.objects.filter(author=doctor_data)
    context = {
        'doctor_data': doctor_data,
        'blog_posts': blog_posts,
    }
    return render(request, 'doctor_page.html', context)

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            # Get or create the Category instance
            
        
            # Create the BlogPost instance
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()

            return redirect('doctor_page')
    else:
        form = BlogPostForm()

    return render(request, 'create_blog_post.html', {'form': form})

def blog_list(request):
    
    blog_posts = BlogPost.objects.filter(is_draft=False)

    context = {
        
        'blog_posts': blog_posts,
    }

    return render(request, 'blog_list.html', context)

def doctor_posts(request):
    doctor_posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'doctor_posts.html', {'doctor_posts': doctor_posts})

def patient_posts(request):
    patient_posts = BlogPost.objects.filter(is_draft=False)
    return render(request, 'patient_posts.html', {'patient_posts': patient_posts})

def blog_post_detail(request, pk):
    # import pdb;pdb.set_trace()
    is_doctor = False
    if request.user.user_type == 'D':
        is_doctor = True
    post = get_object_or_404(BlogPost, id=pk)
    words = post.summary.split()
    if len(words) > 15:
        post.summary = ' '.join(words[:15]) + '...'
    return render(request, 'blog_detail.html', {'post': post, 'is_doctor':is_doctor})