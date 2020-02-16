import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'service.json'


class df:
    def __init__(self,DIALOGFLOW_PROJECT_ID,DIALOGFLOW_LANGUAGE_CODE='en',SESSION_ID='me'):
        self.DIALOGFLOW_PROJECT_ID = DIALOGFLOW_PROJECT_ID
        self.DIALOGFLOW_LANGUAGE_CODE = DIALOGFLOW_LANGUAGE_CODE
        self.SESSION_ID = SESSION_ID

        # create session
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

    def GetResponse(self,text_to_be_analyzed):
        text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=self.DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)

        try:
            response = self.session_client.detect_intent(session=self.session, query_input=query_input)
        except InvalidArgument:
            raise

        return response.query_result.fulfillment_text

