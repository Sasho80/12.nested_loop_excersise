01.number_pyramid
Write a program that reads an integer n entered by the user and prints a number pyramid as in the examples:
Input  Output       
7      7 1
       2 3
       4 5 6

Input  Output    
10     1
       2 3
       4 5 6
       7 8 9 10

Input  Output
12	    1
        2 3
        4 5 6
        7 8 9 10
        11 12

Input  Output
15	   1
       2 3
       4 5 6
       7 8 9 10
       11 12 13 14 15
       
02. Equal sums of even and odd positions
Write a program that reads two six-digit integers from the console. The first number entered will always be less than the second. On the console, print on 1 line, separated by a space, all the numbers that are between the two numbers read from the console and meet the condition that the sum of the digits in even and odd positions is equal. If there are no numbers that meet the condition on the console, no result is output.
Sample input and output
Input   Output          Explanations
100000  100001 100012   The first number we generate is the number 100000. The sum of the digits in even positions (yellow) is 0+0+0=0.
100050  100023 100034   The sum of the digits in odd positions (green) is 
        100045          0+0+1=1. Since the two sums are different, the number is not printed.
                        The next number is 100001. The sum of the even positions is 1+0+0=1, and the sum of the odd positions is 0+0+1=1.
                        The two sums are equal, and the number is 
                        printed.
                        The next number to check is 100002. It does not meet the condition and is not printed.
                        ……
                        For the number 100045, the sum of the even positions is 5+0+0=5, and the sum of the odd positions is 4+0+1=5.
                        The two sums are equal, and the number is printed. 
                        And so on.
    
Input   Output 
123456  123464 123475 
124000  123486 123497 
        123530 123541 
        123552 123563 
        123574 123585 
        123596 123640
        123651 123662 
        123673 123684 
        123695 123750 
        123761 123772 
        123783 123794 
        123860 123871 
        123882 123893 
        123970 123981 
        123992

Input   Output 
299900  299970 299981 299992
300000

Input   Output 
100115  There is no way out.
100120




