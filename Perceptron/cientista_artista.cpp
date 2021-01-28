#include <iostream>
using namespace std;

int F(float Y){
    if (Y > 0)
        return 1;
    return 0;
}

float erro(int Ydesejado, int Ycalculado){
    return Ydesejado - Ycalculado;
}

float atualiza_peso(float Wi, float taxaAprendizagem, int erro, int entrada){
    return Wi + taxaAprendizagem * erro * entrada;
}

int Y(float W11, float W21, int X1, int X2, int Bias, float Wb1){
    float y = X1 * W11 + X2 * W21 + Bias * Wb1;
    return F(y);
}

void percepton(){
    float W11 = 0;
    float W12 = 0;
    float W21 = 0;
    float W22 = 0;
    float Wb1 = 0;
    float Wb2 = 0;
    int Bias1 = 1;
    int Bias2 = 1;
    int X1[] = {
        1, 1, 0, 0
    };
    int X2[] = {
        1, 0, 1, 0
    };
    int tam = 4;
    float y1 = 0, y2 = 0, _erro;
    float taxaAprendizado = 1;

    for (int i = 0; i < 100; i++)
    {
        cout<<"\n_______________________Iteracao "<<i + 1<<"_______________________"<<endl<<endl;
        // Entrada 1
        // X1 = 1   X2 = 1  Y1 = 1  Y2 = 0
        cout<<"\nEntrada 1"<<endl;
        cout<<"X1 = 1   X2 = 1  Y1 = 1  Y2 = 0  Einstein";
        y1 = Y(W11, W21, X1[0], X2[0], Bias1, Wb1);
        _erro = erro(1, y1);
        if (_erro != 0){
            W11 = atualiza_peso(W11, taxaAprendizado, _erro, X1[0]);
            W21 = atualiza_peso(W21, taxaAprendizado, _erro, X2[0]);
            Wb1 = atualiza_peso(Wb1, taxaAprendizado, _erro, Bias1);
        }
        printf("\nY1 = %f\nErro = %f\nW11 = %f\nW21 = %f\nWb1 = %f\n", y1, _erro, W11, W21, Wb1);

        y2 = Y(W12, W22, X1[0], X2[0], Bias2, Wb2);
        _erro = erro(0, y2);
        if (_erro != 0){
            W12 = atualiza_peso(W12, taxaAprendizado, _erro, X1[0]);
            W22 = atualiza_peso(W22, taxaAprendizado, _erro, X2[0]);
            Wb2 = atualiza_peso(Wb2, taxaAprendizado, _erro, Bias2);
        }
        printf("\nY2 = %f\nErro = %f\nW12 = %f\nW22 = %f\nWb2 = %f\n\n", y2, _erro, W12, W22, Wb2);

        // Entrada 2
        // X1 = 1   X2 = 0  Y1 = 0  Y2 = 0
        cout<<"\nEntrada 2"<<endl;
        cout<<"X1 = 1   X2 = 0  Y1 = 0  Y2 = 0 M. Assis";
        y1 = Y(W11, W21, X1[1], X2[1], Bias1, Wb1);
        _erro = erro(0, y1);
        
        if (_erro != 0){
            W11 = atualiza_peso(W11, taxaAprendizado, _erro, X1[1]);
            W21 = atualiza_peso(W21, taxaAprendizado, _erro, X2[1]);
            Wb1 = atualiza_peso(Wb1, taxaAprendizado, _erro, Bias1);
        }
        printf("\nY1 = %f\nErro = %f\nW11 = %f\nW21 = %f\nWb1 = %f\n", y1, _erro, W11, W21, Wb1);

        y2 = Y(W12, W22, X1[1], X2[1], Bias2, Wb2);
        _erro = erro(0, y2);
        if (_erro != 0){
            W12 = atualiza_peso(W12, taxaAprendizado, _erro, X1[1]);
            W22 = atualiza_peso(W22, taxaAprendizado, _erro, X2[1]);
            Wb2 = atualiza_peso(Wb2, taxaAprendizado, _erro, Bias2);
        }
        printf("\nY2 = %f\nErro = %f\nW12 = %f\nW22 = %f\nWb2 = %f\n\n", y2, _erro, W12, W22, Wb2);

        // Entrada 3
        // X1 = 0   X2 = 1  Y1 = 1  Y2 = 1
        
        cout<<"\nEntrada 3"<<endl;
        cout<<"X1 = 0   X2 = 1  Y1 = 1  Y2 = 1  M. Curie";
        y1 = Y(W11, W21, X1[2], X2[2], Bias1, Wb1);
        _erro = erro(1, y1);
        if (_erro != 0){
            W11 = atualiza_peso(W11, taxaAprendizado, _erro, X1[2]);
            W21 = atualiza_peso(W21, taxaAprendizado, _erro, X2[2]);
            Wb1 = atualiza_peso(Wb1, taxaAprendizado, _erro, Bias1);
        }
        printf("\nY1 = %f\nErro = %f\nW11 = %f\nW21 = %f\nWb1 = %f\n", y1, _erro, W11, W21, Wb1);
        y2 = Y(W12, W22, X1[3], X2[3], Bias2, Wb2);
        _erro = erro(1, y2);
        if (_erro != 0){
            W12 = atualiza_peso(W12, taxaAprendizado, _erro, X1[2]);
            W22 = atualiza_peso(W22, taxaAprendizado, _erro, X2[2]);
            Wb2 = atualiza_peso(Wb2, taxaAprendizado, _erro, Bias2);
        }
        
        printf("\nY2 = %f\nErro = %f\nW12 = %f\nW22 = %f\nWb2 = %f\n\n", y2, _erro, W12, W22, Wb2);

        // Entrada 4
        // X1 = 0   X2 = 0  Y1 = 0  Y2 = 1
        cout<<"\nEntrada 4"<<endl;
        cout<<"X1 = 0   X2 = 0  Y1 = 0  Y2 = 1  R. Queiroz";
        y1 = Y(W11, W21, X1[3], X2[3], Bias1, Wb1);
        _erro = erro(0, y1);
        if (_erro != 0){
            W11 = atualiza_peso(W11, taxaAprendizado, _erro, X1[3]);
            W21 = atualiza_peso(W21, taxaAprendizado, _erro, X2[3]);
            Wb1 = atualiza_peso(Wb1, taxaAprendizado, _erro, Bias1);
        }
        
        printf("\nY1 = %f\nErro = %f\nW11 = %f\nW21 = %f\nWb1 = %f\n", y1, _erro, W11, W21, Wb1);
        y2 = Y(W12, W22, X1[3], X2[3], Bias2, Wb2);
        _erro = erro(1, y2);
        if (_erro != 0){
            W12 = atualiza_peso(W12, taxaAprendizado, _erro, X1[3]);
            W22 = atualiza_peso(W22, taxaAprendizado, _erro, X2[3]);
            Wb2 = atualiza_peso(Wb2, taxaAprendizado, _erro, Bias2);
        }
        printf("\nY2 = %f\nErro = %f\nW12 = %f\nW22 = %f\nWb2 = %f\n\n", y2, _erro, W12, W22, Wb2);
    }
    cout<<endl<<endl;
    cout<<"\nDepois do treino..."<<endl<<endl;
    printf("Os pesos sao:\nW11 = %.2f W21 = %.2f Wb1 = %.2f\nW12 = %.2f W22 = %.2f Wb2 = %.2f\n",
    W11, W21, Wb1, W12, W22, Wb2);

    cout<<"\nAs equacoes das saidas sao:"<<endl;
    printf("Y1 = %.2f * X1 + %.2f * X2 + %.2f * Bias",
    W11, W21, Wb1);

    printf("\nY2 = %.2f * X1 + %.2f * X2 + %.2f * Bias\n",
    W12, W22, Wb2);

    cout<<"\nTeste com todas as entradas possiveis"<<endl;
    cout<<"Einstein\nEntradas:\n X1 = 1\tX2 = 1\nSaidas Esperadas:\n Y1 = 1\tY2 = 0"<<endl;
    cout<<"Saidas obtidas:\n Y1 = "<<Y(W11, W21, X1[0], X2[0], Bias1, Wb1)<<"\tY2 = "<<Y(W12, W22, X1[0], X2[0], Bias2, Wb2)<<endl<<endl;
    
    cout<<"M. Assis\nEntradas:\n X1 = 1\tX2 = 0\nSaidas Esperadas:\n Y1 = 0\tY2 = 0"<<endl;
    cout<<"Saidas obtidas:\n Y1 = "<<Y(W11, W21, X1[1], X2[1], Bias1, Wb1)<<"\tY2 = "<<Y(W12, W22, X1[1], X2[1], Bias2, Wb2)<<endl<<endl;

    cout<<"M. Curie\nEntradas:\n X1 = 0\tX2 = 1\nSaidas Esperadas:\n Y1 = 1\tY2 = 1"<<endl;
    cout<<"Saidas obtidas:\n Y1 = "<<Y(W11, W21, X1[2], X2[2], Bias1, Wb1)<<"\tY2 = "<<Y(W12, W22, X1[2], X2[2], Bias2, Wb2)<<endl<<endl;

    cout<<"R. Queiroz\nEntradas:\n X1 = 0\tX2 = 1\nSaidas Esperadas:\n Y1 = 0\tY2 = 1"<<endl;
    cout<<"Saidas obtidas:\n Y1 = "<<Y(W11, W21, X1[3], X2[3], Bias1, Wb1)<<"\tY2 = "<<Y(W12, W22, X1[3], X2[3], Bias2, Wb2)<<endl<<endl;
}

int main(){
    percepton();
}