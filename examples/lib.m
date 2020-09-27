classdef lib
   methods
      function r = SetTempCold(obj, temp)
            opts = weboptions('RequestMethod','post', 'MediaType','application/json');
            body = struct('objective_temperature', temp); % temp must be int or float
            uri = 'http://127.0.0.1:5000/cold';
            r = webwrite(uri, body, opts);
      end
      function r = SetTempHot(obj, temp)
            opts = weboptions('RequestMethod','post', 'MediaType','application/json');
            body = struct('objective_temperature', string(temp)); % temp must be int or float
            uri = 'http://127.0.0.1:5000/hot';
            r = webwrite(uri, body, opts);
      end
      function r = Stop(obj)
            opts = weboptions('RequestMethod','post', 'MediaType','application/json');
            body = struct();
            uri = 'http://127.0.0.1:5000/stop_device';
            r = webwrite(uri, body, opts);
      end
      function [temp, time] = GetTemperature(obj)
            uri = 'http://127.0.0.1:5000/read_temperature';
            resp = webread(uri);
            temp = resp.temperature;
            time = resp.time;
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
