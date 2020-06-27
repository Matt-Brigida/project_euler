#include<stdio.h>
#include "solution.h"


int
main()
{

  int ans = 0;
  int i = 0; 
  
  while(fib(i) < MAX_NUMBER){
    if (fib(i) % 2) 
      ans += fib(i);
    i++;
  }

  printf("The answer is %d\n", ans);
  
  return 0;
	
}


//returns 4613732, is it correct?
