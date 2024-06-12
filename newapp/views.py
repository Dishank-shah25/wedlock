from django.shortcuts import render , redirect
from .models import submit
# Create your views here.
def index(request):
    return render(request,'index.html')
def element(request):
    useremail = request.POST.get("email address")
    userpassword = request.POST.get("password")
    userrepass = request.POST.get("repassword")
    userselect = request.POST.get("select")
    userfirstname = request.POST.get("username")
    userlastname = request.POST.get("lusername")
    usergender = request.POST.get("gender")
    userfgender = request.POST.get("fgender")
    userreligion = request.POST.get("religion")
    userlanguage2 = request.POST.get("userlanguage")

    insert =submit(email=useremail,password=userpassword,repassword=userrepass,person_select=userselect,firstname=userfirstname,lastname=userlastname,gender=usergender,fgender=userfgender,religion=userreligion,language=userlanguage2)
    insert.save()

    return redirect('table')

def table(request):
    viewers = submit.objects.all()
    print(viewers)
    context = {
        "allindex": viewers
    }
    return render(request,'table.html',context)
