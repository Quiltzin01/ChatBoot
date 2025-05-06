// Frontend del chatbot

#include <stdio.h>

int main(){
    // Definiendo el amaño de la interfaz gráfica (filas y columnas)
    int interfaceSizeRows = 38;
    int interfaceSizeColumns = 150;

    int i, j;

    char interface[interfaceSizeRows][interfaceSizeColumns];
    char question[250];

    // Creando la interfaz gráfica
    for (i = 0; i < interfaceSizeRows/2-1; i++){
        for (j = 0; j < interfaceSizeColumns; j++){
            interface[i][j] = 219; // Caracter ASCII
        }
    }

    for (i = 0; i < interfaceSizeRows/2-1; i++){
        for (j = 0; j < interfaceSizeColumns; j++){
            printf("%c", interface[i][j]);
        }
        printf("\n");
    }

    // Recibiendo la pregunta del usuario para el chatbot
    printf("\n%s", "Haz una pregunta sobre las plantas medicinales: ");
    scanf("%s", question);
    printf("\n");
    printf("\n");

    for (j = 0; j < interfaceSizeColumns; j++){
        interface[interfaceSizeRows/2-1][j] = '#';
    }
    
    for (i = interfaceSizeRows/2; i < interfaceSizeRows; i++){
        for (j = 0; j < interfaceSizeColumns; j++){
            interface[i][j] = 219; // Caracter ASCII
        }
    }

    for (i = interfaceSizeRows/2; i < interfaceSizeRows; i++){
        for (j = 0; j < interfaceSizeColumns; j++){
            printf("%c", interface[i][j]);
        }
        printf("\n");
    }

    return 0;
}
