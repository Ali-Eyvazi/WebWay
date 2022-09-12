from django.shortcuts import redirect
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils import send_otp_code
from .models import OtpCode
from django.http import HttpResponseRedirect
from .serializers import UserRegisterSerializer,CodeSerializer

class UserRegisterView(APIView):

    serializer_class=UserRegisterSerializer
    def post(self,request):
        ser_data=self.serializer_class(data=request.POST)
        if ser_data.is_valid():
            
            random_Code=random.randint(1000,9999)
            send_otp_code(ser_data.validated_data['phone_number'],random_Code)

            OtpCode.objects.create(phone_number=ser_data.validated_data['phone_number'],code=random_Code)
            request.session['user_registration_info'] = {

                    'email':ser_data.validated_data['email'],
                    'phone_number':ser_data.validated_data['phone_number'],
                    'full_name':ser_data.validated_data['full_name'],
                    'password':ser_data.validated_data['password'],
                    'password2':ser_data.validated_data['password2']
            }
            # return redirect(redirect_to='https://127.0.0.1:8000/accounts/verify_code/')
            
            return Response(ser_data.data,status=status.HTTP_201_CREATED)

        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)



class VerifyRegistrationCode (APIView):

    serializer_class=CodeSerializer
    def post(self,request):
        user_session=request.session['user_registration_info'] 
                
        code_instance=OtpCode.objects.get(phone_number=user_session['phone_number'])
        # print(code_instance.code)
        ser_data=self.serializer_class(data=request.POST)
        
        if ser_data.is_valid():
            if ser_data.validated_data['code']== code_instance.code:
                UserRegisterSerializer.create(user_session) 
        
                code_instance.delete()
                return Response(ser_data.data,status=status.HTTP_201_CREATED)

            return Response(ser_data.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
