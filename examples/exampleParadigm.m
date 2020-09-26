clear
clc
% import lib
classdef lib % Class lib can be moved to another file
   methods
      function r = SetTempCold(obj, temp)
            opts = weboptions('RequestMethod','post', 'MediaType','application/json');
            body = struct('temperature', temp); % temp must be int or float
            uri = 'http://127.0.0.1:5000/cold';
            r = webwrite(uri, body, opts);
      end
      function r = SetTempHot(obj, temp)
            opts = weboptions('RequestMethod','post', 'MediaType','application/json');
            body = struct('temperature', string(temp)); % temp must be int or float
            uri = 'http://127.0.0.1:5000/hot';
            r = webwrite(uri, body, opts);
      end
      function r = GetTemperature(obj)
            uri = 'http://127.0.0.1:5000/temperature_test';
            resp = webread(uri);
            r = [str2double(resp.temperature), str2double(resp.time)];
      end
      function r = RestartTimer(obj)
            opts = weboptions('RequestMethod','post', 'MediaType','application/json');
            body = struct();
            uri = 'http://127.0.0.1:5000/restart_timer';
            webwrite(uri, body, opts);
      end
      function r = Status(obj)
            uri = 'http://127.0.0.1:5000/';
            r = webread(uri);
      end            
   end
end
a = lib;

Ts = 0.5; % sec
x = zeros(2, 1);
y = zeros(2, 1);
index = 1;

a.SetTempCold(15);
objectiveTemperatureReached = false

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
ylim([0 30])
p.XDataSource = 'x';
p.YDataSource = 'y';

a.RestartTimer()
while(time < 20)
    [temp, time] = a.GetTemperature();
    x(index) = time;
    y(index) = temp;
    index = index + 1;
    refreshdata
    drawnow
    pause(Ts);
end