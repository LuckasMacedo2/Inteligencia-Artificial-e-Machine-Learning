#include <iostream>
using namespace std;

#define d1 4
#define d2 2
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

    // AND 1
    int e_and1[d1][d2] = {
        {0, 1},
        {0, 0},
        {1, 1},
        {1, 0}
    };

    int o_and1[] = {
        1,
        1,
        0,
        1
    };

    float p_and1[] = {1, 1};
    int bias_and1[] = {1};
    float p_bias_and1[] = {1};

    // AND 2
    int e_and2[d1][d2] = {
        {1, 0},
        {1, 1},
        {0, 0},
        {0, 1}
    };

    int o_and2[] = {
        1, 
        0,
        1,
        1
    };

    float p_and2[] = {1, 1};
    int bias_and2[] = {1};
    float p_bias_and2[] = {1};

    
    // OR
    int entrada[d1][d2] = {
        {0, 0},
        {0, 1},
        {1, 0},
        {0, 0}
    };

    float pesos_bias[] = {1};

    float bias[] = {1};

    float pesos_camada[] = {
        1, 
        1
    };

    // Saida desejada
    int saida_desejada[] = {
        0,
        1,
        1,
        0
    };

    float y1 = 0, y2 = 0, y;
    float erro_ = 0;
    for (int i = 0; i < num_int; i++)
    {
        for (int j = 0; j < d1; j++)
        {
            // AND 1
            y1 = F(Y(p_and1, e_and1, j) + p_bias_and1[0] * bias_and1[0]);
            erro_ = erro(o_and1[j], y1);
            if (erro_ != 0){
                // Camada 1
                atualiza_peso(p_and1, erro_, e_and1, j, d2);

                // Bias
                atualiza_bias(p_bias_and1, erro_, bias_and1[0], 0);
            }

            // AND 2
            y2 = F(Y(p_and2, e_and2, j) + p_bias_and2[0] * bias_and2[0]);
            erro_ = erro(o_and2[j], y2);
            if (erro_ != 0){
                // Camada 1
                atualiza_peso(p_and2, erro_, e_and2, j, d2);

                // Bias
                atualiza_bias(p_bias_and2, erro_, bias_and2[0], 0);
            }

            // OR
            y = F(y1 * pesos_camada[0] + y2 * pesos_camada[1] + pesos_bias[0] * bias[0]);

            erro_ = erro(saida_desejada[j], y);
            if (erro_ != 0){
                /*// Camada 1
                atualiza_peso(pesos_camada, erro_, entrada, j, d2);

                // Bias
                atualiza_bias(pesos_bias, erro_, bias[0], 0);*/
                pesos_camada[0] =  pesos_camada[0] + taxaAprendizado * erro_ * y1;
                pesos_camada[1] =  pesos_camada[1] + taxaAprendizado * erro_ * y2;

                pesos_bias[0] = pesos_bias[0] + taxaAprendizado * erro_ * bias[0];

            }
        }
        
    }
    cout<<endl;
    imprime(p_and1, d2, "Pesos AND 1: ");
    imprime(p_bias_and1, dBias, "Peso Bias AND 1: ");
    cout<<endl;

    imprime(p_and2, d2, "Pesos AND 2: ");
    imprime(p_bias_and2, dBias, "Peso Bias AND 2: ");
    cout<<endl;

    imprime(pesos_camada, d2, "Pesos camada 1: ");
    imprime(pesos_bias, dBias, "Pesos bias: ");
    cout<<endl;

    cout<<endl<<"Testes..."<<endl;
    cout<<"Calculado \t\tEsperado"<<endl;
    for (int i = 0; i < d1; i++)
    {
        // AND 1
            y1 = F(Y(p_and1, e_and1, i) + p_bias_and1[0] * bias_and1[0]);


            // AND 2
            y2 = F(Y(p_and2, e_and2, i) + p_bias_and2[0] * bias_and2[0]);
            

            // OR
            y = F(y1 * pesos_camada[0] + y2 * pesos_camada[1] + pesos_bias[0] * bias[0]);

            
        cout<<y<<"\t\t\t"<<saida_desejada[i]<<endl;
    }
    
}
