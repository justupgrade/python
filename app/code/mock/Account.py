from requests.exceptions import ConnectionError
import requests


class Account(object):

    def __init__(self, data_interface):
        self.di = data_interface

    def get_account(self, id_num):
        try:
            result = self.di.get(id_num)
        except ConnectionError:
            result = "Connection error occurred. Try Again."

        return result

    def get_current_balance(self, id_num):
        response = requests.get('http:/mvc.dev/rest/balance/' + str(id_num))
        return {
            'status':   response.status_code,
            'data':     response.text
        }

if __name__ == '__main__':
    account = Account(None)
