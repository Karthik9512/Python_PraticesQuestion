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


