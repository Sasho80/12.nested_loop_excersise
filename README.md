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

03. Sums of prime and non-prime numbers
Write a program that reads integers from the console until the "stop" command is received. Find the sum of all entered prime numbers and the sum of all entered non-prime numbers. Since by definition in mathematics negative numbers cannot be prime, if a negative number is given as input, the following message "Number is negative." should be output. In this case, the entered number is ignored and is not added to either of the two sums, and the program continues its execution, waiting for the next number to be entered.
On the output, print the two found sums on two lines in the following format:
• "Sum of all prime numbers is: {prime numbers sum}"
• "Sum of all non prime numbers is: {nonprime numbers sum}"
Sample input and output                     
Input   Output                               Explanations
3       Sum of all prime numbers is: 29      The first number entered is 3. It is prime and we add it to the sum of 
9       Sum of all non prime numbers is: 13  prime numbers.
0                                            The next number is 9. It is not prime and we add it to the sum of 
7                                            prime numbers.
19                                           The number 0 is not prime and we add it to the sum of prime 
4                                            numbers. The sum becomes 9+0=9.
stop	                                      Next comes the number 4, which is not prime and we add it to the corresponding sum 9+4=13.
                                             We receive a stop command. The program stops its execution and we print both sums.

Input   Output  
30      Number is negative.
83      Sum of all prime numbers is: 83
33      Sum of all non prime numbers is: 83
-1
20
stop	

Input   Output 
0       Number is negative.
-9      Sum of all prime numbers is: 0
0       Sum of all non prime numbers is: 0
stop	







