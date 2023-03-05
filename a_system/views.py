from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from api.models import *

# Create your views here.


def adminLoginPage(request):
    status=''
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            if User.objects.get(username=username).is_superuser:
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                    status='Username Or Password Is Wrong'
            else:
                status='wrong admin username'
                data={
                    'status':status
                }
                return render(request,'normal_pages/login.html',data)
        except:
            status='Username Or Password Is Wrong'
    data={
        'status':status
    }
    return render(request,'normal_pages/login.html',data)

def adminLogoutPage(request):
    logout(request)
    return HttpResponseRedirect('/login/')










@login_required(login_url='/login/')
def dashboard(request):
    subscribedUser=UserProfile.objects.filter(isSubscribedUser=True)
    normalUsers=UserProfile.objects.filter(isSubscribedUser=False)
    prodcuts=ProductInfo.objects.all()
    orders=OrderedProduct.objects.all()
    return render(request,'normal_pages/dashboard.html',{'prodcuts':prodcuts,'orders':orders,'subscribedUser':subscribedUser,'normalUsers':normalUsers})

# about questions
@login_required(login_url='/login/')
def questionMgn(request):
    questions=ProbQuestion.objects.all().order_by('-probQuestionCategory')
    productCategory=ProductCategory.objects.all()
    productsInfo=ProductInfo.objects.all().order_by('-category')
    adkarWithTaloyin=AdkarWithTalo.objects.all()
    questionCategorys=ProbQuestionCategory.objects.all()

    return render(request,'reg_mang/questions_mgn.html',{'questionCategorys':questionCategorys,'productCategory':productCategory,'questions':questions,'adkarWithTaloyin':adkarWithTaloyin,'productsInfo':productsInfo})

@login_required(login_url='/login/')
def adkarWithTaloMgn(request):
    adkarWithTaloyin=AdkarWithTalo.objects.all()
    adkarCount=AdkarWithTalo.objects.filter(isAdkar=True)
    taloCount=AdkarWithTalo.objects.filter(isAdkar=False)
    return render(request,'reg_mang/adkar_with_talo.html',{'adkarCount':adkarCount,'taloCount':taloCount,'adkarWithTaloyin':adkarWithTaloyin})


@login_required(login_url='/login/')
def listeningQuranClMng(request):
    shikhsCategory=ShikhCategory.objects.all().order_by('-isHero')
    listeningCilajWithQuran=ListeningCilajWithQuran.objects.all().order_by('theShikh')
    return render(request,'reg_mang/listening_quran_cl_mng.html',{'shikhsCategory':shikhsCategory,'listeningCilajWithQuran':listeningCilajWithQuran})






# USERS-PROFILE
@login_required(login_url='/login/')
def usersList(request):
    usersInfo=UserProfile.objects.all()
    subscribedUsers=UserProfile.objects.filter(isSubscribedUser=True).all().count()
    unSubscribedUsers=usersInfo.count() - subscribedUsers
    return render(request,'reg_mang/users_list.html',{'usersInfo':usersInfo,'unSubscribedUsers':unSubscribedUsers,'subscribedUsers':subscribedUsers})
# USERS-PROFILE
@login_required(login_url='/login/')
def userDetail(request,pk):
    userInfo=UserProfile.objects.get(pk=pk)
    
    userProbAnswers=ProbAnswer.objects.filter(theUser=userInfo)
    userOrderedProducts=OrderedProduct.objects.filter(theUser=userInfo)
    unTakedOrders=OrderedProduct.objects.filter(theUser=userInfo,userTaked=False)
    completeOrders=OrderedProduct.objects.filter(theUser=userInfo,status='completed')
    userProductsRoutine=UserProductsRoutine.objects.filter(theUser=userInfo)
    doctorAppointments=DoctorAppointment.objects.filter(theUser=userInfo)
    bugProducts=ProductsInTheBug.objects.filter(theUser=userInfo).filter(isTaked=False)
    userAnswerInformation = UserAnswerInformation.objects.filter(theUser=userInfo)
    myChilds = UserChildAnswerInformation.objects.filter(theUser=userInfo)
    childCounts=myChilds.distinct('theChild').count()
    routineTimes=RoutineTime.objects.all()
    return render(request,'reg_mang/user_detail.html',{'completeOrders':completeOrders,'unTakedOrders':unTakedOrders,'myChilds':myChilds,'childCounts':childCounts,'userAnswerInformation':userAnswerInformation,'bugProducts':bugProducts,'doctorAppointments':doctorAppointments,'routineTimes':routineTimes,'userOrderedProducts':userOrderedProducts,'userProductsRoutine':userProductsRoutine,'userInfo':userInfo,'userProbAnswers':userProbAnswers})





# products 
@login_required(login_url='/login/')
def productCreate(request):
    productCategory=ProductCategory.objects.all()
    return render(request,'reg_mang/product_create.html',{'productCategory':productCategory})

@login_required(login_url='/login/')
def productsList(request):
    productsInfo=ProductInfo.objects.all()
    return render(request,'reg_mang/product_list.html',{'productsInfo':productsInfo})

@login_required(login_url='/login/')
def orderedList(request):
    orderedProducts=OrderedProduct.objects.filter(userTaked=False).order_by('-userTaked')
    takedProducts=OrderedProduct.objects.filter(userTaked=True).all()
    untakedOrders=OrderedProduct.objects.filter(userTaked=False)
    
    return render(request,'reg_mang/ordered_list.html',{'takedProducts':takedProducts,'orderedProducts':orderedProducts,'untakedOrders':untakedOrders})


@login_required(login_url='/login/')
def appInfo(request):
    appInformation=ProductInfo.objects.all()
    return render(request,'normal_pages/app_info.html',{'appInfo':appInformation})


@login_required(login_url='/login/')
def appointmentList(request):
    upcomingAppointments=DoctorAppointment.objects.filter(sessionEnded=False).all()
    endedAppointments=DoctorAppointment.objects.filter(sessionEnded=True).all()
    return render(request,'reg_mang/appointment_list.html',{'upcomingAppointments':upcomingAppointments,'endedAppointments':endedAppointments})


@login_required(login_url='/login/')
def appointmentDetail(request,appointId):
    theAppointment=DoctorAppointment.objects.get(pk=appointId)
    userProbAnswers=ProbAnswer.objects.filter(theUser=theAppointment.theUser)
    return render(request,'reg_mang/appointment_detail.html',{'userProbAnswers':userProbAnswers,'theAppointment':theAppointment})




# users
@login_required(login_url='/login/')
def allUsers(request):
    users=UserProfile.objects.all()
    return render(request,'manage/all-users.html',{'users':users})








