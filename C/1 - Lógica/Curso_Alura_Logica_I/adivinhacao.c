#include <stdio.h>


int main() {

    // imprime o cabecalho do nosso jogo
    printf("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n");
    printf("* Olá mundo! Bem vindo ao nosso jogo de adivinhação! * \n");
    printf("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n");


    int numerosecreto = 42;

    int chute;

    printf("Qual é o seu chute? ");
    scanf("%d", &chute);
    printf("Seu chute foi %d\n",chute);
}




