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

    for (int studentNumber = 1; studentNumber <= students; studentNumber++) {
        printf("\nRegistro de notas do %d° aluno\n", studentNumber);
        do {
            printf("Digite a primeira nota: ");
            scanf("%f", &testScore1);

            printf("Digite a segunda nota: ");
            scanf("%f", &testScore2);

            if ((testScore1 < 0.00 || testScore1 > 10.00) || (testScore2 < 0.00 || testScore2 > 10.00)) {
                printf("\nAs notas do %d° aluno precisam estar entre 0 e 10!\n", studentNumber);
                printf("tente novamente...\n\n");

            }
        } while ((testScore1 < 0.00 || testScore1 > 10.00) || (testScore2 < 0.00 || testScore2 > 10.00));
    }
    
    return 0;
}