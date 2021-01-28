#include <iostream>
using namespace std;

float taxaAprendizado = 1;
int num_interacoes = 500;
#define d1 16
#define d2 4
int num_bias = 3;


int F(float Y){
    if (Y > 0)
        return 1;
    return 0;
}

float erro(int Ydesejado, int Ycalculado){
    return Ydesejado - Ycalculado;
}

void atualiza_pesos(float pesos_camada11[], float pesos_camada12[], float y11, float y12,
    int bias[], float pesos_bias[], float pesos_camada2[], float y2, float _erro, int j, int entrada[d1][d2]){
    
    float temp = taxaAprendizado * _erro;
    // Atualizacao pesos camada 1
    for (int m = 0; m < d2; m++)
    {
        pesos_camada11[m] = pesos_camada11[m] + temp * entrada[j][m];
        pesos_camada12[m] = pesos_camada12[m] + temp * entrada[j][m];
    }

    // Atualizacao pesos camada 2
    pesos_camada2[0] = pesos_camada2[0] + temp * y11;
    pesos_camada2[1] = pesos_camada2[1] + temp * y12;
                    
    // Atualização dos bias
    for (int m = 0; m < num_bias; m++)
    {
        pesos_bias[m] = pesos_bias[m] + temp * bias[m];
    }
}

int soma(int entrada[d1][d2], float pesos_camada11[], float pesos_camada12[],
int bias[], float pesos_bias[], float pesos_camada2[], int j){
    // Calculo das saidas da camada 1
    float y11 = 0;
    float y12 = 0;
    
    for (int k = 0; k < d2; k++)
    {
        y11 += pesos_camada11[k] * entrada[j][k];
        y12 += pesos_camada12[k] * entrada[j][k];
    }
    y11 += bias[0] * pesos_bias[0];
    y12 += + bias[1] * pesos_bias[1];
    // Calculo da saida da camada 2
    float y2 = y11 * pesos_camada2[0] + y12 * pesos_camada2[1] + bias[2] * pesos_bias[2];

    return F(y2);
}

int soma_treino(int entrada[d1][d2], float pesos_camada11[], float pesos_camada12[],
int bias[], float pesos_bias[], float pesos_camada2[], int j, int saida_desejada){

    // Calculo das saidas da camada 1
    float y11 = 0;
    float y12 = 0;
    for (int k = 0; k < d2; k++)
    {
        y11 += pesos_camada11[k] * entrada[j][k];
        y12 += pesos_camada12[k] * entrada[j][k];
    }
    y11 += bias[0] * pesos_bias[0];
    y12 += + bias[1] * pesos_bias[1];
    // Calculo da saida da camada 2
    float y2 = y11 * pesos_camada2[0] + y12 * pesos_camada2[1] + bias[2] * pesos_bias[2];

    // Funcao de ativacao
    int Y = F(y2);

    // Calculo do erro
    float _erro = erro(saida_desejada, Y);
    if (_erro != 0){
        atualiza_pesos(pesos_camada11, pesos_camada12, y11, y12,
                    bias, pesos_bias, pesos_camada2, y2, _erro, j, entrada);
        
    }
    
    return Y;
}


void perceptron(){
    // Entrada
    int entrada[d1][d2] = {
        {1, 1, 1, 1},
        {1, 1, 1, 0},
        {1, 1, 0, 1},
        {1, 1, 0, 0},
        {1, 0, 1, 1},
        {1, 0, 1, 0},
        {1, 0, 0, 1},
        {1, 0, 0, 0},
        {0, 1, 1, 1},
        {0, 1, 1, 0},
        {0, 1, 0, 1},
        {0, 1, 0, 0},
        {0, 0, 1, 1},
        {0, 0, 1, 0},
        {0, 0, 0, 1},
        {0, 0, 0, 0}
    };

    //  Camada 1
    // y1
    float pesos_camada11[] = {
        1,  // Ye
        1,  // Gr
        1,  // Re
        1   // Bl
    };

    // y2
    float pesos_camada12[] = {
        1,  // Ye
        1,  // Gr
        1,  // Re
        1   // Bl
    };

    //  Camada 2
    float pesos_camada2[] = {
        1, 
        1
    };

    // Bias
    int bias[] = {
        1,  // bias1
        1,  // bias2
        1   // bias3
    };

    float pesos_bias[] = {
        1,  // Wb1
        1,  // Wb2
        1   // Wb3
    };

    // Saida desejada
    int saida_desejada[] = {
        1,  
        0,  
        0,  
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    };

    int Y = 0;
    float _erro = 0;

    for (int i = 0; i < num_interacoes; i++)
    {
        for (int j = 0; j < d1; j++)
        {
            Y = soma_treino(entrada, pesos_camada11, pesos_camada12,
                    bias, pesos_bias, pesos_camada2, j, saida_desejada[j]);
                  
        }
    }

    string r[] = {
        "Ye",   // Amarelo
        "Gr",   // Verde
        "Re",   // Vermelho
        "Bl"    // Azul
    };


    cout<<"Os pesos sao: "<<endl;
    cout<<"Camada 11"<<endl;

    for (int l = 0; l < d2; l++)
    {
        cout<<"W"<<r[l]<<"1 = "<<pesos_camada11[l]<<" ";
    }
    cout<<endl;

    for (int l = 0; l < d2; l++)
    {
        cout<<"W"<<r[l]<<"2 = "<<pesos_camada12[l]<<" ";
    }
    cout<<endl;

    cout<<"Bias"<<endl;
    for (int i = 0; i < num_bias; i++)
    {
        cout<<"Wb"<<i+1<<" = "<<pesos_bias[i]<<endl;
    }

    cout<<"Camada 2"<<endl;
    for (int i = 0; i < d2/2; i++)
    {
        cout<<"Wc"<<i+1<<" = "<<pesos_camada2[i]<<endl;
    }

    cout<<endl;
    // Testes
    float s = 0;
    bool ok = true;
    for (int i = 0; i < d1; i++)
    {
        Y = soma(entrada, pesos_camada11, pesos_camada12,
        bias, pesos_bias, pesos_camada2, i);

        _erro = erro(saida_desejada[i], Y);
        if (_erro != 0){
            cout<<"Erro, linha: "<<i<<"\nErro: "<<_erro<<endl<<endl;
            ok = false;
        }
            
    }
    if (ok)
        cout<<"Nenhum problema encontrado"<<endl;
    else
        cout<<"O percepton nao convergiu!"<<endl;

    while (true)
    {    
        int teste[1][4];
        cout<<"Informe os valores das cores\n[1] Para cor selecionada\n[0] Caso contrario"<<endl;

        cout<<"Amarela: ";
        cin>>teste[1][0];

        cout<<"Verde: ";
        cin>>teste[1][1];

        cout<<"Vermelha: ";
        cin>>teste[1][2];

        cout<<"Verde: ";
        cin>>teste[1][3];

        Y = soma(teste, pesos_camada11, pesos_camada12,
        bias, pesos_bias, pesos_camada2, 1);
        _erro = erro(1, Y);
        if (_erro != 0){
            cout<<"Errou! Tente novamente\n"<<endl;
        }else{
            cout<<"Acertou!\n"<<endl;
            break;
        }
    }
    
}


int main(){
    perceptron();
}