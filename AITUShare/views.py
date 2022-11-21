from django.shortcuts import render, redirect, HttpResponse
from profiles.forms import RegisterForm, LoginForm
from profiles.models.profiles import Profile, Verification
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from AITUShare.settings import ALLOWED_HOSTS, EMAIL_HOST_USER
import re
import hashlib


def index(request):
    return render(request, 'main/index.html', {'login': bool(request.session.get('login', False))})


def logout(request):
    request.session.clear()
    return redirect('index')


def login_page(request):

    if request.method == "GET":
        if not request.session.get('login', False):
            return render(request, 'auth/login_page.html', {'form': LoginForm})
        else:
            return redirect('index')
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login = login_form.clean().get('login')
            passwd = login_form.clean().get('password')
            remember = login_form.clean().get('remember')

            db_profile = Profile.objects.filter(login__exact=login)[0]
            if check_password(passwd, db_profile.password):
                request.session.set_expiry(7*24*60*60 if remember else 0)
                request.session['first_name'] = db_profile.first_name
                request.session['last_name'] = db_profile.last_name
                request.session['email'] = db_profile.email
                request.session['login'] = login
                request.session['hash'] = passwd
                return redirect('forum_index')
            else:
                return render(request, 'auth/login_page.html', {'err': "Password or login aren't correct"})


def register_page(request, err=None):
    # check if request is from browser
    if request.method == "GET":
        if not request.session.get('login', False):
            return render(request, 'auth/register_page.html', {'form': RegisterForm, 'err': err})
        else:
            return redirect('index')

    elif request.method == "POST":
        # POST request processing
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():

            # some checks about email
            email_pattern = r'^\d+@astanait.edu.kz$'
            if not re.match(email_pattern, register_form.clean().get('email')):
                # not aitu's email
                return render(request, 'auth/register_page.html', {'err': "Not AITU email"})

            first_name = register_form.clean().get('first_name')
            last_name = register_form.clean().get('last_name')
            email = register_form.clean().get('email')
            login = register_form.clean().get('login')
            passwd = make_password(register_form.clean().get('password'))

            _hash = hashlib.md5(login.encode()).hexdigest()
            if Profile.objects.filter(login__exact=login).exists()\
                    or Profile.objects.filter(email__exact=email).exists():
                return render(request, 'auth/register_page.html', {'err': 'Same user/email already registered'})

            Verification.objects.create(
                email=email,
                hash_key=_hash,
                status=False
            )

            verification_link = f"http://{ALLOWED_HOSTS[0]}:8000/verify_auth?_hash={_hash}"
            email_to_string = strip_tags(render_to_string('auth/email.html', {'verification_link': verification_link}))
            send_mail(
                'Verification',
                email_to_string,
                EMAIL_HOST_USER,
                [email],
                fail_silently=True
            )
            print("sent")

            Profile.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                login=login,
                password=passwd).save()

            request.session.set_expiry(0)
            request.session['login'] = login
            request.session['hash'] = passwd

            return render(
                request,
                'auth/register_success.html',
                {
                    'email': email
                }
            )


def verify_auth(request):
    if request.method == "GET":
        _hash = request.GET.get('_hash', False)
        if _hash:
            hash_obj = Verification.objects.filter(hash_key=_hash)
            if hash_obj.exists():
                hash_obj = Verification.objects.get(hash_key=_hash)
                hash_obj.status = True
                hash_obj.save()

    return redirect('index')
