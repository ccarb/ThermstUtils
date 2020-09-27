clear
clc
import lib
a = lib;

Ts = 0.5; % sec
x = zeros(2, 1);
y = zeros(2, 1);
index = 1;

a.SetTempCold(15);
objectiveTemperatureReached = false;

% while(objectiveTemperatureReached) % Leaving this purposefuly commented until arduino implements it
%     status = a.Status()
%     if (status.status_codes[1] == 2) || (status.status_codes[1] == 4)
%         objectiveTemperatureReached = status.status_codes[1]
%     end
% end

p = plot(x, y);
xlabel('Time [s]')
ylabel('Temperature [C]')
grid on
xlim([0 25])
ylim([0 60])
p.XDataSource = 'x';
p.YDataSource = 'y';

a.RestartTimer()
time = 0;
while(time < 5)
    [temp, time] = a.GetTemperature();
    x(index) = time;
    y(index) = temp;
    index = index + 1;
    refreshdata
    drawnow
    pause(Ts);
end
a.Stop()