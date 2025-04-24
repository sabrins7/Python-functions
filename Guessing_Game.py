import random
random_number = random.randint(1,20)
print(random_number)

num_of_guess=0
max_guess=5

while num_of_guess<max_guess:
  try:
    input_str=input("Enter a num between 1 and 20: ")
    number=int(input_str)
    num_of_guess +=1

    if number > random_number:
         print("Number is too high!")
    elif number < random_number:
         print("Number is to low!")
    else:
         print("correct! You guessed it!")
         break
    
  except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    print(f"Ganme Over! The correct answer was {random_number}")




