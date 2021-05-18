#include <stdio.h>
#include <stdlib.h>

int triangle(int a1, int a2){
  int v3; // rbx

  if ( a2 > (int)a1 )
    return 0;
  if ( a1 == 1 && a2 == 1 )
    return 1;
  if ( a2 == 1 )
    return triangle(a1 - 1, a1 - 1);
  v3 = triangle(a1, a2 - 1);
  return v3 + triangle(a1 - 1, a2 - 1);
}

int main(int argc, char* argv[]){
    int arg = strtol(argv[1], NULL, 10);
    for (int i=1; i <= arg; i++)
    {
      printf("%d\n", triangle(arg, i));
    }
}
