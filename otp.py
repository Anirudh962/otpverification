import random

def generate_otp():
    "Generate a random 6-digit OTP"
    return str(random.randint (100000, 999999))
    
def send_otp(phone_number, otp): 
    "Simulate sending the OTP to a user's phone number" 
    print (f"OTP sent to {phone_number}: {otp}")

def verify_otp(entered_otp, generated_otp): 
    "Verity if the entered OTP matches the generated OTP"
    return entered_otp == generated_otp

def otp_verification(): 
    phone_number = input ("Enter your phone number: ")
    generated_otp = generate_otp() 
    send_otp (phone_number, generated_otp)
    entered_otp = input ("Enter the OTP you received: ")
    
    if verify_otp(entered_otp, generated_otp): 
        print ("OTP verification successful!")
    else: 
        print ("OTP verification failed.")

otp_verification()