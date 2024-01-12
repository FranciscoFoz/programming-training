#include <stdio.h>

int main(){
    int x;
    int y;

    printf("Digite um valor para x e outro para y ");
    scanf("%d %d", &x,&y);

    int multiplicacao = x * y;

    printf("A multiplicação de %d e %d é %d\n",x,y,multiplicacao);

}