from ba_whatsapp_api_client_python.response import Response


class Device:
    def __init__(self, basisApi) -> None:
        self.basisApi = basisApi
        
    def getDeviceInfo(self) -> Response:
            'The method is aimed for getting information about the device '\
            '(phone) running WhatsApp Business application.'
            
            return self.basisApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/GetDeviceInfo/{{apiTokenInstance}}')