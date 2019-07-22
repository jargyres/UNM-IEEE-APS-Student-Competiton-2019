
data = csvread('final3Ddata.csv');

x = data(:,1);
y = data(:,2);
z = data(:,3);

z =  z - max(z);

p = patternCustom(z,y,x);
while true
    pause(0.01)
    if ~isvalid(p)
        exit
    end
end
