from kavenegar import *
def send_otp_code(phone_number,code):
    try:
        api = KavenegarAPI('6F4E4647356747484C685A304D5552667968445A6E7235307A506B55534771564736524E333368444333383D')
        params = {
            'sender': '',#optional
            'receptor': phone_number,#multiple mobile number, split by comma
            'message': f'this is your OTP code {code}',
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        
        print(e)
    except HTTPException as e: 
       
        print(e)

    s=b'APIException[501] \xd8\xa7\xd9\x85\xda\xa9\xd8\xa7\xd9\x86 \xd8\xa7\xd8\xb1\xd8\xb3\xd8\xa7\xd9\x84 \xd9\xbe\xdb\x8c\xd8\xa7\xd9\x85\xda\xa9 \xd9\x81\xd9\x82\xd8\xb7 \xd8\xa8\xd9\x87 \xd8\xb4\xd9\x85\xd8\xa7\xd8\xb1\xd9\x87 \xd8\xb5\xd8\xa7\xd8\xad\xd8\xa8 \xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8 \xd8\xaf\xd8\xa7\xd8\xaf\xd9\x87 \xd8\xb4\xd8\xaf\xd9\x87 \xd8\xa7\xd8\xb3\xd8\xaa'
    e= s.decode('utf-8')
    print(e)
