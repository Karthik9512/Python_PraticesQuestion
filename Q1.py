# # Tuition Discount Calculation- Question 1
# ------------------------------------------------------------------------------------------------------------

# # Create a Python program to calculate the tuition fee discount 
# for students based on their grade levels and academic performance.


# Get user input for the following information:
#     Student's name 
#     Student's grade level (1-12) 
#     Base tuition fee 
#     Discount percentage
#     Academic Topper status (e.g whether the student is an academic topper or not)

# Determine the discount based on the following rules:
#     For students in grades 9 to 12:
#     If they are academic toppers, apply a 20% discount.
#     Otherwise, apply a 10% discount.
#     For students in grades 6 to 8, apply a 5% discount.
#     For grades below 6, apply no discount.

# Additional Discounts:
#     For grade 10, add an additional 3% discount.
#     For grade 12, add an additional 5% discount.
#     No additional discounts for other grades.

# Calculate the final tuition fee after applying the discount:
#     Calculate discount amount
#     Calculate final fee

# Output following
#     Student name
#     Grade level
#     Academic topper status (Yes/No)
#     Base tuition fee
#     Total discount percentage
#     Discount amount saved
#     Final tuition fee after discount
# ------------------------------------------------------------------------------------------------------------

s_name= input('enter the student name')
s_grade= int(input('enter the student grade(1-12)'))
s_tuition= float(input('enter the student tuition fee'))
s_discount= float(input('enter the student discount percentage'))
acd_topper= input('is the student academic topper(yes/no)')

if s_grade>=9 and s_grade<=12:
    if acd_topper=='yes':
        s_discount=20
    elif acd_topper=='no':
        s_discount=10
    else:
        print('invalid input for academic topper')

elif s_grade>=6 and s_grade<=8:
    if acd_topper=='yes':
        s_discount=5
    elif acd_topper=='no':
        s_discount=0
#Additional discount for 10th and 12th students
if s_grade==10:
    s_discount+=3
elif s_grade==12:
    s_discount+=5

final_discount= (s_discount/100)*s_tuition  
final_tuition= s_tuition-final_discount
saved_amount= s_tuition-final_tuition

print('-----------------------------------')
print('student name:',s_name)
print('student grade:',s_grade)
print('is student academic topper:',acd_topper)
print('student tuition fee:',s_tuition)
print('Total discount percentage:',final_discount)
print('amount saved:',saved_amount)
print('final tuition fee:',final_tuition)



