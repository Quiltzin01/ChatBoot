// Frontend del chatbot Florabot

#include <stdio.h>
#include <time.h>

// Función para poner retardo para hacer la animación de cuando inicia la interfaz gráfica
void delay(float numberOfSeconds){
	float milliSeconds = 1000 * numberOfSeconds;
	clock_t startTime = clock();
	while (clock() < startTime + milliSeconds)
		;
}

int main(){
    // Definiendo el amaño del banner de la interfaz gráfica (filas y columnas)
    int interfaceSizeRows = 38;
    int interfaceSizeColumns = 150;
    int i, j;
    // Matriz que interpreta el banner visual
    char interface[interfaceSizeRows][interfaceSizeColumns];

    char question[250];

    // Creando el banner
    for (i = 0; i < interfaceSizeRows/2-1; i++){
        for (j = 0; j < interfaceSizeColumns; j++){
            interface[i][j] = 219; // Caracter ASCII
        }
    }

    // Mostrando el banner
    for (i = 0; i < interfaceSizeRows/2-1; i++){
        for (j = 0; j < interfaceSizeColumns; j++){
            printf("%c", interface[i][j]);
        }
        printf("\n");
    }

    // Recibiendo la pregunta que hace el usuario para el chatbot
    printf("\n%s", "Haga una pregunta sobre la familia de las plantas medicinales: ");

    // Escribiendo la pregunta en un archivo de texto para pasársela al backend para que el backend la procese
    FILE *file = fopen("pregunta.txt", "w");
	if (file == NULL){
		printf("%s\n", "Hubo un error, intentelo de nuevo.");
		return 1;
	}

	scanf("%[^\n]%*c", question);
	fprintf(file,"%s", question);
	fclose(file);

    printf("\n");
    printf("\n");

    return 0;
}
