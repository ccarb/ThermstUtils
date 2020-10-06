import json

class StatusParser():
    with open('json/status_descriptions.json') as json_file:
        descriptions = json.load(json_file)
    status_descriptions = descriptions["status"]
    errors_descriptions = descriptions["errors"]
    @classmethod
    def parse(cls, status):
        return [
            cls.device_state(str(status[0])),
            cls.error_state(str(status[1]))
        ]
    
    @classmethod
    def isvalid(cls, error):
        return error == 0

    @classmethod
    def device_state(cls, status):
        return StatusParser.status_descriptions[str(status)]
    
    @classmethod
    def error_state(cls, error):
        error_bits = bin(int(error))[2:].rjust(8, '0')
        descriptions = []
        for index, bit in enumerate(reversed(error_bits)):
            if bit == '1': descriptions.append(StatusParser.errors_descriptions[str(index)])
        return descriptions