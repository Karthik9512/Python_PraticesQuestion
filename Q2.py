# # Simulate OTP Verification System

# -> Say you are building a OTP Verification System
# -> User will be asked to enter a 4-Digit OTP
# -> User will be given 3 attempts to enter correct OTP
# -> When attempts reach beyond 3, Say Maximum Attempts Reached, try after 24 Hours
# -> If the OTP is correct, say Transaction Success
# _______________________________________________________________________________________________________________________


import random

otp = random.randint(1000,9999)
print("Your OTP is:", otp)

attempt=0
max_attempts=3

while attempt<max_attempts:
    otp1= int(input("Enter the OTP: "))
    
    if otp==otp1:
        print("OTP verified")
        break
    else:     
        attempt+=1
        if attempt<max_attempts:
            print("Incorrect OTP. Try again.")
        else:   
            print("OTP not verified")


