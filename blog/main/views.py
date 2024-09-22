from django.shortcuts import render, redirect
from .models import News, View, User
from django.contrib.auth.hashers import make_password, check_password

def index(request):
    news = News.objects.order_by('-create_at')
    return render(request, 'index.html', {'news': news})

def about(request):
    return render(request, 'about.html')


def detail(request, id): #ud=2
    new = News.objects.filter(id=id).first()
    if View.objects.filter(new=new).exists():
        id = View.objects.filter(new=new).first().id
        a = View.objects.get(id=id)
        a.count += 1
        a.save()
    else:
        v = View()
        v.new = new
        v.count = 1
        v.save()

    count = View.objects.filter(new=new).first()
    return render(request,'detail.html', {'new': new, 'count': count})


def reg(request):
    if 'user' in request.session:
        return redirect('/panel')
    m = ''
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        fio = request.POST['fio']
        u = User()
        u.login = login
        u.password = make_password(password)
        u.fio = fio
        u.save()
        m = 'Вы успешно зарегистрированы!'

    return render(request, 'reg.html',{'m':m})

def auth(request):
    if 'user' in request.session:
        return redirect('/panel')
    error = ''
    if request.method == 'POST':

        if User.objects.filter(login=request.POST['login']).exists():
            user = User.objects.filter(login=request.POST['login']).first()
            if check_password(request.POST['password'], user.password):
                request.session['user'] = request.POST['login']
                return redirect('/panel')
            else:
                error = 'Пароль error!!'
        else:
            error = 'Логин error!!'

    return render(request, 'auth.html', {'error': error})

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('/')

def panel(request):
    if 'user' in request.session:
        current_user = User.objects.filter(login=request.session['user']).first()
        errors = ''
        suc = ''
        if request.method == 'POST':
            old_password = request.POST['old_password']
            new_password_1 = request.POST['new_password_1']
            new_password_2 = request.POST['new_password_2']
            if check_password(old_password, current_user.password):
                if new_password_1 == new_password_2:
                    current_user.password = make_password(new_password_1)
                    current_user.save()

                    suc += 'Пароль успешно изменен!'
                else:
                    errors += 'Пароли не совпали!'
            else:
                errors += 'Password error'

        current_user = User.objects.filter(login=request.session['user']).first()
        return render(request, 'lk/panel.html', {'current_user': current_user, 'errors': errors, 'suc': suc})