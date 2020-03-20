''' The program prints teh numbers from 1 to 100. For multiples of three print "Fizz"
 and for the numbers for the multiples of five print "Buzz".
 For the numbers which are multiples of both print "FizzBuzz". '''

for number in range(1,101):

    # Check if the number is multiple of 3 and 5
     if number % 3 and number % 5 == 0:
         print("FizzBuzz")

     # Check if the number is multiple of 3
     elif number % 3 == 0:
         print("Fizz")

     # Check if the number is multiple of 5
     elif number % 5 ==0:
         print("Buzz")

     # Print the number
     else:
          print(number)

