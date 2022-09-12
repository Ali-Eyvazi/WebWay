
from rest_framework import serializers
from .models import User,OtpCode


class UserRegisterSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    phone_number=serializers.CharField(required=True)
    full_name=serializers.CharField(required=True)
    password=serializers.CharField(required=True,write_only=True)
    password2=serializers.CharField(required=True,write_only=True)




    def create( user_session):
        print('*'*90)
        return User.objects.create_user(# or del validated_data['password2'] **validated_data
                    email=user_session['email'],
                    phone_number=user_session['phone_number'],
                    full_name=user_session['full_name'],
                    password=user_session['password'],
                                ) 

    def validate_email(self,value):
        email=User.objects.filter(email=value).exists()
        if email:
            raise serializers.ValidationError('Try an other email address')
        return value



    def validate_full_name(self,value):
        if value== 'admin':
            raise serializers.ValidationError('username cant be "admin "')
        return value


    def validate_phone_number(self,value):
        email=User.objects.filter(phone_number=value).exists()
        if email:
            raise serializers.ValidationError('Try an other phone_number')
        return value

            
    def validate(self,data):
        if data['password']!=data['password2']:
            raise serializers.ValidationError('passwords must match "')
        return data



class CodeSerializer(serializers.ModelSerializer):
    class Meta :
        model= OtpCode
        fields=('code',)

    