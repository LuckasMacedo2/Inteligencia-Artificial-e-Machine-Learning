#include <iostream>
using namespace std;

#define d1 8
#define d2 3
#define taxaAprendizado 1
#define dBias 1
const int num_int = 500;

int F(float y){
    if (y > 0)
        return 1;
    return 0;
}

float erro(int Ydesejado, int Ycalculado){
    return Ydesejado - Ycalculado;
}

float Y(float peso[], int entrada[d1][d2], int j){
    float y = 0;
    for (int i = 0; i < d2; i ++){
        y += peso[i] * entrada[j][i];
    }
    return y;
}

void atualiza_peso(float peso[], float erro, int entrada[d1][d2], int j, int n){
    for (int i = 0; i < n; i++)
    {
        peso[i] = peso[i] + taxaAprendizado * erro * entrada[j][i];
    }    
}

void atualiza_bias(float peso_bias[], int erro, float bias, int j){
    peso_bias[j] = peso_bias[j] + taxaAprendizado * erro * bias;
}

void imprime(float v[], int n, string label){
    cout<<label;
    for (int i = 0; i < n; i++)
    {
        cout<<v[i]<<", ";
    }
    cout<<endl;
}



int main (){
    int entrada[d1][d2] = {
        {1, 1, 1},
        {1, 1, 0},
        {1, 0, 1},
        {1, 0, 0},
        {0, 1, 1},
        {0, 1, 0},
        {0, 0, 1},
        {0, 0, 0}
    };

    float pesos_bias[] = {1};

    float bias[] = {1};

    float pesos_camada[] = {
        1, 
        1, 
        1
    };

    // Saida desejada
    int saida_desejada[] = {
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        0
    };

    float y = 0;
    float erro_ = 0;
    for (int i = 0; i < num_int; i++)
    {
        for (int j = 0; j < d1; j++)
        {

            // Melhorar aqui
            y = F(Y(pesos_camada, entrada, j) + pesos_bias[0] * bias[0]);

            erro_ = erro(saida_desejada[j], y);
            if (erro_ != 0){
                // Camada 1
                atualiza_peso(pesos_camada, erro_, entrada, j, d2);

                // Bias
                atualiza_bias(pesos_bias, erro_, bias[0], 0);
            }
        }
        
    }
    cout<<endl;
    imprime(pesos_camada, d2, "Pesos camada 1: ");
    imprime(pesos_bias, dBias, "Pesos bias: ");
    cout<<endl<<"Testes..."<<endl;
    cout<<"Calculado \t\tEsperado"<<endl;
    for (int i = 0; i < d1; i++)
    {
        cout<<F(Y(pesos_camada, entrada, i) + pesos_bias[0] * bias[0])<<"\t\t\t"<<saida_desejada[i]<<endl;
    }
    
}
