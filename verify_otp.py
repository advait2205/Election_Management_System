import random
from twilio.rest import Client

def send_otp(phone):
    otp = random.randint(1000, 9999)

    account_sid = "AC407fd137c4b102900606965b7f27163e"
    auth_token = "c19a23f6b3e9f2c805cf74b40f7ccc08"

    client = Client(account_sid, auth_token)

    msig = client.messages.create(
        body=f"Your OTP is {otp}",
        from_="+18457576411",
        to=phone
    )

    return otp


def verify(phone):
    otp = "0000"
    print("Enter your OTP")
    user_otp = int(input())

    if user_otp == otp:
        print("Verified")
        return True
    else:
        print("Incorrect OTP")
        return False

