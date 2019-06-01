import os
import requests
import webbrowser
import datetime


class DeezerClientCredentials(object):

    def __init__(self, client_id=None, client_secret=None, scope=None, redirect_url=None):

        if not client_id:
            client_id = os.environ.get("DEEZER_CLIENT_ID")

        if not client_secret:
            client_secret = os.environ.get("DEEZER_SECRET_ID")

        if not redirect_url:
            redirect_url = os.environ.get("DEEZER_REDIRECT_URL")

        if not scope:
            print("You need to provide what permissions your application need.")

        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self.scope = scope
        self.redirect_url = redirect_url
        self.token_expires = 0

    def get_access_token(self):
        if self.token and not self.is_token_expired():
            return self.token

        new_token = self._retrieve_access_token()
        self.token = new_token
        return new_token

    def _retrieve_access_token(self):
        auth = f"https://connect.deezer.com/oauth/auth.php?app_id={self.client_id}&redirect_uri={self.redirect_url}" \
               f"&perms={self.scope}"
        try:
            webbrowser.open(auth)
        except:
            print(f"Please navigate here {auth}")

        response = input("Enter the URL you were redirected to: ")
        code = self._parse_response_code(response)
        access = f"https://connect.deezer.com/oauth/access_token.php?app_id={self.client_id}&secret={self.client_secret}" \
                 f"&code={code}"

        res = requests.get(access)
        token, expires = self._parse_response_token(res.text)
        print(f"Your access token is: {token}")

        self.token_expires = expires

        if token:
            return token
        else:
            return None

    def is_token_expired(self):
        now = datetime.datetime.now()
        if now > self.token_expires:
            return True

    def _parse_response_code(self, response):
        try:
            return response.split("?code=")[1]
        except IndexError:
            return None

    def _parse_response_token(self, response):
        try:
            token = response.split("access_token=")[1].split("&expires=")[0]
            seconds = int(response.split("access_token=")[1].split("&expires=")[1])
            expires = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
            return token, expires
        except IndexError:
            return None




