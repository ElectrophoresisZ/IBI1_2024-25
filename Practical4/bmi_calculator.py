#Function for BMI calculation
def BMI_calculator(weight, height):  #Unit for weight:kg; Unit for height:m
    
    BMI = weight/(height*2)          # Formula of BMI calculation
    print('Your BMI is'+str(BMI))
    if BMI < 18.5:                   #Different conditions correspond to different outputs.
        print('You are underweight!')
    elif BMI > 18.5 and BMI <30:
        print('You have a normal weight.')
    else:
        print('You are obese!')

BMI_calculator(50, 1.72)        #Input values of weight and height.
BMI_calculator(100, 1.77)