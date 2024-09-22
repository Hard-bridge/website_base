from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, New, Category
'''ф-ция представления index'''
def index(request):
    return render(request, 'index.html')


'''ф-ция представления reg'''
def reg(request):
    suc = ''
    error = ''
    if request.method == 'POST':
        fio = request.POST['fio']
        login = request.POST['login']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']


        if len(fio) < 4 or len(login) < 4 or len(password) < 4 or len(email) < 4 or len(phone) < 4:
            error = 'Ошибка'
        else:
            if User.objects.filter(login=login).exists() or  User.objects.filter(email=email).exists():
                error += 'Такой логин и/или email существует!'
            else:
                user = User()
                user.login = login
                user.password = password
                user.fio =fio
                user.email = email
                user.phone = phone
                user.save()
                suc = 'Регистрация прошла успешно!'
    return render(request, 'reg.html', context={'suc': suc, 'error': error})


def auth(request):
    error = ''
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        if User.objects.filter(login=login).exists() and User.objects.filter(password=password).exists():
            request.session['login'] = login
            return redirect('/panel')
        else:
            error = 'Такой логин и/или пароль не существует!'
    return  render(request, 'auth.html', context={'error': error})

def panel(request):
    suc = ''
    error = ''
    user_current = User.objects.filter(login=request.session['login']).first()
    cats = Category.objects.all()
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        if User.objects.filter(login=request.session['login']).exists() and User.objects.filter(password=old_password).exists():
            id = User.objects.filter(login=request.session['login']).first().id
            user = User(id=id)
            user.password = new_password
            user.email = 'test@test.ru'
            user.phone = 12345
            user.save()
            suc += 'Пароль успешно обновлен!'
        else:
            error += 'Не правльно введен старый пароль!'

    return render(request, 'panel.html', context={'suc': suc, 'error': error, 'user_current': user_current, 'cats': cats})

def logout(request):
    if 'login' in request.session:
        del request.session['login']

    return redirect('/auth')

def edit_user_data(request):
    if request.method == 'POST':
        fio = request.POST['fio']
        email = request.POST['email']
        phone = request.POST['phone']
        id = User.objects.filter(login=request.session['login']).first().id
        '''user = User(id=id)
        user.email = email
        user.phone = phone
        user.fio = fio
        user.save()'''
    return redirect('/panel')

def editavatat(request):
    if 'login' in request.session:
        if request.method == 'POST':
            if 'avatar' in request.FILES:
                file = request.FILES['avatar']
                fs = FileSystemStorage()
                fs.save('avatars/'+file.name, file)
                path = 'avatars/'+file.name
                id_user = User.objects.filter(login=request.session['login']).first().id
                ins = get_object_or_404(User, id=id_user)
                ins.avatar = path
                ins.save()
        return redirect('/panel')

def addnew(request):
    if 'login' in request.session:
        if request.method == 'POST':
            if 'image' in request.FILES:
                file = request.FILES['image']
                fs = FileSystemStorage()
                fs.save('news/' + file.name, file)

                title = request.POST['title']
                description = request.POST['description']
                id_user = User.objects.filter(login=request.session['login']).first().id
                current_user = User.objects.get(id=id_user)
                image = 'news/' + file.name
                cat = Category.objects.get(id = request.POST['cat'])

                new = New()
                new.title = title
                new.description = description
                new.user = current_user
                new.image = image
                new.category = cat
                new.save()

                return redirect('/panel')

def news(request):
    news = New.objects.all()
    return render(request, 'new.html', context={'news': news})

def newid(request, id):
    new = New.objects.filter(id=id).first()
    return render(request, 'newid.html', context={'new': new})

def like(request, id):
    new_1 = New.objects.filter(id=id).first()

    new = New(id=id)
    new.count_like = new_1.count_like +  1
    new.title = new_1.title
    new.description = new_1.description
    new.image = new_1.image
    new.category = new_1.category
    new.user = new_1.user
    new.save()

    return redirect('/news')