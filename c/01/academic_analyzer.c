#include <stdio.h>

void processMetrics(float testScore1, float testScore2, float *pAverage, char *pStatus) {
    *pAverage = (testScore1 + testScore2) / 2;

    if (*pAverage >= 7.0 ) {
        *pStatus = 'A';
    } else if (*pAverage >= 5.0) {
        *pStatus = 'R';
    } else {
        *pStatus = 'F';
    }
}

int main(void) {
    float testScore1, testScore2, average;
    char status;
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

            if ((testScore1 < 0.00 || testScore1 > 10.00) || (testScore2 < 0.00 || testScore2 > 10.00)) {
                printf("\nAs notas do %d° aluno precisam estar entre 0 e 10!\n", studentNumber);
                printf("tente novamente...\n\n");

            }
        } while ((testScore1 < 0.00 || testScore1 > 10.00));

        do {
            printf("Digite a segunda nota: ");
            scanf("%f", &testScore2);

            if ((testScore2 < 0.00 || testScore2 > 10.00)) {
                printf("\nAs notas do %d° aluno precisam estar entre 0 e 10!\n", studentNumber);
                printf("tente novamente...\n\n");

            }
        } while ((testScore1 < 0.00 || testScore1 > 10.00) || (testScore2 < 0.00 || testScore2 > 10.00));

        processMetrics(testScore1, testScore2, &average, &status);

        printf("\n------------------------------\n");
        printf("Resultado do aluno %d:\n", studentNumber);
        printf("Média: %.2f\n", average);

        switch (status) {
            case 'A':
                printf("Staus: Aprovado\n");
                break;
            case 'R':
                printf("Status: Recuperação\n");
                break;
            default:
                printf("Status: Reprovado\n");
        }
        
        printf("------------------------------\n\n");
    }
    
    return 0;
}