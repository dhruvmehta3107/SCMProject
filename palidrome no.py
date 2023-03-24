# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 20:39:17 2022

@author: nakul
"""

def reverseDigits(num) :
 
    rev_num = 0;
    while (num > 0) :
        rev_num = rev_num * 10 + num % 10
        num = num // 10
     
    return rev_num

def isPalindrome(n) :
 
    rev_n = reverseDigits(n);

    if (rev_n == n) :
        return 1
    else :
        return 0
 
if __name__ == "__main__" :
 
    print("Hello! world")
    n = int(input())
     
    if isPalindrome(n) == 1 :
        print("Is", n, "a Palindrome number? ->", True)
         
    else :
        print("Is", n, "a Palindrome number? ->", False)
