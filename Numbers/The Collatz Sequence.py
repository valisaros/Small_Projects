def collatz(number):

    if number % 2 == 0:
          number = number // 2;
          print(number);
          return number

    elif number % 2 == 1:
           number = 3 * number + 1;
           print(number);
           return number

try:
    n = int(input())

    while n != 1:
        n = collatz(n);

except ValueError:
      print('Enter an integer value.')

