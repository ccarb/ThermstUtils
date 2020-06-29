clear
clc
import lib
a = lib;

Ts = 0.5; % sec
Ns = 100;
x = zeros(2, 1);
y = zeros(2, 1);
index = 1;

a.SetTemperature(10);

p = plot(x, y);
xlabel('Time [s]')
ylabel('Temperature [C]')
grid on
xlim([0 25])
ylim([0 30])
p.XDataSource = 'x';
p.YDataSource = 'y';

time = 0;
while(time < 20)
    temp = a.GetTemperature();
    time = Ts * index;
    x(index) = time;
    y(index) = temp;
    index = index + 1;
    refreshdata
    drawnow
    pause(Ts);
end