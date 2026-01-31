#include <stdio.h>

int main(void) {
    float testScore1, testScore2, average;
    char status[15];
    int students;

    do {
        printf("Digite a quantidade de alunos: ");
        scanf("%d", &students);

        if (students < 0) {
            printf("O número de estudantes não pode ser negativo!\n\n");
        }
    } while (students < 0);

    return 0;
}