clear; close all; clc;
% Gerando os valoress
X = zeros(100, 2);
X(:,1) = rand(100, 1);
X(:,2) = rand(100, 1);

% --- Plotando o gráfico ---
figure();
plot(X(:,1), X(:,2), '.', 'MarkerSize',15);
title('Dados gerados');

% Treino
rng(1); % Permitir a reprodutibilidade
k = 3;
[idx, C] = kmeans(X, k); 

% Grafico da distribuição
i = 1;
figure();
gscatter(X(:,i), X(:,i+1), idx);
hold on;
plot(C(:,i), C(:,i+1), 'kx', 'MarkerSize',15,'LineWidth',3);
title(strcat('Agrupamento dos dados para K=', num2str(k)));

% Encontrando o melhor K
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
title(strcat('Agrupamento dos dados para o ótimo K=', num2str(va.OptimalK)));

figure();
%plot(va.InspectedK, va.CriterionValues, '-*', 'MarkerSize',10);
plot(va)