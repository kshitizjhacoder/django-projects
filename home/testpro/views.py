
from django.db import connection
from .forms import PersonalFrom
from .models import Personal, Train, Cld, Reservation
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

# Create your views here.


sn = []


def details(request, id):
    t_name = Train.objects.filter(PNR=id)
    t_cld = Cld.objects.filter(train=id)
    t_cld_general = Cld.objects.filter(train=id, class_at="GENERAL CLASS")
    t_cld_sleeper = Cld.objects.filter(train=id, class_at="SLEEPER CLASS")
    t_cld_ac = Cld.objects.filter(train=id, class_at="AC CLASS")
    for t_c_g in t_cld_general:
        t_c_g_amt = t_c_g.amt
    for t_c_s in t_cld_sleeper:
        t_c_s_amt = t_c_s.amt
    for t_c_a in t_cld_ac:
        t_c_a_amt = t_c_a.amt

    return render(request, 'details.html', {'id': id, 't_cld_general': t_cld_general,
                                            't_cld_sleeper': t_cld_sleeper, 't_cld_ac': t_cld_ac,
                                            'class_at_g': 'GENERAL CLASS', 'class_at_s': 'SLEEPER CLASS', 'class_at_a': 'AC CLASS',
                                            't_c_g_amt': t_c_g_amt, 't_c_s_amt': t_c_s_amt, 't_c_a_amt': t_c_a_amt})


def reservation(request):
    if request.method == 'POST' and 'submit1' in request.POST:
        global sn
        sn = request.POST.getlist('sn')
        print(sn)
        t_cld = Cld.objects.filter(seat_no=sn[0])
        l = len(sn)
        for t in t_cld:
            amt = t.amt*l
        return render(request, 'reservation.html', {'t_cld': t_cld, 'length_selected': l, 'sn': sn, 'amt': amt})
    elif request.method == 'POST' and 'submit2' in request.POST:
        em = request.POST.get('email')
        pw = request.POST.get('password')
        t_pers = Personal.objects.filter(email=em, password=pw)
        if not t_pers:
            return render(request, 'signup.html')
        print(t_pers)
        print(sn)
        for s in sn:
            post = Reservation()
            post.email = em
            post.password = pw
            post.seat_no = s
            post.save()
        emum = EmailMessage(
            "Your Confirmation", "Thank you for choosing us. Your Ticket have been confirmed. if you wish to see go to the cancel page", to={em})
        if emum.send():
            messages.success(request, 'Enjoy our ride')
        return render(request, 'reservation.html', {'book': True})


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account"
    message = render_to_string('message_to_email.html', {
        'user': user.name,
        # 'domain': get_current_site(request).domain,
        # 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        # 'token': account_activate_token.make_token(user),
        # 'protocol': https if request.is_secure() else http
    })
    email = EmailMessage(mail_subject, message, to={to_email})
    if email.send():
        messages.success(request, 'the mail has been sent')
    else:
        messages.error(request, 'please check your data')


def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()

    return row


def cancel(request, id=0):
    if request.method == 'POST':
        em = request.POST.get('email')
        pw = request.POST.get('password')
        t_pers = Personal.objects.filter(email=em, password=pw)
        for t in t_pers:
            name = t.name
        t_res = Reservation.objects.filter(email=em, password=pw)
        if t_pers:
            return render(request, 'cancel.html', {'name': name, 't_res': t_res, 'cancel': True})

    return render(request, 'cancel.html', {})


def cancel_this(request, id):
    t_res = Reservation.objects.filter(id=id)
    for t in t_res:
        st = t.seat_no
        if '2s' in st:
            amt = 300
        if 'sl' in st:
            amt = 600
        if 'ac' in st:
            amt = 900
    t_res.delete()
    messages.success(
        request, f'you have just deleted an seat {st} and the amount {amt} will be refunded on your account')
    return redirect('home')


def home(request):
    return render(request, 'index.html', {})


def signup(request):
    if request.method == "POST":
        form = PersonalFrom(request.POST or None)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_activate = False
            user.save()
            # form.save()
            name = request.POST['name']
            email = request.POST['email']
            messages.success(
                request, f'NEW ACCOUNT CREATED WE HAVE SEND THE MAIL FOR CONFIRMATION THANK YOU : {name} and your mail is {email}')
            activateEmail(request, user, email)
            return render(request, 'index.html')

    else:
        return render(request, 'signup.html', {})


def signin(request):
    if request.method == 'POST':
        # data = form.cleaned_data
        email = request.POST['email']
        password = request.POST['password']
        obj = Personal.objects.filter(
            email=email, password=password)
        for ob in obj:
            em = ob.email
        user = authenticate(request, email=em)
        if user is not None:
            # print(obj.email)
            # if user.is_active:
            #     login(request, user)
            #     return redirect('home', request)
            return redirect('home')

        return HttpResponse('<h1>invalid Data</h1>')
    else:
        return render(request, 'signin.html', {})


def signout(request):
    logout(request)
    return redirect('home')


def pnrsearch(request):
    if request.method == 'POST':
        searched = (request.POST['pnr_no'])
        t_name = Train.objects.filter(name_of_train=searched)
    #     t_times = Times.objects.filter(PNR_NO__contains=searched)
        for t in t_name:
            tn = t.name_of_train
            tc = t.no_of_coach
            t_pn = t.PNR
            ts = t.Source
            td = t.Destination
        return render(request, 'pnrsearch.html', {'searched': searched,
                                                  't_name': t_name})
    else:
        return render(request, 'pnrsearch.html', {})


def timesearch(request):
    if request.method == 'POST':
        src = request.POST['src']
        dest = request.POST['dest']
        t_times = Train.objects.filter(
            Source__contains=src, Destination__contains=dest)
        return render(request, 'timesearch.html', {'tt': t_times})
    return render(request, 'timesearch.html', {})

# post = Personal()
    # post.email = request.POST.get("email")
    # post.password = request.POST.get("password")
    # post.name = request.POST.get("Name")
    # post.phone = request.POST.get("phn")
    # post.street = request.POST.get("addr")
    # post.city = request.POST.get("City")
    # post.sex = request.POST.get("gender")
    # post.bday = request.POST.get("day")
    # post.bmonth = request.POST.get("month")
    # post.byear = request.POST.get("year")
