from whatsapp_api_client_python.response import Response


class Marking:
    def __init__(self, basisApi) -> None:
        self.basisApi = basisApi
        
    def readChat(self, chatId: str, idMessage: str) -> Response:
            'The method returns the chat message history.'

            requestBody = {
                'chatId': chatId,
                'idMessage': idMessage,
            }

            return self.basisApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/ReadChat/{{apiTokenInstance}}',
                requestBody)