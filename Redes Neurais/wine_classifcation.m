[x,t] = wine_dataset; % Carrega o dataset

size(x)

net = patternnet(10);   % Cria a rede com 10 neuronios na camada oculta
view(net)               % Mostra a rede

[net,tr] = train(net,x,t); % Treina a rede
nntraintool % Mostra a interface grafica do treinamento

testX = x(:,tr.testInd);
testT = t(:,tr.testInd);

testY = net(testX);
testIndices = vec2ind(testY)

figure();
plotconfusion (testT, testY) % Plota a matriz de confusao

[c,cm] = confusion(testT,testY)
fprintf('Percentage Correct Classification   : %f%%\n', 100*(1-c));
fprintf('Percentage Incorrect Classification : %f%%\n', 100*c);

figure();
plotroc(testT,testY)