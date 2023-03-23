# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:41:06 2022

@author: KAALI PAHADI
"""



print()
print("Thank You for giving us information.")
print()
print("The information you gave us is as follows :-")
print()
print("Course selected              :  ",course)
print("Time period of the Course    :  ",time,"months")
print("Your experience in the gym   :  ",exp)
print("Do you want a Trainer?       :  ",trainer)
print()

if course=='Cardio'or'cardio':
    amount1 = 1400
    if time== 1 or 3 or 6 or 12 :
        amount1 = amount1*time
        if trainer=='Yes'or'yes':
            amount1 = amount1 + time*400
        elif trainer=='No'or'no':
            pass
        else:
            print('Invalid')
        if exp=='beginner'or'Beginner':
                amount1 += 1000
        elif exp=='mediocre'or'Mediocre':
                amount1 += 500
        elif exp=='professional'or'Professional':
            pass
        else:
            print('Invalid')
        
    print("The Total Amount1 to be paid Of the Given Course you selected is Rs.",amount1)
    
elif course=='Weightlifting'or'weightlifting':
    amount2 = 1500
    if time== 1 or 3 or 6 or 12 :
        amount2 = amount2*time
        if trainer=='Yes'or'yes':
            amount2 = amount2 + time*600
        elif trainer=='No'or'no':
            pass
        else:
            print('Invalid')
        if exp=='beginner'or'Beginner':
                amount2 += 1000
        elif exp=='mediocre'or'Mediocre':
                amount2 += 500
        elif exp=='professional'or'Professional':
            pass
        else:
            print('Invalid')
        
    print("The Total Amount2 to be paid Of the Given Course you selected is Rs.",amount2)
    
elif course=='Combined'or'combined':
    amount3 = 2000
    if time== 1 or 3 or 6 or 12 :
        amount3 = amount3*time
        if trainer=='Yes'or'yes':
            amount3 = amount3 + time*800
        elif trainer=='No'or'no':
            pass
        else:
            print('Invalid')
        if exp=='beginner'or'Beginner':
                amount3 += 1000
        elif exp=='mediocre'or'Mediocre':
                amount3 += 500
        elif exp=='professional'or'Professional':
            pass
        else:
            print('Invalid')
            
    print("The Total Amount3 to be paid Of the Given Course you selected is Rs.",amount3)
    
else:
    print("Invalid Information") 
    print("Please Check and fill again.")

