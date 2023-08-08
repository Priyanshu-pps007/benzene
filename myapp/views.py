from django.shortcuts import render,HttpResponse,redirect
from .models import video,ouruser,pdf,eleventh,twelveth,order,mycart,short_video
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.http import JsonResponse



n=[]
def logi(request):
    if request.method=="POST":
        user=User()
        user.username=request.POST.get('username')
        name=user.username
        n.append(name)
        user.password=request.POST.get('password')
        passw=user.password
        user = authenticate(request, username=user.username, password=user.password)
        if user is not None:
            login(request,user)
            # u=ouruser.objects.filter(username=name,password=passw)
            u=ouruser.objects.get(username=name)
            request.session['us']=name
            request.session['c'] = u.counter
            c = request.session.get('c', None)   #copy from here
            userr = request.session.get('us', None)
            myuser=ouruser.objects.filter(username=userr)
            return render(request,'myapp/index.html',{"count":c,"myu":myuser})
        else:
            return HttpResponse("Authentication failed")

def sign(request):
    if request.method=="POST":
        try:

            user=User()
            u=ouruser()
            c=mycart()
            user.username=request.POST.get('username')
            c.username=user.username
            c.save()
            u.username=user.username
            user.email=request.POST.get('email')
            user.password=request.POST.get('password')
            u.password=user.password
            u.save()
            user.set_password(user.password)
            user.save()
            return render(request,'myapp/index.html')
        except Exception as e:
            return HttpResponse("<h1>This username has been already registerd try another one </h1>")
    
def logou(request):
    n.clear()
    logout(request)
    return render(request,'myapp/index.html')


def index(request): 
    try:
        # c=ouruser.objects.filter(username=n[0])
        c = request.session.get('c', None) 
        userr = request.session.get('us', None)
        myuser=ouruser.objects.filter(username=userr)  
        return render(request,'myapp/index.html',{"count":c,"myu":myuser})
    except Exception as e:
        return render(request,'myapp/index.html')
def home(request):
    try:
        # c=ouruser.objects.filter(username=n[0])
         
        userr = request.session.get('us', None)
        myuser=ouruser.objects.filter(username=userr)
        a=ouruser.objects.get(username=userr)
        c=a.counter
        return render(request,'myapp/index.html',{"count":c,"myu":myuser})
    except Exception as e:
        return render(request,'myapp/index.html')
def contact(request):
    return render(request,'myapp/contact.html')
def course(request):
    try:
        # c=ouruser.objects.filter(username=n[0])
        
        userr = request.session.get('us', None)
        myuser=ouruser.objects.filter(username=userr)
        a=ouruser.objects.get(username=userr)
        c=a.counter
        return render(request,'myapp/courses.html',{"count":c,"myu":myuser})
    except Exception as e:
        return render(request,'myapp/courses.html')
def upload(request):
    if request.method=="POST":
        chem=video()
        chem.video=request.FILES['video']
        chem.save()
        return HttpResponse("File uploaded successfully")       
    
def loader(request):
    return render(request,'myapp/loader.html')

def show(request):
    chem=video.objects.all()
    userr = request.session.get('us', None)
    u=ouruser.objects.filter(username=userr)
    return render(request,'myapp/dashboard1.html',{"course":chem,"userr":u})
def logandsin(request):
    return render(request, 'myapp/signupandlogin.html')

@csrf_exempt
def cart(request):
    c = request.session.get('c', None)
    userr = request.session.get('us', None)
    print(userr)
    u=ouruser.objects.filter(username=userr)
    print("paying")
    cart=mycart.objects.get(username=userr)
    if(cart.eleven.all() or cart.twelve.all()):
        el=cart.eleven.all()
        tw=cart.twelve.all()
        u=ouruser.objects.get(username=userr)
        uss=u.counter
        myuser=ouruser.objects.filter(username=userr)
        return render(request,'myapp/cart.html',{"el":el,"userr":uss,"count":uss,"myu":myuser,"tw":tw})
    else:
        o=ouruser.objects.get(username=userr)
        count=o.counter
        myuser=ouruser.objects.filter(username=userr)
        return render(request,'myapp/empty.html',{"count":count,"myu":myuser})


@csrf_exempt
def paid(request):
    print("paying")
    if request.method=="POST":
        print("paying")

        client = razorpay.Client(auth=("rzp_test_CUCNWEytRu04a5", "0oeN6h68TptSe8iFmKRo7L3F"))

        DATA = {
        "amount": 5000,
        "currency": "INR",
        "payment_capture":0,
        }
        client=razorpay.Client(auth=('rzp_test_CUCNWEytRu04a5','0oeN6h68TptSe8iFmKRo7L3F'))
        order=client.order.create(data=DATA)
        orderr=order['id']
        print(orderr)
        print("your order is ",order)
        return render(request,'myapp/home_dashboard.html',{"payment":orderr})
        # client.order.fetch(orderId)


@csrf_exempt
def verifypay(request):
    razorpay_client = razorpay.Client(auth=("rzp_test_CUCNWEytRu04a5", "0oeN6h68TptSe8iFmKRo7L3F"))
    if request.method == "POST":
        userr = request.session.get('us', None)
        u=ouruser.objects.get(username=userr)
        payload = request.body.decode('utf-8')  # decode the raw data to a string
        a=payload.split("&")
        u.razorpay_payment_id=a[0]
        u.razorpay_order_id=a[1]
        m=u.razorpay_order_id.split("=")
        print(m[1])
        var2=order.objects.get(order_id=m[1])
        var=u.userorder.add(var2)
        var2.flag="True"
        var2.save()
        u.razorpay_signature=a[2]
        u.save()
        print(a)
        if "razorpay_signature" in request.POST:
            payment_verification = razorpay_client.utility.verify_payment_signature(request.POST)
            if payment_verification:
                
                return redirect('home')
            else:
                var2.flag="false"
                return HttpResponse('failed')
        
              # Logic to perform is payment is unsuccessful
    return HttpResponse("success")


@login_required(login_url=logandsin)

def adding(request):
    
    if request.method=="POST": 
        user = request.session.get('us', None)
        u=ouruser.objects.get(username=user)

        if request.method=="POST":
            car=mycart.objects.get(username=user)
            chapter=request.POST.get('chapter')
            try:
                if(car.eleven.get(chapter_name=chapter)):
                    pass
            except Exception as e:
                u.counter=u.counter+1
                print(car)
                print(chapter)
                obj=eleventh.objects.get(chapter_name=chapter)
                car.eleven.add(obj)
            
                print(obj)
                car.save()
                u.save()
        u.save()
    return redirect('eleventh')

def addin(request):
    if request.method=="POST": 
        user = request.session.get('us', None)
        u=ouruser.objects.get(username=user)

        if request.method=="POST":
            car=mycart.objects.get(username=user)
            chapter=request.POST.get('chapter')
            try:
                if(car.twelve.get(chapter_name=chapter)):
                    pass
            except Exception as e:
                u.counter=u.counter+1
                print(car)
                print(chapter)
                obj=twelveth.objects.get(chapter_name=chapter)
                car.twelve.add(obj)
            
                print(obj)
                car.save()
                u.save()
        u.save()
    a=ouruser.objects.get(username=user)
    c=a.counter
    print(c)
    myuser=ouruser.objects.filter(username=user)
    return redirect('twelveth')
@login_required(login_url=logandsin)
def learn(request):
    userr = request.session.get('us', None)
    myuser=ouruser.objects.filter(username=userr)
    a=ouruser.objects.get(username=userr)
    obj=twelveth.objects.all()
    c=a.counter    
    return render(request,'myapp/dashboard-2.html',{"myu":myuser,"count":c,"obj":obj})

@login_required(login_url=logandsin)
def learning(request):
    userr = request.session.get('us', None)
    myuser=ouruser.objects.filter(username=userr)
    a=ouruser.objects.get(username=userr)
    obj=eleventh.objects.all()
    c=a.counter
    return render(request,'myapp/dashboard1.html',{"myu":myuser,"count":c,"obj":obj})

def dash(request):
    return render(request,'myapp/dashboard2.html')

@login_required(login_url=logandsin)
@csrf_exempt
def celeven(request):
    obj=eleventh.objects.all()
    userr = request.session.get('us', None)
    print(userr)
    u=ouruser.objects.filter(username=userr)
    print("paying")

    client = razorpay.Client(auth=("rzp_test_CUCNWEytRu04a5", "0oeN6h68TptSe8iFmKRo7L3F"))

    DATA = {
        "amount": 5000,
        "currency": "INR",
        "payment_capture":0,
        }
    client=razorpay.Client(auth=('rzp_test_CUCNWEytRu04a5','0oeN6h68TptSe8iFmKRo7L3F'))
    order=client.order.create(data=DATA)
    orderr=order['id']
    print(orderr)
    print("your order is ",order)
    myuser=ouruser.objects.filter(username=userr)
    b=ouruser.objects.get(username=userr)
    c=b.counter
    return render(request,'myapp/home_dashboard.html',{",userr":u,"count":c,"payment":orderr,"obj":obj,"myu":myuser})

def ctwelve(request):
    user=request.session.get('us',None)
    obj=twelveth.objects.all()
    c = request.session.get('c', None)
    a=ouruser.objects.get(username=user)
    c=a.counter
    myuser=ouruser.objects.filter(username=user)
    return render(request,'myapp/home2_dashboard.html',{"count":c,"obj":obj,"myu":myuser})

def fetch(request):
    if request.method=="POST":
        print("hello")
        var=order()
        var.order_id=request.POST.get('order_id')
        var.title=request.POST.get('title')
        print(var.order_id)
        var.save()
        return HttpResponse("<h1> Success </h1>")


def remove(request):
    if request.method=="POST":
        chapter=request.POST.get('chapter')
        user=request.session.get('us',None)
        u=ouruser.objects.get(username=user)
        u.counter=u.counter-1
        u.save()
        cart=mycart.objects.get(username=user)
        try:
            el=eleventh.objects.get(chapter_name=chapter)
            cart.eleven.remove(el)
            cart.save()
        except Exception as e:
            tw=twelveth.objects.get(chapter_name=chapter)
            cart.twelve.remove(tw)
            cart.save()
    return redirect('cart')

def dpdf(request):
    if request.method=="POST":
        chapter=request.POST.get('pdf')
        chapter_video=request.POST.get('video')
        chapter_shorts=request.POST.get('shorts')
        try:
            pdf.objects.get(chapter_name=chapter)
            p=pdf.objects.get(chapter_name=chapter)
            print(p.status)
            u=p.pdf.url
            return render(request,'myapp/demo.html',{"url":u})
        except Exception as e:
            print(e)
        try:
            if(video.objects.get(chapter_name=chapter_video)):
                p=video.objects.get(chapter_name=chapter_video)
                url=p.video.url
                return render(request,'myapp/demo.html',{"url":url})
        except Exception as e:
            print(e)
        try:
                short_video.objects.get(chapter_name=chapter_shorts)
                p=short_video.objects.get(chapter_name=chapter_shorts)
                urll=p.video.url
                return render(request,'myapp/demo.html',{"url":urll})
        except Exception as e:
            print(e)
        return HttpResponse("No data found")


# Create your views here.

