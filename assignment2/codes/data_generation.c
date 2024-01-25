#include <stdio.h>

int main() {
    FILE *file = fopen("data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int a = 8;
    int d = 8;
    int start_n = -2;
    int end_n = 15;

    for (int n = start_n; n <= end_n; ++n) {
        int x_n = (a + d * n) > 0 ? (a + d * n) : 0;
        fprintf(file, "%d %d\n", n, x_n);
    }

    fclose(file);

    return 0;
}

