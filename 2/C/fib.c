#include<stdio.h>
#include "solution.h"


int fib(int n){
    if (n < 2){
      return(1);
    } else {
      return fib(n - 1) + fib(n - 2); 
    }
}


/* int */
/* main() */
/* { */

/*   printf("fib(10) is %d\n", fib(10)); */
  
/* } */
