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

04. Train the Trainers
The "Train the trainers" course is coming to an end and the final assessment is approaching. Your task is to help the jury, which will assess the presentations, by writing a program that calculates the average grade for each presentation given by a given student, and finally - the average grade for all of them.
The first line of the console reads the number of people in the jury, n - an integer.
Then, on a separate line, the name of the presentation - text is read.
For each presentation, n - the number of grades - a real number are read on a new line.
After calculating the average grade for a specific presentation, the console prints:
"{presentation name} - {average grade}."
After receiving the "Finish" command, the console prints "Student's final assessment is {average grade for all presentations}." and the program ends.
All grades must be formatted to the second decimal place.
Sample input and output
Input         Output                               Explanations
2      	While-Loop - 5.75.                   2 – the number of people in the jury, therefore we will receive 2 
While-Loop    For-Loop - 5.75.                     marks per presentation.
6.00          Student's final assessment is 5.75.  (6.00 + 5.50) / 2 = 5.75
5.50                                               (5.84 + 5.66) / 2 = 5.75
For-Loop                                           (6.00 + 5.50 + 5.84 + 5.66) / 4 = 5.75 
5.84
5.66
Finish

Input         Output  
3             Arrays - 4.92.
Arrays        Lists - 5.75.
4.53          Student's final assessment is 5.34.
5.23
5.00
Lists
5.83
6.00
5.42
Finish	

Input                  Output 
2                      Objects and Classes - 5.00.
Objects and Classes    Dictionaries - 4.82.
5.77                   RegEx - 3.15.
4.23                   Student's final assessment is 4.32.
Dictionaries
4.62
5.02
RegEx
2.88
3.42
Finish	

05. Special numbers
Write a program that reads an integer N entered by the user and generates all possible "special" numbers from 1111 to 9999. For a number to be "special", it must meet the following condition:
• N must be divisible by each of its digits without a remainder.
Example: for N = 16, 2418 is a special number:
• 16 / 2 = 8 without a remainder
• 16 / 4 = 4 without a remainder
• 16 / 1 = 16 without a remainder
• 16 / 8 = 2 without a remainder
Input
The input is read from the console and consists of an integer in the interval [1…600000]
Output
All "special" numbers, separated by a space, must be printed on the console
Sample input and output
Input         Output                                                                            comments
3	       1111 1113 1131 1133 1311 1313 1331 1333 3111 3113 3131 3133 3311 3313 3331 3333   3 / 1 = 3 without remainder
                                                                                                3 / 3 = 1 without remainder
                                                                                                3 / 3 = 1 without remainder
                                                                                                3 / 3 = 1 without remainder
Input         Output
11	       1111

Input         Output
16	       1111 1112 1114 1118 1121 1122 1124 1128 1141 1142 1144 1148 1181 1182 1184 1188 
              1211 1212 1214 1218 1221 1222 1224 1228 1241 1242 1244 1248 1281 1282 1284 1288 
              1411 1412 1414 1418 1421 1422 1424 1428 1441 1442 1444 1448 1481 1482 1484 1488 
              1811 1812 1814 1818 1821 1822 1824 1828 1841 1842 1844 1848 1881 1882 1884 1888 
              2111 2112 2114 2118 2121 2122 2124 2128 2141 2142 2144 2148 2181 2182 2184 2188 
              2211 2212 2214 2218 2221 2222 2224 2228 2241 2242 2244 2248 2281 2282 2284 2288 
              2411 2412 2414 2418 2421 2422 2424 2428 2441 2442 2444 2448 2481 2482 2484 2488 
              2811 2812 2814 2818 2821 2822 2824 2828 2841 2842 2844 2848 2881 2882 2884 2888 
              4111 4112 4114 4118 4121 4122 4124 4128 4141 4142 4144 4148 4181 4182 4184 4188 
              4211 4212 4214 4218 4221 4222 4224 4228 4241 4242 4244 4248 4281 4282 4284 4288 
              4411 4412 4414 4418 4421 4422 4424 4428 4441 4442 4444 4448 4481 4482 4484 4488 
              4811 4812 4814 4818 4821 4822 4824 4828 4841 4842 4844 4848 4881 4882 4884 4888 
              8111 8112 8114 8118 8121 8122 8124 8128 8141 8142 8144 8148 8181 8182 8184 8188 
              8211 8212 8214 8218 8221 8222 8224 8228 8241 8242 8244 8248 8281 8282 8284 8288 
              8411 8412 8414 8418 8421 8422 8424 8428 8441 8442 8444 8448 8481 8482 8484 8488 
              8811 8812 8814 8818 8821 8822 8824 8828 8841 8842 8844 8848 8881 8882 8884 8888



