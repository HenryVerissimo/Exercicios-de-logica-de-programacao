#include <stdio.h>

#define DIAS_SEMANA 7

int main(void) {
    int aboveAverage = 0;
    float temperatureSum = 0.0;
    float temperatures[DIAS_SEMANA];
    float average;

    for (int day = 0; day < DIAS_SEMANA; day ++) {
       printf("Digite a temperatura do %d° dia: ", day + 1);
       scanf("%f", &temperatures[day]);

       temperatureSum += temperatures[day];
    }

    average = temperatureSum / DIAS_SEMANA;

    for (int index = 0; index < DIAS_SEMANA; index ++) {
        if (temperatures[index] > average) {
            aboveAverage ++;
        }
    }

    printf("\nMédia semanal: %.2f\n", average);
    printf("Dias a cima da média: %d\n", aboveAverage);

    return 0;
}