#include <stdio.h>

int main() {
    float temp;
    int opcao;

    printf("Temperatura em Celsius: ");
    scanf("%f", &temp);

    printf("1. Para Fahrenheit\n2. Para Kelvin\nEscolha: ");
    scanf("%d", &opcao);

    if (opcao == 1)
        printf("Fahrenheit: %.2f\n", (temp * 9/5) + 32);
    else if (opcao == 2)
        printf("Kelvin: %.2f\n", temp + 273.15);
    else
        printf("Opção inválida\n");

    return 0;
}
