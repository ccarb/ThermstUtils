classdef lib
   methods
      function r = GetDevices(obj)
            uri = 'http://127.0.0.1:5000/list_devices';
            r = webread(uri);
      end
      function r = ConnectDevice(obj, device)
            opts = weboptions('RequestMethod','post', 'MediaType','application/json');
            body = struct('device', device);
            uri = 'http://127.0.0.1:5000/open_connection';
            r = webwrite(uri, body, opts);
      end
      function r = SetTemperature(obj, temp)
            opts = weboptions('RequestMethod','post', 'MediaType','application/json');
            body = struct('temperature', string(temp));
            uri = 'http://127.0.0.1:5000/temperature_test';
            r = webwrite(uri, body, opts);
      end
      function r = GetTemperature(obj)
            uri = 'http://127.0.0.1:5000/temperature_test';
            resp = webread(uri);
            r = str2double(resp.temperature);
      end
   end
end

