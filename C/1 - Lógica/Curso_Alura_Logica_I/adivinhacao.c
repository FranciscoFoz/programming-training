#include <stdio.h>

#define NUMERO_DE_TENTATIVAS 5

int main() {

    // imprime o cabecalho do nosso jogo
    printf("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n");
    printf("* Olá mundo! Bem vindo ao nosso jogo de adivinhação! * \n");
    printf("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n");


    int numerosecreto = 42;
    int chute;
    int ganhou = 0;
    int tentativas = 1;

    char frasemotivacional[] = "Mas não desanime. Tente novamente.\n\n";


    while(1){
    //for (int i = 1; i <= NUMERO_DE_TENTATIVAS; i++){
        printf("+++++++++Tentativa %d++++++++++\n",tentativas);
        printf("Qual é o seu chute? ");
        scanf("%d", &chute);
        printf("Seu chute foi %d\n",chute);



        int acertou = (chute == numerosecreto);
        int maior = chute > numerosecreto;



        if (chute < 0){
            printf("Você não pode chutar números negativos!\n");
            tentativas--;
            
            continue;

        }


        if(acertou){
            printf("Parabéns! Você acertou!\n");

            break;
        }

        else if(maior){
            printf("Você errou! :( \n");
            printf("Seu chute foi maior que o numero secreto.\n");

            printf("%s", frasemotivacional);
            }

        else {
            printf("Você errou! :( \n");
            printf("Seu chute foi menor que o numero secreto. \n");

            printf("%s", frasemotivacional);
            }


        tentativas++;
        }
            
         
    printf("++++++FIM DE JOGO+++++++\n\n");   
    }





