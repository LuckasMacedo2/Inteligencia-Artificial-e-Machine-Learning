clear; clc; close all;

% Sobre o dataset 
% Dataset com 777 observações com 18 variáveis, as variáveis são:
% ---
% Name: Nome da universidade
% Private: Um fator com níveis Não e Sim, indicando universidade privada ou pública.
% Apps: Número de inscrições recebidas.
% Accept: Quantidade de inscrições aceitas.
% Enroll: Número de estudantes matriculados.
% Top10perc: Percentual de novos estudantes vindo do grupo de 10% melhores do segundo grau.
% Top25perc: Percentual de novos estudantes vindo do grupo de 25% melhores do segundo grau.
% F.Undergrad: Número de alunos de graduação em tempo integral.
% P.Undergrad Número de alunos de graduação em tempo parcial.
% Outstate: Aulas fora do estado.
% Room.Board: Custos da sala.
% Books: Custos de livros estimados.
% Personal: Estimativa de gastos por pessoa.
% PhD: Percentual de PHD's na universidade.
% Terminal: Percentual da faculdade com graduação.
% S.F.Ratio: Taxa estudantes/faculdade.
% perc.alumni: Percentual dos ex-alunos que doam.
% Expend: Despesas da instituição por aluno.
% Grad.Rate: Taxa de graduação
% ---
%

% -------------------------------------------------------------------------
% 1. Lendo os dados
dados = readtable('D:\Estudos\Liga IA\Codigos\College_data.csv');

% -------------------------------------------------------------------------
% 2. Arrumando os dados
% 2.1. Removendo a coluna nome
dados = dados(:,2:19);

% 2.2. Convertendo a tbaela para array
X = table2array(dados(:,2:18));
temp = table2array(dados(:,1:1));

% 2.3. Ajustes finais
% Convertendo a coluna de resposta para corresponder com os clusters
% 2 = privada, yes
% 1 = publica, no
Y = [];

for i = 1: size(dados(:,1:1))
   if  strcmp(table2array(dados(i,1:1)), 'No')
       Y(i) = 1;
   else
       Y(i) = 2;
   end
end
Y = Y';
% -------------------------------------------------------------------------
% 3. Criação do modelo
rng(1); % Permitir a reprodutibilidade
k = 20;

% Modelo Kmeans e treino
% [idx, C] = kmeans(dados, k) -> Executa o algoritmo de kmeans partindo dos
% dados observados 'X' e retorna a matriz idx com o resultado para cada
% % observação e as centroides C
% [idx, C] = kmeans(X, k); 
% 
% % -------------------------------------------------------------------------
% % 4. Teste
% % 4.1. Matriz de confusão
% conf = confusionmat(idx, Y);

% 4.2. Teste aleatorio
% for i = 1: size(X, 2) - 1
%     figure();
%     gscatter(X(:,i), X(:,i+1), idx, 'bg');
%     hold on;
%     plot(C(:,i), C(:,i+1), 'kx', 'MarkerSize',15,'LineWidth',3);
%     legend('Cluster 1', 'Cluster 2', 'Centroide');
%     title(strcat('Var', num2str(i), ', Var', num2str(i+1)));
% end

% -------------------------------------------------------------------------
% 5. Encontrando o melhor k
% Elbow metodo ou metodo do cotovelo

clusters = zeros(size(X, 1), 10);
for i = 1:10
   clusters(:,i) = kmeans(X, i); 
end

va = evalclusters(X,clusters,'CalinskiHarabasz')

[idx, C] = kmeans(X, va.OptimalK); 
i = 1;
figure();
gscatter(X(:,i), X(:,i+1), idx);
hold on;
plot(C(:,i), C(:,i+1), 'kx', 'MarkerSize',15,'LineWidth',3);
legend('Cluster 1', 'Cluster 2', 'Centroide');
title(strcat('Var', num2str(i), ', Var', num2str(i+1)));