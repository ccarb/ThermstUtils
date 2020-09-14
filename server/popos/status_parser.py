import json

class StatusParser():
    with open('server/popos/status_descriptions.json') as json_file:
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
        return StatusParser.errors_descriptions[str(error)]