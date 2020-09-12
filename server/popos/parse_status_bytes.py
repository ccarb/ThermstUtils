class ParseStatusBytes():
    @classmethod
    def parse(cls, status):
        return [
            self.device_state(status[0]),
            self.error_state(status[1])
        ]
    
    @classmethod
    def isvalid(cls, error):
        return error == 0

    @classmethod
    def device_state(cls, status):
        {
            "0": "standby",
            "1": "enfriando",
            "2": "calentando",
            "3": "temperatura en modo frio alcanzada",
            "4": "temperatura en modo calor alcanzada",
        }[str(status)]
    
    @classmethod
    def error_state(cls, error):
        {
            "1": "falla en termistor 1"
            "2": "falla en termistor 2"
            "3": "desvio entre termistores"
            "4": "falla en calibracion"
            "5": "falla en los rpm del fan del water cooling"
            "6": "temperatura limite superior superada"
            "7": "temperatura limite inferior superada"
        }[str(error)]