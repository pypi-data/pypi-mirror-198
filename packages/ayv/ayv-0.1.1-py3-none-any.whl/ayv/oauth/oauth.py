import os
from .oauth_constants import YouTubeOAuthConstants
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError


class Authenticate:
    """Handle the YouTube authentication process."""
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    __TOKEN_FILE = YouTubeOAuthConstants.TOKEN_FILE
    __API_SERVICE_NAME = YouTubeOAuthConstants.API_SERVICE_NAME
    __API_VERSION = YouTubeOAuthConstants.API_VERSION
    __SCOPES = YouTubeOAuthConstants.SCOPES
    
    def __init__(self, client_secrets_file: str , api_token_path: str = ''):
        """Create the auth object."""
        self.__credentials = None
        
        self.__verify_client_secret_file(client_secrets_file)
        self.__client_secrets_file = client_secrets_file
        
        if not api_token_path or not os.path.exists(api_token_path):
            self.__api_token_path = self.__get_default_api_token_path()
        else:
            self.__api_token_path = api_token_path
            
    def __verify_client_secret_file(self, client_secrets_file: str) -> None:
        """Verfy the client secret file."""
        if not client_secrets_file:
            raise ValueError('The clients secret file path has to be provided.')
        if not isinstance(client_secrets_file, str):
            raise TypeError('The clients secret file should be a string.')
        if not os.path.exists(client_secrets_file):
            raise ValueError(f'The path {client_secrets_file} does not exist!')
        
    def __get_default_api_token_path(self):
        """Generate the default api token file location."""
        current_user_home_dir = os.path.expanduser('~')
        api_token_path = os.path.join(current_user_home_dir, self.__TOKEN_FILE)
        return api_token_path
    
    def __authenticate_youtube(self):
        """Authenticate the YouTube API."""
        if os.path.exists(self.__api_token_path):
            with open(self.__api_token_path, "rb") as token:
                self.__credentials = pickle.load(token)
        # if there are no (valid) credentials availablle, let the user log in.
        if not self.__credentials or not self.__credentials.valid:
            if self.__credentials and self.__credentials.expired and self.__credentials.refresh_token:
                self.__credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.__client_secrets_file, self.__SCOPES)
                self.__credentials = flow.run_local_server(port=0)
            # save the credentials for the next run
            with open(self.__api_token_path, "wb") as token:
                pickle.dump(self.__credentials, token)

        return build(self.__API_SERVICE_NAME, self.__API_VERSION, credentials=self.__credentials)
    
    def authenticate(self):
        try:
            youtube_client =  self.__authenticate_youtube()
        except RefreshError as e:
            #delete token
            raise Exception('The token is expired. Kindly generate a new one.')
        else:
            return youtube_client