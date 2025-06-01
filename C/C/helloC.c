#include <stdio.h>
extern int hi()
{
    printf("Hello, C!\n");

    return 0;
}

void main() {
    hi();
}