//Laura Fawzia Sambowo - 2306260145
//Proyek UAS Komnum - Adaptive Noise Cancellation Using Least-Squares Regression

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 1000  // max data length
#define M 32    // filter tap length
#define MU 0.01 // step size

// function to compute dot product between two vectors
float dot_product(float *h, float *x)
{
    float result = 0.0;
    for (int i = 0; i < M; i++)
        result += h[i] * x[i];
    return result;
}

// function to shift buffer and insert new sample
void shift_and_insert(float *buffer, float new_sample)
{
    for (int i = M - 1; i > 0; i--)
        buffer[i] = buffer[i - 1];
    buffer[0] = new_sample;
}

int main()
{
    float h[M] = {0}; // filter coefficients
    float x[M] = {0}; // input buffer
    float d[N] = {0}; // desired signal
    float n[N] = {0}; // reference signal (noise)
    float y[N] = {0}; // filter output
    float e[N] = {0}; // error signal

    int data_len = 0;

    // open input csv
    FILE *input_file = fopen("input.csv", "r");
    if (input_file == NULL)
    {
        printf("error: cannot open input.csv\n");
        return 1;
    }

    // skip header
    char line[100];
    fgets(line, sizeof(line), input_file); // discard header line

    // read data
    while (fscanf(input_file, "%f,%f", &d[data_len], &n[data_len]) == 2 && data_len < N)
    {
        data_len++;
    }
    fclose(input_file);

    // apply lms algorithm
    for (int i = 0; i < data_len; i++)
    {
        shift_and_insert(x, n[i]);
        y[i] = dot_product(h, x);
        e[i] = d[i] - y[i];
        for (int j = 0; j < M; j++)
            h[j] += 2 * MU * e[i] * x[j];
    }

    // write output
    FILE *output_file = fopen("output_signal.txt", "w");
    if (output_file == NULL)
    {
        printf("error: cannot open output_signal.txt\n");
        return 1;
    }

    fprintf(output_file, "index\tdesired\toutput\terror\n");
    for (int i = 0; i < data_len; i++)
        fprintf(output_file, "%d\t%.4f\t%.4f\t%.4f\n", i, d[i], y[i], e[i]);

    fclose(output_file);

    printf("simulation completed. results saved in 'output_signal.txt'.\n");
    return 0;
}
