camera = webcam;

nnet = alexnet;

picture = camera.snapshot;

picture = imresize(picture,[227,227]);

label = classify(nnet, picture);
% Classify the picture
image(picture); % Show the picture
title(char(label)); % Show the label