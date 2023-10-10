from django.urls import path
from . import views
urlpatterns = [
    
    # userProfile
    path('userProfile-list/',views.userProfileList),
    path('userProfile-create/',views.userProfileCreate),
    path('userProfile-update/<str:pk>/',views.userProfileUpdate),
    path('userProfile-delete/<str:pk>/',views.userProfileDelete),
    path('userProfile-detail/<str:pk>/',views.userProfileDetail),
    path('user-loginPr/<str:number>/<str:password>/',views.userLoginPr),
    path('user-login/',views.userLogin),
    path('check-user-exist/<str:number>/',views.checkUserExist),

    # appInfopython
    path('appInfo-data/',views.appInfoData),
    # path('appInfo-create/',views.probQuestionCreate),
    # path('appInfo-update/<str:pk>/',views.probQuestionUpdate),
    # path('appInfo-delete/<str:pk>/',views.probQuestionDelete),
    # path('appInfo-detail/<str:pk>/',views.probQuestionDetail),

    # ProbQuestion
    path('probQuestion-list/',views.probQuestionList),
    path('probQuestion-create/',views.probQuestionCreate),
    path('probQuestion-update/<str:pk>/',views.probQuestionUpdate),
    path('probQuestion-delete/<str:pk>/',views.probQuestionDelete),
    path('probQuestion-detail/<str:pk>/',views.probQuestionDetail),
    path('checkThisQusetionExist/<str:question>/',views.checkThisQusetionExist),

    # probanswer
    path('probAnswer-list/',views.probAnswerList),
    path('probAnswer-create/',views.probAnswerCreate),
    path('probAnswer-update/<str:pk>/',views.probAnswerUpdate),
    path('probAnswer-delete/<str:pk>/',views.probAnswerDelete),
    path('probAnswer-detail/<str:pk>/',views.probAnswerDetail),
    path('thisUserProbAnswer/<str:userId>/',views.thisUserProbAnswerList),
    path('probAnswerAssigning/<str:theQuestion>/<str:theUser>/<int:theAnswer>/',views.probAnswerAssigning),


    path('childProbAnswer-list/',views.childProbAnswerList),
    path('childProbAnswer-create/',views.childProbAnswerCreate),
    path('childProbAnswer-update/<str:pk>/',views.childProbAnswerUpdate),
    path('childProbAnswer-delete/<str:pk>/',views.childProbAnswerDelete),
    path('childProbAnswer-detail/<str:pk>/',views.childProbAnswerDetail),
    path('thisUserChildProbAnswer/<str:theUser>/',views.thisUserChildProbAnswer),
    path('childProbAnswerAssigning/<str:theQuestion>/<str:theUser>/<str:theChild>/<int:theAnswer>/',views.childProbAnswerAssigning),

    
    path('userChildAdkarWithProduct-list/',views.userChildAdkarWithProductList),
    path('userChildAdkarWithProduct-create/',views.userChildAdkarWithProductCreate),
    path('userChildAdkarWithProduct-update/<str:pk>/',views.userChildAdkarWithProductUpdate),
    path('userChildAdkarWithProduct-delete/<str:pk>/',views.userChildAdkarWithProductDelete),
    path('userChildAdkarWithProduct-detail/<str:pk>/',views.userChildAdkarWithProductDetail),
    path('thisUserChildAdkarWithProduct/<str:theUser>/<str:theChild>/',views.thisUserChildAdkarWithProduct),


    # probanswer
    path('productsInTheBug-list/',views.productsInTheBugList),
    path('productsInTheBug-create/',views.productsInTheBugCreate),
    path('productsInTheBug-update/<str:pk>/',views.productsInTheBugUpdate),
    path('productsInTheBug-delete/<str:pk>/',views.productsInTheBugDelete),
    path('productsInTheBug-detail/<str:pk>/',views.productsInTheBugDetail),
    path('thisUserProductsInTheBug/<str:userId>/',views.thisUserProductsInTheBugList),
    
    # adkarWithTalo
    path('adkarWithTalo-list/',views.adkarWithTaloList),
    path('adkarWithTalo-create/',views.adkarWithTaloCreate),
    path('adkarWithTalo-update/<str:pk>/',views.adkarWithTaloUpdate),
    path('adkarWithTalo-delete/<str:pk>/',views.adkarWithTaloDelete),
    path('adkarWithTalo-detail/<str:pk>/',views.adkarWithTaloDetail),
    # path('checkThisQusetionExist/<str:question>/',views.checkThisQusetionExist),
    

    path('productInfo-list/',views.productInfoList),
    path('productInfo-create/',views.productInfoCreate),
    path('productInfo-update/<str:pk>/',views.productInfoUpdate),
    path('productInfo-delete/<str:pk>/',views.productInfoDelete),
    path('productInfo-detail/<str:pk>/',views.productInfoDetail),
    # path('checkThisQusetionExist/<str:question>/',views.checkThisQusetionExist),

    path('productCategory-list/',views.productCategoryList),
    path('productCategory-create/',views.productCategoryCreate),
    path('productCategory-update/<str:pk>/',views.productCategoryUpdate),
    path('productCategory-delete/<str:pk>/',views.productCategoryDelete),
    path('productCategory-detail/<str:pk>/',views.productCategoryDetail),
    path('thisCategoryProducts-list/<str:catId>/',views.thisCategoryProductsList),

    
    path('probQuestionCategory-list/',views.probQuestionCategoryList),
    path('probQuestionCategory-create/',views.probQuestionCategoryCreate),
    path('probQuestionCategory-update/<str:pk>/',views.probQuestionCategoryUpdate),
    path('probQuestionCategory-delete/<str:pk>/',views.probQuestionCategoryDelete),
    path('probQuestionCategory-detail/<str:pk>/',views.probQuestionCategoryDetail),


    path('orderedProduct-list/',views.orderedProductList),
    path('orderedProduct-create/',views.orderedProductCreate),
    path('orderedProduct-update/<str:pk>/',views.orderedProductUpdate),
    path('orderedProduct-delete/<str:pk>/',views.orderedProductDelete),
    path('orderedProduct-detail/<str:pk>/',views.orderedProductDetail),
    path('thisUserOrderedProduct-list/<str:pk>/',views.orderedProductThisUser),
    path('changeOrderStatus/<str:orderId>/<str:status>/',views.changeOrderStatus),


    path('doctorAppointment-list/',views.doctorAppointmentList),
    path('doctorAppointment-create/',views.doctorAppointmentCreate),
    path('doctorAppointment-update/<str:pk>/',views.doctorAppointmentUpdate),
    path('doctorAppointment-delete/<str:pk>/',views.doctorAppointmentDelete),
    path('doctorAppointment-detail/<str:pk>/',views.doctorAppointmentDetail),
    path('thisUserDoctorAppointment-list/<str:pk>/',views.doctorAppointmentThisUser),


    path('appointmentCategory-list/',views.appointmentCategoryList),
    path('appointmentCategory-create/',views.appointmentCategoryCreate),
    path('appointmentCategory-update/<str:pk>/',views.appointmentCategoryUpdate),
    path('appointmentCategory-delete/<str:pk>/',views.appointmentCategoryDelete),
    path('appointmentCategory-detail/<str:pk>/',views.appointmentCategoryDetail),

    path('userProductsRoutine-list/',views.userProductsRoutineList),
    path('userProductsRoutine-create/',views.userProductsRoutineCreate),
    path('userProductsRoutine-update/<str:pk>/',views.userProductsRoutineUpdate),
    path('userProductsRoutine-delete/<str:pk>/',views.userProductsRoutineDelete),
    path('userProductsRoutine-detail/<str:pk>/',views.userProductsRoutineDetail),
    path('checkRoutineProductForThisUser-exist/<str:theProduct>/<str:theUser>/',views.checkRoutineProductForThisUserExist),
    path('thisUserProductsRoutine-list/<str:userId>/',views.thisUserProductRoutineList),

    path('listeningCilajWithQuran-list/',views.listeningCilajWithQuranList),
    path('listeningCilajWithQuran-create/',views.listeningCilajWithQuranCreate),
    path('listeningCilajWithQuran-update/<str:pk>/',views.listeningCilajWithQuranUpdate),
    path('listeningCilajWithQuran-delete/<str:pk>/',views.listeningCilajWithQuranDelete),
    path('listeningCilajWithQuran-detail/<str:pk>/',views.listeningCilajWithQuranDetail),


    path('shikhCategory-list/',views.shikhCategoryList),
    path('shikhCategory-create/',views.shikhCategoryCreate),
    path('shikhCategory-update/<str:pk>/',views.shikhCategoryUpdate),
    path('shikhCategory-delete/<str:pk>/',views.shikhCategoryDelete),
    path('shikhCategory-detail/<str:pk>/',views.shikhCategoryDetail),
    path('thisShikhListening-list/<str:shikhId>/',views.thisShikhListeningList),

    # user appointment
    path('generateCilajToTheUser/<str:userId>/',views.generateCilajToTheUser),
    path('guessTheUserChildPian/<str:userId>/<str:theChild>/',views.guessTheUserChildPian),
    path('generateCilajToTheUserChild/<str:userId>/<str:theChild>/',views.generateCilajToTheUserChild),
    path('guessTheUserPian/<str:userId>/',views.guessTheUserPian),



    path('userPaidingCharges/<str:paymentType>/<str:itemType>/',views.merchantPaidApi),

    path('searchProduct/<str:searchKey>/',views.searchProduct),
    # path('sendOtpSMS/<str:userNumber>/',views.sendOtpSMS),

    path('waafiApiPREAUTHORIZE/',views.waafiAPIPREAUTHORIZE),
    path('commitWaafiApiPREAUTHORIZE',views.commitWaafiApiPREAUTHORIZE),
    path('cancelWaafiApiPREAUTHORIZE',views.cancelWaafiApiPREAUTHORIZE),
    
    path('sendAppointmentNot/<str:email>/',views.sendAppointmentNot),
    path('sendProbQuestionRequest/<str:email>/',views.sendProbQuestionRequest)
    
]   