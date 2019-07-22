data = csvread('final3Ddata.csv');

x = data(:,1);
y = data(:,2);
z = data(:,3);

z =  z - max(z);
p = patternCustom(z,x,y);
saveas(gcf, '3DPatternImage.png');
