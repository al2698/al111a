#include <stdio.h>

int main() {
    int n=10, s, i;

_sum:
    s=0; i=1;
_begin:
    if (i>n) goto _end;
    s+=i;
    i++;
    goto _begin;
_end:

    if (n == 100) goto _printSum100;

    printf("sum(10)=%d\n", s);

    n = 100;
    goto _sum;

_printSum100:
    printf("sum(100)=%d\n", s);
}
// goto 會讓程式很難寫，功能越多越長，非常不好維護，因此發明函數取代 goto