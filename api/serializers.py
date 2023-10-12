from rest_framework import serializers

from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'
        depth=2

class AppInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppInformation
        fields='__all__'
        depth=1

class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'


class ProbQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProbQuestion
        fields='__all__'
        depth=3


class ProbQuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProbQuestion
        fields='__all__'

class ProbQuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProbQuestionCategory
        fields='__all__'
        

class ProbAnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProbAnswer
        fields='__all__'
    
    
class ProbAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProbAnswer
        fields='__all__'
        depth=4

class ChildProbAnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChildProbAnswer
        fields='__all__'
    
class ChildProbAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChildProbAnswer
        fields='__all__'
        depth=4



class AdkarWithTaloSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdkarWithTalo
        fields='__all__'
        depth=1

class AdkarWithTaloCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdkarWithTalo
        fields='__all__'
        
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductCategory
        fields='__all__'

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductInfo
        fields='__all__'
        depth=1


class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderedProduct
        fields='__all__'
        depth=3

class OrderedProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderedProduct
        fields='__all__'

class UserProductsRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProductsRoutine
        fields=['id','theProduct','isRoutine','fromDate','toDate','usageTimes']
        depth=3


class UserProductsRoutineCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProductsRoutine
        fields='__all__'
    
class ProductsInTheBugCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductsInTheBug
        fields='__all__'

class ProductsInTheBugSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductsInTheBug
        fields='__all__'
        depth=1

class ListeningCilajWithQuranSerializer(serializers.ModelSerializer):
    class Meta:
        model=ListeningCilajWithQuran
        fields='__all__'
        depth=1

class ListeningCilajWithQuranCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=ListeningCilajWithQuran
        fields='__all__'


class ShikhCategorySerializer(serializers.ModelSerializer):
    dhagaysigaWithMuqaalkaShiiqa=ListeningCilajWithQuranCreateSerializer(read_only=True,many=True)
    class Meta:
        model=ShikhCategory
        fields='__all__'
        depth=1

class UserAnswerInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserAnswerInformation
        fields='__all__'
        depth=1


class UserChildAnswerInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserChildAnswerInformation
        fields='__all__'
        depth=1


class UserChildAdkarWithProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserChildAdkarWithProduct
        fields='__all__'
        depth=4

class AppointmentCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=AppointmentCategory
        fields='__all__'
        depth=1

class DoctorAppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model=DoctorAppointment
        fields='__all__'
        depth=1


class PatientResultSerializers(serializers.ModelSerializer):
    class Meta:
        model=PatientResult
        fields='__all__'
        depth=2

