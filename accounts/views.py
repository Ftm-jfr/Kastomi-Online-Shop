from datetime import date
from sqlite3 import IntegrityError

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from accounts.forms import CustomUserForm, LoginForm, ContactInfoForm, UserInfoForm, AccountInfoForm
from accounts.models import CustomUser, City, Province, UserProfile

from django.http import JsonResponse
from accounts.models import City


def get_cities(request):
    province_id = request.GET.get('province_id')
    if province_id:
        cities = City.objects.filter(province_id=province_id).values('id', 'name')
        return JsonResponse({'cities': list(cities)})
    else:
        return JsonResponse({'cities': []})


@login_required
def user_profile_view(request):
    user = request.user
    profile = getattr(user, 'profile', None)
    form = CustomUserForm(instance=user)

    return render(request, 'user-profile.html', {
        'form': form,
        'profile': profile,
        'user': user,
    })


def customer_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        print(form.errors)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "نام کاربری یا رمز عبور اشتباه است.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def signup_userInfo_view(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.copy()
            dob = data.get('date_of_birth')
            if dob:
                data['date_of_birth'] = dob.isoformat()  # تبدیل به رشته "YYYY-MM-DD"
            request.session['user_info'] = data
            return redirect('signup-contactInfo')

    else:
        form = UserInfoForm()
    return render(request, 'user-signup-userInfo.html', {'form': form})


def signup_contactInfo_view(request):
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user_info = request.session.get('user_info')
            if user_info is None:
                return redirect('signup-userInfo')
            data = {**user_info, **form.cleaned_data}

            province_instance = data['province']
            city_instance = data['city']

            user = CustomUser(
                full_name=data['full_name'],
                national_code=data['national_code'],
                job=data['job'],
                education=data['education'],
                email=data['email'],
                date_of_birth=date.fromisoformat(data['date_of_birth']),
                mobile_number=data['mobile_number'],
                telephone_number=data['telephone_number'],
                province=province_instance,
                city=city_instance,
                postal_code=data['postal_code'],
                full_address=data['full_address'],
                # password=make_password(data['password']),
            )
            user.set_password(data['password'])
            user.save()
            request.session.pop('user_info', None)
            return redirect('home')
    else:
        form = ContactInfoForm()
    return render(request, 'user-signup-contactInfo.html', {'form': form})


def password_validation(form):
    if form.is_valid():
        if form.password == form.confirm_password:
            return True
    return False


class AccountForm:
    pass



@login_required(login_url='login')
def account_info(request):
    user = request.user
    profile = getattr(user, 'profile', None)

    if request.method == 'POST':
        form = AccountInfoForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            return redirect('accountInfo')
    else:
        form = AccountInfoForm(instance=user)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'account-info.html', context)
