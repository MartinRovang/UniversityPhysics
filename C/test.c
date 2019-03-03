#include <stdio.h>
#include <stdlib.h>  // for strtol
 

int main(int argc, char *argv[]){

   //printf(argv[1]);
   int number = strtol(argv[1],NULL, 10);
   return number;

}