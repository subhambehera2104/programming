from random import choice

def generate_4_digit_otp_bad():
    numbers = ['0','1', '2', '3', '9']
    otp = ""
    for i in range(0,4):
        otp += choice(numbers)
    return otp

def generate_4_digit_otp_medium():
    numbers = []
    for i in range(0, 9):
        numbers.append(str(i))
    otp = ""
    for i in range(0,4):
        otp += choice(numbers)
    return otp



def generate_4_digit_otp_best():
    numbers = [str(i) for i in range(0,9)] # list comprehension
    otp =  ''.join(choice(numbers) for i in range(4))
    return otp


print(generate_4_digit_otp_bad())

print(generate_4_digit_otp_medium())
print(generate_4_digit_otp_best())


