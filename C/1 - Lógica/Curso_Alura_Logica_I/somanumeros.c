//SOMA NÚMEROS

#include <stdio.h>

int main(){

    int numero = 1;
    int soma = 0;

    while(numero <= 100){
        numero++;
        soma = soma + numero;
    }

    printf("A soma total é de %d\n", soma);

}