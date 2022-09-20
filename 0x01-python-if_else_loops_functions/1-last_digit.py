#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

RandomNum = number



if number < 0:

    number = -(number)

else:

    number = number



            lastDigit = number % 10

            if RandomNum < 0:

                number = RandomNum

                        lastDigit = -(lastDigit)



                        if lastDigit > 5:

                            string = "and is greater than 5"

                        elif lastDigit == 0:

                            string = "and is 0"

                        elif lastDigit < 6:

                            string = "and is less than 6 and not 0"

                        print(f"Last digit of {number} is {lastDigit}", string)
