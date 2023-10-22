from datetime import datetime
from datetime import timedelta
from email.policy import default
from decouple import config
from django.utils.safestring import mark_safe
import requests
from django.db import models
from cloudinary_storage.storage import VideoMediaCloudinaryStorage


class SubscriptionFeatures(models.Model):
    featureName = models.CharField(max_length=255, default='')
    desc = models.TextField(default='')

    def __str__(self) -> str:
        return str(self.featureName)+' -- '+str(self.desc)

# Create your models info here.


class AppInformation(models.Model):
    loginPageImage = models.ImageField(
        upload_to='images/appInfo', null=True, blank=True)
    fmLink = models.CharField(max_length=10000, default='')
    youSearchedText = models.CharField(max_length=500)
    isThereDiscount = models.BooleanField(default=False)
    discountSubscriptionPrice = models.FloatField(default=5)
    subscriptionPrice = models.FloatField(default=7)
    subscriptionPageTitle = models.CharField(max_length=255, default='')
    subscriptionFeatures = models.ManyToManyField(SubscriptionFeatures)
    subscriptionPageImage = models.ImageField(
        upload_to='images/appInfo', null=True, blank=True)
    subscriptionPageVideoLink = models.CharField(max_length=3000, default='')
    subscriptionButtonTitle = models.CharField(max_length=100, default='')
    subscriptionButtonDesc = models.CharField(max_length=255, default='')
    doctorWorkingForYouText = models.CharField(max_length=255, default='')

    def __str__(self) -> str:
        return str(self.subscriptionPrice)+' -- '+str(self.isThereDiscount)


class ShikhCategory(models.Model):
    name = models.CharField(max_length=255)
    profileImage = models.ImageField(
        upload_to='images/shikh', null=True, blank=True)
    simDesc = models.TextField(default='')
    isHero = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.name)+' -- '+str(self.isHero)


class ListeningCilajWithQuran(models.Model):
    name = models.CharField(max_length=255)
    theShikh = models.ForeignKey(
        ShikhCategory, related_name='dhagaysigaWithMuqaalkaShiiqa', on_delete=models.CASCADE)
    isVideo = models.BooleanField(default=False)
    videoLink = models.CharField(
        default='', max_length=10000, null=True, blank=True)
    voiceLink = models.CharField(
        default='', max_length=10000, null=True, blank=True)
    voice = models.FileField(upload_to='voice/listeningCilajWithQuran/',
                             null=True, blank=True, storage=VideoMediaCloudinaryStorage())
    text = models.TextField(default='')


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='images/products', null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)+' -- '+str(self.desc)


class RoutineTime(models.Model):
    name = models.CharField(max_length=255, default='subax')
    fromTime = models.TimeField(null=True)
    toTime = models.TimeField(null=True)
    notificationTime = models.TimeField(null=True)

    def __str__(self) -> str:
        return str(self.name)+' -- '+str(self.fromTime)


class ProductInfo(models.Model):
    name = models.CharField(max_length=255)
    isRoutine = models.BooleanField(default=True)
    theUsageTimes = models.ManyToManyField(RoutineTime, null=True, blank=True)
    theMessageText = models.TextField(default='')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image1 = models.ImageField(
        upload_to='images/products', null=True, blank=True)
    image2 = models.ImageField(
        upload_to='images/products', null=True, blank=True)
    price = models.FloatField(default=3)
    desc = models.TextField(null=True, blank=True)
    dateRegistred = models.DateField(auto_now=True)

    def theImage(self):
        if self.image1:
            return mark_safe('<img src={} width="100px" >'.format(self.image1.url))
        else:
            return mark_safe('<img src={} width="100px" >'.format('https://st3.depositphotos.com/3581215/18899/v/450/depositphotos_188994514-stock-illustration-vector-illustration-male-silhouette-profile.jpg'))

    theImage.allow_tags = True

    def __str__(self) -> str:
        return str(self.name)+' -- '+str(self.category.name)


class AdkarWithTalo(models.Model):
    name = models.CharField(max_length=255)
    voice = models.FileField(upload_to='voice/adkarWithTalo/',
                             null=True, blank=True, storage=VideoMediaCloudinaryStorage())
    isAdkar = models.BooleanField(default=False)
    itsArabic = models.BooleanField(default=True)
    text = models.TextField(default='')
    readingTime = models.ManyToManyField(RoutineTime, null=True, blank=True)
    readingCount = models.IntegerField(default=1)
    # readingTime=models.TimeField(null=True,blank=True)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)+' -- '+str(self.isAdkar)


class ProbQuestionCategory(models.Model):
    name = models.CharField(max_length=255)
    questionsCount = models.IntegerField(default=1)
    desc = models.TextField(default='')
    moreTrueDesc = models.TextField(default='')

    def __str__(self) -> str:
        return str(self.name)


DADKA_SUAASHAN = (
    ('caruur', 'CARUUR'),
    ('dadwaawayn', 'DADWAAWAYN')
)


class ProbQuestion(models.Model):
    probQuestionCategory = models.ForeignKey(
        ProbQuestionCategory, null=True, blank=True, on_delete=models.CASCADE)
    nuucaSuaasha = models.CharField(
        max_length=255, choices=DADKA_SUAASHAN, default='dadwaawayn')
    som = models.CharField(max_length=255, default='')
    arb = models.CharField(max_length=255, default='')
    eng = models.CharField(max_length=255, default='')
    desc = models.TextField(null=True, blank=True)
    isTrueAdkarWithTaloyin = models.ManyToManyField(
        AdkarWithTalo)
    isTrueProducts = models.ManyToManyField(ProductInfo, null=True, blank=True)
    regDate = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.som)+' -- '+str(self.desc)


class UserProfile(models.Model):
    fullName = models.CharField(max_length=255)
    number = models.CharField(max_length=16, default=0, unique=True)
    fireMessageId = models.CharField(max_length=1000, default='')
    profileImage = models.ImageField(
        upload_to='images/userProfile', null=True, blank=True)
    city = models.CharField(default='Mogadishu', max_length=33)
    password = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    age = models.IntegerField(default=15)
    userMatchedAdkarWithTalo = models.ManyToManyField(
        AdkarWithTalo, null=True, blank=True)
    aboutUser = models.TextField(null=True, blank=True)
    socialSituation = models.CharField(default='DOOB', max_length=25)
    numberOfWives = models.IntegerField(default=0)
    numberOfChilds = models.IntegerField(default=0)
    yearsOfPain = models.IntegerField(default=0)
    # userPruducts=models.ManyToManyField(ProductInfo,null=True,blank=True)
    # subscription
    latestTimeAnsweredQuestion = models.DateField(null=True, blank=True)
    latestSbscriptionDateFrom = models.DateField(null=True, blank=True)
    latestSbscriptionDateTo = models.DateField(null=True, blank=True)
    inPending = models.BooleanField(default=False)
    isSubscribedUser = models.BooleanField(default=False)
    subscriptionActive = models.BooleanField(default=False)
    is_activate = models.BooleanField(default=False)
    
    
    def save(self, *args, **kwargs):
        if self.inPending:
            self.latestTimeAnsweredQuestion = datetime.now()
            
        return super().save()
            
    def theImage(self):
        if self.profileImage:
            return mark_safe('<img src={} width="100px" >'.format(self.profileImage.url))
        else:
            return mark_safe('<img src={} width="100px" >'.format('https://st3.depositphotos.com/3581215/18899/v/450/depositphotos_188994514-stock-illustration-vector-illustration-male-silhouette-profile.jpg'))

    theImage.allow_tags = True

    def __str__(self) -> str:
        return str(self.fullName)+' -- '+str(self.number)


class UserProductsRoutine(models.Model):
    theUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    theProduct = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    isRoutine = models.BooleanField(default=True)
    isTakedProduct = models.BooleanField(default=False)
    fromDate = models.DateField(default=datetime.now())
    toDate = models.DateField(default=datetime.now() + timedelta(days=2))
    usageTimes = models.ManyToManyField(RoutineTime, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.theProduct.name)+' -- '+str(self.theUser)


class ProbAnswer(models.Model):
    theProbQuestion = models.ForeignKey(
        ProbQuestion, on_delete=models.CASCADE, default=1)
    theUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    desc = models.TextField(null=True, blank=True)
    answer = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.theProbQuestion.som)+' -- '+str(self.answer)


class ChildProbAnswer(models.Model):
    theProbQuestion = models.ForeignKey(
        ProbQuestion, on_delete=models.CASCADE, default=1)
    theChild = models.CharField(max_length=255)
    theUser = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    answer = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.theProbQuestion.som)+' -- '+str(self.answer)


PRODUCT_STATUS = (
    ('Pending', 'Pending'),
    ('Delivering', 'Delivering'),
    ('Completed', 'Completed')
)


class OrderedProduct(models.Model):
    theUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    theProductInfo = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(
        default='Pending', choices=PRODUCT_STATUS, max_length=25)
    orderTime = models.DateTimeField(auto_now=True)
    deliveredTime = models.DateTimeField(null=True, blank=True)
    isFromBug = models.BooleanField(default=False)
    userTaked = models.BooleanField(default=False)
    paidedMoney = models.FloatField(default=0)
    userTakedTime = models.DateTimeField(null=True, blank=True)
    paymentMethod = models.CharField(
        max_length=255, default='EVC WAAFI-PAYMENT')
    discount = models.FloatField(default=0)

    class Meta:
        ordering = ['-userTaked']

    def save(self, *args, **kwargs):
        if self.status == 'Completed':
            self.userTakedTime = datetime.now()
            self.userTaked = True

        if self.status == 'Delivering':
            self.deliveredTime = datetime.now()

        if self.userTaked:
            self.status == 'Completed'
            self.userTakedTime = datetime.now()

        if self.isFromBug:
            theProduct = ProductsInTheBug.objects.filter(
                pk=self.theProductInfo.pk)
            if theProduct.exists():
                theProduct = theProduct.first()
                UserProductsRoutine.objects.create(
                    theUser=self.theUser.pk,
                    theProduct=self.theProductInfo.pk,
                    usageTimes=theProduct.theUsageTimes,

                )

        return super().save()

    def __str__(self) -> str:
        return str(self.theUser)+' -- '+str(self.theProductInfo)


class AppointmentCategory(models.Model):
    categoryName = models.CharField(max_length=255)
    meetinTime = models.CharField(max_length=255, default='01:00 saac')
    bookingPrice = models.FloatField(default=5)
    fullDesc = models.TextField(default='')

    def __str__(self) -> str:
        return str(self.categoryName)+' -- '+str(self.bookingPrice)


class DoctorAppointment(models.Model):
    theUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    userAssignedDated = models.DateField(null=True, blank=True)
    doctorAssignedDated = models.DateTimeField(null=True, blank=True)
    sessionEnded = models.BooleanField(default=False)
    appointmentMeetingLink = models.CharField(
        max_length=255, null=True, blank=True)
    userRate = models.IntegerField(default=3)
    theCategory = models.ForeignKey(
        AppointmentCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-sessionEnded']

    def __str__(self) -> str:
        return str(self.theUser)+' -- '+str(self.userRate)


class ProductsInTheBug(models.Model):
    theUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    theProduct = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    theUsageTimes = models.ManyToManyField(RoutineTime, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    isTaked = models.BooleanField(default=False)


class UserAnswerInformation(models.Model):
    theUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    thePorbQuestionCategory = models.ForeignKey(
        ProbQuestionCategory, on_delete=models.CASCADE)
    trueAnswers = models.IntegerField(default=0)
    falseAnswers = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.theUser)+' -- '+str(self.trueAnswers)


class UserChildAnswerInformation(models.Model):
    theUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    theChild = models.CharField(max_length=255, default='')
    thePorbQuestionCategory = models.ForeignKey(
        ProbQuestionCategory, on_delete=models.CASCADE)
    trueAnswers = models.IntegerField(default=0)
    falseAnswers = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.theUser)+str(self.theChild)+' -- '+str(self.trueAnswers)


class UserChildAdkarWithProduct(models.Model):
    theUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    theChild = models.CharField(max_length=255, default='')
    theProducts = models.ManyToManyField(ProductInfo, null=True, blank=True)
    childMatchedAdkarWithTalo = models.ManyToManyField(
        AdkarWithTalo, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.theUser)


class SendNotification(models.Model):
    theUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    desc = models.CharField(max_length=255, default='')
    isLocalNotification = models.BooleanField(default=False)
    number = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.isLocalNotification:
            message = {
                # "notification_id": self.theUser.fireMessageId,
                "notification_type": self.title,
                "to":self.theUser.fireMessageId,
                "notification": {
                    "title": self.title,
                    "body": self.desc,
                }
            }
            response = requests.post(
                "https://fcm.googleapis.com/fcm/send",
                json=message,
                headers={
                    "Authorization": f'key={config("fmcAuthKey")}',
                    "Content-Type": "application/json"
                }
            )


class WaafiMarchentConfig(models.Model):
    merchantUid = models.CharField(default='', max_length=255)
    apiUserId = models.CharField(default='', max_length=255)
    apiKey = models.CharField(default='', max_length=255)

    merchantUidCABDALLA = models.CharField(default='', max_length=255)
    apiUserIdCABDALLA = models.CharField(default='', max_length=255)
    apiKeyCABDALLA = models.CharField(default='', max_length=255)

    def __str__(self) -> str:
        return str(self.merchantUid)



class PatientResult(models.Model):
    theUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    resultTitle=models.CharField(max_length=255,default='JAWAABTA BAARINTAANKA')
    resultDesc=models.TextField(default='')
    latestResult=models.BooleanField(default=True)
    resultDate=models.DateTimeField()
    adkarsWithTalos=models.ManyToManyField(
        AdkarWithTalo, null=True, blank=True)
    routineProducts=models.ManyToManyField(
        UserProductsRoutine, null=True, blank=True)


    def save(self, *args, **kwargs):
        if self.latestResult:
            PatientResult.objects.filter(theUser=self.theUser).update(latestResult=False)
            
        super().save(*args, **kwargs)
        self.theUser.inPending=False
        self.theUser.latestTimeAnsweredQuestion=self.resultDate
        self.theUser.subscriptionActive=True
        for thAdkar in self.adkarsWithTalos.all():
            self.theUser.userMatchedAdkarWithTalo.add(thAdkar)
        self.theUser.save()
        SendNotification.objects.create(
            theUser = self.theUser,
            title ="JAWAABTA BAARINTAAKA",
            desc =self.resultDesc,
            isLocalNotification =True
        )
        
        
        