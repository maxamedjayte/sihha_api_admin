from rest_framework.response import Response
import json
from api.serializers import *
from django.shortcuts import render,redirect
import requests
from shiffa_app import settings
from decouple import config
from rest_framework.decorators import api_view
from datetime import datetime

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os
import random
from decouple import config
from twilio.rest import Client 
# Create your views here.

# userprofiles data
@api_view(['GET'])
def userProfileList(request):
    objects=UserProfile.objects.all()
    serializer=UserProfileSerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def userProfileCreate(request):
    serializer=UserProfileCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def userProfileUpdate(request,pk):
    theObject=UserProfile.objects.get(pk=pk)
    serializer=UserProfileCreateSerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        theObject=UserProfile.objects.get(pk=pk)
        serializer=UserProfileSerializer(theObject,many=False)
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def userProfileDelete(request,pk):
    theObject=UserProfile.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def userProfileDetail(request,pk):
    theObject=UserProfile.objects.get(pk=pk)
    serializer=UserProfileSerializer(theObject,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def userLoginPr(request,number,password):
    theUser=UserProfile.objects.filter(number=number,password=password)
    if theUser.exists():
        serializer=UserProfileSerializer(theUser.first(),many=False)
        return Response({'isExist':True,'userInfo':serializer.data})
    else:
        if UserProfile.objects.filter(number=number).exists():
            return Response({'message':'user password was incrrect','isExist':False,'userInfo':''})
        else:
            return Response({'message':'username was not registred','isExist':False,'userInfo':''})

@api_view(['POST'])
def userLogin(request):
    number=request.data['number']
    password=request.data['password']
    theUser=UserProfile.objects.filter(number=number,password=password)
    if theUser.exists():
        serializer=UserProfileSerializer(theUser.first(),many=False)
        return Response({'isExist':True,'userInfo':serializer.data})
    else:
        if UserProfile.objects.filter(number=number).exists():
            return Response({'message':'user password was incrrect','isExist':False,'userInfo':''})
        else:
            return Response({'message':'username was not registred','isExist':False,'userInfo':''})




@api_view(['GET'])
def checkUserExist(request,number):
    userr=UserProfile.objects.filter(number=number).exists()
    return Response({'isExist':userr})





@api_view(['GET'])
def appInfoData(request):
    theObject=AppInformation.objects.first()
    serializer=AppInformationSerializer(theObject,many=False)
    return Response(serializer.data)







def countTheQuestionCateg():
    quesCount=0
    for qCat in ProbQuestionCategory.objects.all():
        quesCount=ProbQuestion.objects.filter(probQuestionCategory=qCat.pk).count()
        qCat.questionsCount=quesCount
        qCat.save()






# userprofile
@api_view(['GET'])
def probQuestionList(request):
    countTheQuestionCateg()
    objects=ProbQuestion.objects.all()
    serializer=ProbQuestionSerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def probQuestionCreate(request):
    serializer=ProbQuestionCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def probQuestionUpdate(request,pk):
    theObject=ProbQuestion.objects.get(pk=pk)
    serializer=ProbQuestionCreateSerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def probQuestionDelete(request,pk):
    theObject=ProbQuestion.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def probQuestionDetail(request,pk):
    theObject=ProbQuestion.objects.get(pk=pk)
    serializer=ProbQuestionSerializer(theObject,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def checkThisQusetionExist(request,question):
    exists=ProbQuestion.objects.filter(title=question).exists()
    # serializer=ClasseSerializer(classe,many=True)
    return Response({'isExist':exists})







@api_view(['GET'])
def probAnswerList(request):
    countTheQuestionCateg()
    objects=ProbAnswer.objects.all()
    serializer=ProbAnswerSerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def probAnswerCreate(request):
    serializer=ProbAnswerCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def probAnswerUpdate(request,pk):
    theObject=ProbAnswer.objects.get(pk=pk)
    serializer=ProbAnswerCreateSerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def probAnswerDelete(request,pk):
    theObject=ProbAnswer.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def probAnswerDetail(request,pk):
    theObject=ProbAnswer.objects.get(pk=pk)
    serializer=ProbAnswerSerializer(theObject,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def thisUserProbAnswerList(request,userId):
    countTheQuestionCateg()
    theObjects=ProbAnswer.objects.filter(theUser=userId)
    serializer=ProbAnswerSerializer(theObjects,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def probAnswerAssigning(request,theQuestion,theUser,theAnswer):
    theProbAnswer=ProbAnswer.objects.filter(theProbQuestion=theQuestion,theUser=theUser)
    if theProbAnswer.exists():
        serializer=ProbAnswerSerializer(theProbAnswer.first(),many=False)
        theProbAnswer.update(answer=True if theAnswer==1 else False)
        # theProbAnswer.save()
        return Response({'exists':True,'theAnswer':serializer.data})
    else:
        theRegistredAnswer=ProbAnswer.objects.create(
            theProbQuestion=ProbQuestion.objects.get(pk=theQuestion),
            theUser=UserProfile.objects.get(pk=theUser),
            answer=True if theAnswer==1 else False
        )
        serializer=ProbAnswerSerializer(theRegistredAnswer,many=False)
        return Response({'exists':True,'theAnswer':serializer.data})









@api_view(['GET'])
def childProbAnswerList(request):
    countTheQuestionCateg()
    objects=ChildProbAnswer.objects.all()
    serializer=ChildProbAnswerSerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def childProbAnswerCreate(request):
    serializer=ChildProbAnswerCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def childProbAnswerUpdate(request,pk):
    theObject=ChildProbAnswer.objects.get(pk=pk)
    serializer=ChildProbAnswerCreateSerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def childProbAnswerDelete(request,pk):
    theObject=ChildProbAnswer.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def childProbAnswerDetail(request,pk):
    theObject=ChildProbAnswer.objects.get(pk=pk)
    serializer=ChildProbAnswerSerializer(theObject,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def thisUserChildProbAnswer(request,theUser):
    countTheQuestionCateg()
    theObjects=ChildProbAnswer.objects.filter(theUser=theUser)
    serializer=ChildProbAnswerSerializer(theObjects,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def childProbAnswerAssigning(request,theQuestion,theUser,theChild,theAnswer):
    theProbAnswer=ChildProbAnswer.objects.filter(theProbQuestion=theQuestion,theUser=theUser,theChild=theChild)
    if theProbAnswer.exists():
        serializer=ChildProbAnswerSerializer(theProbAnswer.first(),many=False)
        theProbAnswer.update(answer=True if theAnswer==1 else False)
        # theProbAnswer.save()
        return Response({'exists':True,'theAnswer':serializer.data})
    else:
        theRegistredAnswer=ChildProbAnswer.objects.create(
            theProbQuestion=ProbQuestion.objects.get(pk=theQuestion),
            theChild=theChild,
            theUser=UserProfile.objects.get(pk=theUser),
            answer=True if theAnswer==1 else False
        )
        serializer=ChildProbAnswerSerializer(theRegistredAnswer,many=False)
        return Response({'exists':True,'theAnswer':serializer.data})





@api_view(['GET'])
def userChildAdkarWithProductList(request):
    countTheQuestionCateg()
    objects=UserChildAdkarWithProduct.objects.all()
    serializer=UserChildAdkarWithProductSerializers(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def userChildAdkarWithProductCreate(request):
    serializer=UserChildAdkarWithProductSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def userChildAdkarWithProductUpdate(request,pk):
    theObject=UserChildAdkarWithProduct.objects.get(pk=pk)
    serializer=UserChildAdkarWithProductSerializers(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def userChildAdkarWithProductDelete(request,pk):
    theObject=UserChildAdkarWithProduct.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def userChildAdkarWithProductDetail(request,pk):
    theObject=UserChildAdkarWithProduct.objects.get(pk=pk)
    serializer=UserChildAdkarWithProductSerializers(theObject,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def thisUserChildAdkarWithProduct(request,theUser,theChild):
    countTheQuestionCateg()
    theObjects=UserChildAdkarWithProduct.objects.filter(theUser=theUser)
    serializer=UserChildAdkarWithProductSerializers(theObjects,many=True)
    return Response(serializer.data)


























@api_view(['GET'])
def productsInTheBugList(request):
    countTheQuestionCateg()
    objects=ProductsInTheBug.objects.all()
    serializer=ProductsInTheBugSerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def productsInTheBugCreate(request):
    serializer=ProductsInTheBugCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def productsInTheBugUpdate(request,pk):
    theObject=ProductsInTheBug.objects.get(pk=pk)
    serializer=ProductsInTheBugCreateSerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def productsInTheBugDelete(request,pk):
    theObject=ProductsInTheBug.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def productsInTheBugDetail(request,pk):
    theObject=ProductsInTheBug.objects.get(pk=pk)
    serializer=ProductsInTheBugSerializer(theObject,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def thisUserProductsInTheBugList(request,userId):
    theObjects=ProductsInTheBug.objects.filter(theUser=userId)
    serializer=ProductsInTheBugSerializer(theObjects,many=True)
    return Response(serializer.data)


    








# adkarWithTalo
@api_view(['GET'])
def adkarWithTaloList(request):
    objects=AdkarWithTalo.objects.all()
    serializer=AdkarWithTaloSerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def adkarWithTaloCreate(request):
    serializer=AdkarWithTaloCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def adkarWithTaloUpdate(request,pk):
    theObject=AdkarWithTalo.objects.get(pk=pk)
    serializer=AdkarWithTaloCreateSerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def adkarWithTaloDelete(request,pk):
    theObject=AdkarWithTalo.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def adkarWithTaloDetail(request,pk):
    theObject=AdkarWithTalo.objects.get(pk=pk)
    serializer=AdkarWithTaloSerializer(theObject,many=False)
    return Response(serializer.data)














# productInfo
@api_view(['GET'])
def productInfoList(request):
    objects=ProductInfo.objects.all()
    serializer=ProductInfoSerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def productInfoCreate(request):
    serializer=ProductInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def productInfoUpdate(request,pk):
    theObject=ProductInfo.objects.get(pk=pk)
    serializer=ProductInfoSerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def productInfoDelete(request,pk):
    theObject=ProductInfo.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def productInfoDetail(request,pk):
    theObject=ProductInfo.objects.get(pk=pk)
    serializer=ProductInfoSerializer(theObject,many=False)
    return Response(serializer.data)









# productInfo
@api_view(['GET'])
def productCategoryList(request):
    objects=ProductCategory.objects.all()
    serializer=ProductCategorySerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def productCategoryCreate(request):
    serializer=ProductCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def productCategoryUpdate(request,pk):
    theObject=ProductCategory.objects.get(pk=pk)
    serializer=ProductCategorySerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def productCategoryDelete(request,pk):
    theObject=ProductCategory.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def productCategoryDetail(request,pk):
    theObject=ProductCategory.objects.get(pk=pk)
    serializer=ProductCategorySerializer(theObject,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def thisCategoryProductsList(request,catId):
    theObject=ProductInfo.objects.filter(category=catId)
    serializer=ProductInfoSerializer(theObject,many=True)
    return Response(serializer.data)




# productInfo
@api_view(['GET'])
def probQuestionCategoryList(request):
    countTheQuestionCateg()
    objects=ProbQuestionCategory.objects.all()
    serializer=ProbQuestionCategorySerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def probQuestionCategoryCreate(request):
    serializer=ProbQuestionCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def probQuestionCategoryUpdate(request,pk):
    theObject=ProbQuestionCategory.objects.get(pk=pk)
    serializer=ProbQuestionCategorySerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def probQuestionCategoryDelete(request,pk):
    theObject=ProductCategory.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def probQuestionCategoryDetail(request,pk):
    theObject=ProbQuestionCategory.objects.get(pk=pk)
    serializer=ProbQuestionCategorySerializer(theObject,many=False)
    return Response(serializer.data)









# productInfo
@api_view(['GET'])
def orderedProductList(request):
    objects=OrderedProduct.objects.all()
    serializer=OrderedProductSerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def orderedProductCreate(request):
    serializer=OrderedProductCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def orderedProductUpdate(request,pk):
    theObject=OrderedProduct.objects.get(pk=pk)
    serializer=OrderedProductSerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def orderedProductDelete(request,pk):
    theObject=OrderedProduct.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def orderedProductDetail(request,pk):
    theObject=OrderedProduct.objects.get(pk=pk)
    serializer=OrderedProductSerializer(theObject,many=False)
    return Response(serializer.data)



@api_view(['GET'])
def orderedProductThisUser(request,pk):
    theObject=OrderedProduct.objects.filter(theUser=UserProfile.objects.get(pk=pk))
    serializer=OrderedProductSerializer(theObject,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def changeOrderStatus(request,orderId,status):
    theOrder=OrderedProduct.objects.get(pk=orderId)
    theOrder.status=status
    theOrder.userTakedTime=datetime.now()
    theOrder.save()
    return Response({'status':theOrder.status})







# appoint cat
@api_view(['GET'])
def doctorAppointmentList(request):
    objects=DoctorAppointment.objects.all()
    serializer=DoctorAppointmentSerializers(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def doctorAppointmentCreate(request):
    serializer=OrderedProductCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def doctorAppointmentUpdate(request,pk):
    theObject=DoctorAppointment.objects.get(pk=pk)
    serializer=DoctorAppointmentSerializers(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def doctorAppointmentDelete(request,pk):
    theObject=DoctorAppointment.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def doctorAppointmentDetail(request,pk):
    theObject=DoctorAppointment.objects.get(pk=pk)
    serializer=DoctorAppointmentSerializers(theObject,many=False)
    return Response(serializer.data)



@api_view(['GET'])
def doctorAppointmentThisUser(request,pk):
    theObject=DoctorAppointment.objects.filter(theUser=UserProfile.objects.get(pk=pk))
    serializer=DoctorAppointmentSerializers(theObject,many=True)
    return Response(serializer.data)







# appoint cat
@api_view(['GET'])
def appointmentCategoryList(request):
    objects=AppointmentCategory.objects.all()
    serializer=AppointmentCategorySerializers(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def appointmentCategoryCreate(request):
    serializer=AppointmentCategorySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def appointmentCategoryUpdate(request,pk):
    theObject=AppointmentCategory.objects.get(pk=pk)
    serializer=AppointmentCategorySerializers(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def appointmentCategoryDelete(request,pk):
    theObject=AppointmentCategory.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def appointmentCategoryDetail(request,pk):
    theObject=AppointmentCategory.objects.get(pk=pk)
    serializer=AppointmentCategorySerializers(theObject,many=False)
    return Response(serializer.data)






# productInfo
@api_view(['GET'])
def userProductsRoutineList(request):
    objects=UserProductsRoutine.objects.all()
    serializer=UserProductsRoutineSerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def userProductsRoutineCreate(request):
    serializer=UserProductsRoutineCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def userProductsRoutineUpdate(request,pk):
    theObject=UserProductsRoutine.objects.get(pk=pk)
    serializer=UserProductsRoutineCreateSerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def userProductsRoutineDelete(request,pk):
    theObject=UserProductsRoutine.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def userProductsRoutineDetail(request,pk):
    theObject=UserProductsRoutine.objects.get(pk=pk)
    serializer=UserProductsRoutineSerializer(theObject,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def checkRoutineProductForThisUserExist(request,theProduct,theUser):
    theObject=UserProductsRoutine.objects.filter(theProduct=theProduct).filter(theUser=theUser)
    if theObject.exists():
        serializer=UserProductsRoutineSerializer(UserProductsRoutine.objects.filter(theProduct=theProduct).get(theUser=theUser),many=False)
        return Response({'exist':True,'data':serializer.data})
    else:
        return Response({'exist':False})

@api_view(['GET'])
def thisUserProductRoutineList(request,userId):
    theObject=UserProductsRoutine.objects.filter(theUser=userId)
    serializer=UserProductsRoutineSerializer(theObject,many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def orderedProductThisUser(request,pk):
#     theObject=OrderedProduct.objects.filter(theUser=UserProfile.objects.get(pk=pk))
#     serializer=OrderedProductSerializer(theObject,many=False)
#     return Response(serializer.data)
















# listeningCilajWithQuran
@api_view(['GET'])
def listeningCilajWithQuranList(request):
    objects=ListeningCilajWithQuran.objects.all()
    serializer=ListeningCilajWithQuranSerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def listeningCilajWithQuranCreate(request):
    serializer=ListeningCilajWithQuranCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def listeningCilajWithQuranUpdate(request,pk):
    theObject=ListeningCilajWithQuran.objects.get(pk=pk)
    serializer=ListeningCilajWithQuranCreateSerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def listeningCilajWithQuranDelete(request,pk):
    theObject=ListeningCilajWithQuran.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def listeningCilajWithQuranDetail(request,pk):
    theObject=ListeningCilajWithQuran.objects.get(pk=pk)
    serializer=ListeningCilajWithQuranSerializer(theObject,many=False)
    return Response(serializer.data)

# @api_view(['GET'])
# def orderedProductThisUser(request,pk):
#     theObject=OrderedProduct.objects.filter(theUser=UserProfile.objects.get(pk=pk))
#     serializer=OrderedProductSerializer(theObject,many=False)
#     return Response(serializer.data)








# listeningCilajWithQuran
@api_view(['GET'])
def shikhCategoryList(request):
    objects=ShikhCategory.objects.all().order_by('-isHero')
    serializer=ShikhCategorySerializer(objects,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def shikhCategoryCreate(request):
    serializer=ShikhCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def shikhCategoryUpdate(request,pk):
    theObject=ShikhCategory.objects.get(pk=pk)
    serializer=ShikhCategorySerializer(instance=theObject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def shikhCategoryDelete(request,pk):
    theObject=ShikhCategory.objects.get(pk=pk)
    theObject.delete()
    return Response()

@api_view(['GET'])
def shikhCategoryDetail(request,pk):
    theObject=ShikhCategory.objects.get(pk=pk)
    serializer=ShikhCategorySerializer(theObject,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def thisShikhListeningList(request,shikhId):
    theObject=ListeningCilajWithQuran.objects.filter(theShikh=shikhId)
    serializer=ListeningCilajWithQuranSerializer(theObject,many=True)
    return Response(serializer.data)








@api_view(['GET'])
def guessTheUserChildPian(request,userId,theChild):
    probQuestionCategorys=ProbQuestionCategory.objects.all()
    thisUserProbAnswers=ChildProbAnswer.objects.filter(theUser=UserProfile.objects.get(pk=userId)).filter(theChild=theChild)
    
    for questionCat in probQuestionCategorys:
        trueAnswers = 0
        falseAnswers = 0
        for theUserAnswer in thisUserProbAnswers:
            if questionCat.pk == theUserAnswer.theProbQuestion.probQuestionCategory.pk:
                if theUserAnswer.answer:
                    trueAnswers=trueAnswers+1
                else:
                    falseAnswers=falseAnswers+1
        if UserChildAnswerInformation.objects.filter(theUser=UserProfile.objects.get(pk=userId)).filter(thePorbQuestionCategory=questionCat).filter(theChild=theChild).exists():
            UserChildAnswerInformation.objects.filter(theUser=UserProfile.objects.get(pk=userId)).filter(thePorbQuestionCategory=questionCat).filter(theChild=theChild).update(trueAnswers=trueAnswers,falseAnswers=falseAnswers)
        else:
            UserChildAnswerInformation.objects.create(
                theUser=UserProfile.objects.get(pk=userId),
                theChild=theChild,
                thePorbQuestionCategory=questionCat,
                trueAnswers=trueAnswers,
                falseAnswers=falseAnswers   
                )
            
            
    theUserInformation=UserChildAnswerInformation.objects.filter(theUser=UserProfile.objects.get(pk=userId)).filter(theChild=theChild)
    guessedInformationSerialized=UserChildAnswerInformationSerializers(theUserInformation,many=True)
    return Response(guessedInformationSerialized.data)










@api_view(['GET'])
def guessTheUserPian(request,userId):
    probQuestionCategorys=ProbQuestionCategory.objects.all()
    thisUserProbAnswers=ProbAnswer.objects.filter(theUser=UserProfile.objects.get(pk=userId))
    
    for questionCat in probQuestionCategorys:
        trueAnswers = 0
        falseAnswers = 0
        for theUserAnswer in thisUserProbAnswers:
            if questionCat.pk == theUserAnswer.theProbQuestion.probQuestionCategory.pk:
                if theUserAnswer.answer:
                    trueAnswers=trueAnswers+1
                else:
                    falseAnswers=falseAnswers+1
        if UserAnswerInformation.objects.filter(theUser=UserProfile.objects.get(pk=userId)).filter(thePorbQuestionCategory=questionCat).exists():
            print('exist')
            UserAnswerInformation.objects.filter(theUser=UserProfile.objects.get(pk=userId)).filter(thePorbQuestionCategory=questionCat).update(trueAnswers=trueAnswers,falseAnswers=falseAnswers)
        else:
            print('created')
            UserAnswerInformation.objects.create(
                theUser=UserProfile.objects.get(pk=userId),
                thePorbQuestionCategory=questionCat,
                trueAnswers=trueAnswers,
                falseAnswers=falseAnswers   
                )
    theUserInformation=UserAnswerInformation.objects.filter(theUser=UserProfile.objects.get(pk=userId))
    guessedInformationSerialized=UserAnswerInformationSerializers(theUserInformation,many=True)
    return Response(guessedInformationSerialized.data)

@api_view(['GET'])
def generateCilajToTheUserChild(request,userId,theChild):
    theUserInfo=UserProfile.objects.get(pk=userId)
    theChildAdkarWithTalo=UserChildAdkarWithProduct.objects.filter(theUser=theUserInfo).filter(theChild=theChild)
    if(theChildAdkarWithTalo.exists() == False):
        theChildAdkarWithTalo=UserChildAdkarWithProduct.objects.create(
            theUser=theUserInfo,
            theChild=theChild
        )
    else:
        theChildAdkarWithTalo = theChildAdkarWithTalo.first()
    probChildAnswers=ChildProbAnswer.objects.filter(theUser=theUserInfo,theChild=theChild)
    for theAns in probChildAnswers:
        if theAns.answer:
            theChildAdkarWithTalo.childMatchedAdkarWithTalo.set(theAns.theProbQuestion.isTrueAdkarWithTaloyin.all())
            theChildAdkarWithTalo.theProducts.set(theAns.theProbQuestion.isTrueProducts.all())
            for relProduct in theAns.theProbQuestion.isTrueProducts.all():
                if ProductsInTheBug.objects.filter(theUser=theUserInfo,theProduct=relProduct).exists() == False:
                    ProductsInTheBug.objects.create(
                        theUser=theUserInfo,
                        theProduct=relProduct,
                        isTaked=False
                    )
                else:
                    productsInTheBug=ProductsInTheBug.objects.filter(theUser=theUserInfo).filter(theProduct=relProduct).first()
                    productsInTheBug.isTaked=False
                    productsInTheBug.save()

    return Response({'guessedUserInformation':'guessedUserInformation'})


@api_view(['GET'])
def generateCilajToTheUser(request,userId):
    theUserInfo=UserProfile.objects.get(pk=userId)
    probAnswers=ProbAnswer.objects.filter(theUser=theUserInfo)
    # guessedUserInformation=guessTheUserPian(request,userId)
    for theAns in probAnswers:
        if theAns.answer:
            theUserInfo.userMatchedAdkarWithTalo.set(theAns.theProbQuestion.isTrueAdkarWithTaloyin.all())
            for relProduct in theAns.theProbQuestion.isTrueProducts.all():
                if UserProductsRoutine.objects.filter(theUser=theUserInfo).filter(theUser=theUserInfo).exists() == False:
                    rtnUserProduct= UserProductsRoutine.objects.create(
                        theUser=theUserInfo,
                        theProduct=relProduct
                    )
                    for productUsageTime in relProduct.theUsageTimes.all():
                        rtnUserProduct.usageTimes.add(productUsageTime)
                        rtnUserProduct.save()
                    if ProductsInTheBug.objects.filter(theUser=theUserInfo,theProduct=relProduct).exists() == False:
                        ProductsInTheBug.objects.create(
                            theUser=theUserInfo,
                            theProduct=relProduct,
                            isTaked=False
                        )
                    else:
                        productsInTheBug=ProductsInTheBug.objects.filter(theUser=theUserInfo).filter(theProduct=relProduct).first()
                        productsInTheBug.isTaked=False
                        productsInTheBug.save()
                else:
                    rtnUserProduct=UserProductsRoutine.objects.filter(theUser=theUserInfo).filter(theUser=theUserInfo).first()
                    # rtnUserProduct.usageTimes.set(relProduct.theUsageTimes.all())
                    for productUsageTime in relProduct.theUsageTimes.all():
                        rtnUserProduct.usageTimes.add(productUsageTime)
                        rtnUserProduct.save()
    thisUserProductRoutine = UserProductsRoutine.objects.filter(theUser=theUserInfo)
    thisUserMatchedAdkarWithTalo = theUserInfo.userMatchedAdkarWithTalo
    return Response({'guessedUserInformation':'guessedUserInformation'})


@api_view(['POST'])
def merchantPaidApi(request,paymentType,itemType):
    fullResp=''
    orderInfo=''
    usrId=request.data['userId']
    usrNumber=request.data['number']
    usrMoney=request.data['money']
    if paymentType == 'eDahab':
        if itemType == 'product':
            theProduct=request.data['products']
            print(theProduct)
            paidResp=waafiPaidMoney(usrNumber,usrMoney,'')
            if paidResp['paided']:
                print('user paided')
            else:
                print('user not paided')
        elif itemType=='subscription':
            print('is subcsription')
        else:
            print('is doctor apoint')
    else:
        if itemType == 'product':
            productsInfo=request.data['products']
            paidResp=waafiPaidMoney(usrNumber,usrMoney,'')
            if paidResp['paided']:
                for theProduct in productsInfo:
                    OrderedProduct.objects.create(
                        theUser=UserProfile.objects.get(pk=usrId),
                        theProductInfo=ProductInfo.objects.get(pk=theProduct['id']),
                        quantity=int(theProduct['quantity']),
                        paidedMoney=float(usrMoney),
                        paymentMethod=paymentType
                    )
                fullResp={'paided':True,'status':'success','productOrdred':True}
                orderInfo='products not ordered'
            else:
                fullResp={'paided':True,'status':'failded','productOrdred':False}
                
        elif itemType=='subscription':
            userInfo= UserProfile.objects.filter(pk=usrId)
            userInfo.latestSbscriptionDateFrom=datetime.now()
            userInfo.latestSbscriptionDateTo=datetime.now() + timedelta(days=30)
            userInfo.isSubscribedUser=True
            userInfo.subscriptionActive=True
            userInfo.is_activate=True
            paidResp=waafiPaidMoney(usrNumber,usrMoney,'CABDALLA')
            if paidResp['paided']:
                userInfo.save()
                fullResp={'paided':True,'status':'success','subscriptActivated':True,'fromDate':userInfo.latestSbscriptionDateFrom,'toDate':userInfo.latestSbscriptionDateTo}
            else:
                fullResp={'paided':False,'status':'failed','subscriptActivated':False}
        else:
            theCategory=request.data['theCategory']
            # userAssignedDated=request.data['userAssignedDated']
            if DoctorAppointment.objects.filter(sessionEnded=False).filter(theUser=UserProfile.objects.get(pk=usrId)).filter(theCategory=AppointmentCategory.objects.get(pk=theCategory)).exists():
                fullResp={'paided':True,'status':'success','isExist':True,'appointmentCreated':False}
            else:
                paidResp=waafiPaidMoney(usrNumber,usrMoney,'')
                print(paidResp)
                if paidResp['paided']:
                    try:
                        DoctorAppointment.objects.create(
                            theUser=UserProfile.objects.get(pk=usrId),
                            theCategory=AppointmentCategory.objects.get(pk=theCategory),
                        )
                        print('at try')
                        fullResp={'paided':True,'status':'success','isExist':False,'appointmentCreated':True}
                    except:
                        # DoctorAppointment.objects.create(
                        #     theUser=UserProfile.objects.get(pk=usrId),
                        #     theCategory=AppointmentCategory.objects.get(pk=theCategory),
                        # )
                        print('user paided is except')
                        fullResp={'paided':True,'status':'failded','appointmentCreated':False}
                else:
                    fullResp={'status':'failed','appointmentCreated':False,'paided':False}
    return Response(fullResp)





@api_view(['GET'])
def searchProduct(request,searchKey):
    # resultProduct=ProductInfo.objects.filter(name__unaccent__lower__trigram_similar=searchKey)
    resultProduct=ProductInfo.objects.filter(name__icontains=searchKey)
    serializer=ProductInfoSerializer(resultProduct,many=True)
    return Response(serializer.data)

# bO6yp_WIrGYFoS_RXUeF_L7jRuEJv2kgFMFii1sQ

# ACfdff520a30544ca1530b2e8092dab448    sid

# 169100293d9eea3a51fb492630bb862d    token
@api_view(['GET'])
def sendOtpSMS(request,userNumber):
    # Download the helper library from https://www.twilio.com/docs/python/install
    # Set environment variables for your credentials
    # Read more at http://twil.io/secure
    api_key='293832-67745-11e5-88de-5600000c6b13'
    account_sid = config('ACCOUNT_SID')
    auth_token = config('AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    sendedNumber=str(random.randint(4,9000))
    message = client.messages.create(
                body='SIHHA-APP activation codeka :- '+str(sendedNumber) +' fadlan hala waadig qof kale',
                from_='+12708176406',
                to=userNumber
            )
    return Response({'sendedCode':sendedNumber})





@api_view(['POST'])
def sendAppointmentNot(request,email):
    status=400
    try:
        htmlText=request.data['htmlText']
        msg_html = render_to_string('booking_email.html', {'theHtmlText': htmlText})
        text_content = strip_tags(msg_html)
        emailStatus = EmailMultiAlternatives(
            'SIHHA BOOKING NOTIFICATION',
            text_content,
            'SIHHA APP '+settings.EMAIL_HOST_USER,
            [email],
        )
        emailStatus.attach_alternative(msg_html,"text/html")
        emailStatus.send()
        status=200
    except:
        status=100
        return Response({'sended':False})
    return Response({'sended':True})
    # msg_html = render_to_string('invoice/reset-password.html', {'theUserName': theUser.fullName.split(' ')[0],'sendedCode':(int(sendedCode)+len(email))})
    # text_content = ' Waxaa is soo diiwaangaliyay currentUser!.fullName asigoo dalbaday in uu lakulmo doctor faahfaahin deeri ah http://shiffa-app.up.railway.app/user_detail/currentUser.id/',
    # emailStatus = EmailMultiAlternatives(
    #     'Qaamuus Reset Password',
    #     text_content,
    #     'QAAMUUS ACADEMY '+settings.EMAIL_HOST_USER,
    #     [email],
    # )
    # emailStatus.send()
    # status=200

    
    # return Response({})




def waafiPaidMoney(usrNumber,usrMoney,paymentApiType):
    waafiConfig=WaafiMarchentConfig.objects.first()
    theJsonData={
        "schemaVersion": "1.0",
        "requestId": "10111331033",
        "timestamp": "client_timestamp",
        "channelName": "WEB",
        "serviceName": "API_PURCHASE",
        "serviceParams": {
            "merchantUid": waafiConfig.merchantUidCABDALLA if paymentApiType=='CABDALLA'  else waafiConfig.merchantUid,
            "apiUserId": waafiConfig.apiUserIdCABDALLA if paymentApiType=='CABDALLA'  else waafiConfig.apiUserId,
            "apiKey": waafiConfig.apiKeyCABDALLA if paymentApiType=='CABDALLA'  else waafiConfig.apiKey,
            "paymentMethod": "mwallet_account",
            "payerInfo": { "accountNo": '252'+usrNumber },
            "transactionInfo": {
                "referenceId": "12334",
                "invoiceId": "7896504",
                "amount": usrMoney,
                "currency": "USD",
                "description": "Test USD"
            }
        }
    }
    resp = requests.post('https://api.waafipay.net/asm',json=theJsonData,headers={ 'Content-type': 'application/json;charset=ISO-8859-1' })
    jsonPaidResp=json.loads(resp.text)
    if jsonPaidResp['responseCode']=='2001':
        return {'paided':True,'info':jsonPaidResp}
    else:
        return {'paided':False,'info':jsonPaidResp}

def eDahabPaidMoney(usrNumber,usrMoney):

    return Response({'paided':True})




        



# $.ajax({
#         method: "POST",
#         data: JSON.stringify({
#             "schemaVersion": "1.0",
#             "requestId": "10111331033",
#             "timestamp": "client_timestamp",
#             "channelName": "WEB",
#             "serviceName": "API_PURCHASE",
#             "serviceParams": {
#                 "merchantUid": "M0910332",
#                 "apiUserId": "1000527",
#                 "apiKey": "API-1620730280AHX",
#                 "paymentMethod": "mwallet_account",
#                 "payerInfo": { "accountNo": '252'+number },
#                 "transactionInfo": {
#                     "referenceId": "12334",
#                     "invoiceId": "7896504",
#                     "amount": money.toString(),
#                     "currency": "USD",
#                     "description": "Test USD"
#                 }
#             }
#         }),
#         headers: { 'Content-type': 'application/json;charset=ISO-8859-1' },
#         url: 'https://api.waafipay.net/asm',
#         success:async function (responseResp) {
#             if(responseResp.responseCode=='2001'){
#                 isPaided=true;
#             }else{
#                 isPaided=false;
#             }
            
#         },
#     })
