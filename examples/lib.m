classdef lib
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
