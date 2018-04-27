from google.oauth2 import service_account
from googleapiclient import discovery


class Gsheets:
    def __init__(self, settings, sheetid):
        self.sheet_id = sheetid

        credentials = service_account.Credentials.from_service_account_info(settings['auth_params']) \
            .with_scopes(['https://www.googleapis.com/auth/spreadsheets'])
        self.service = discovery.build('sheets', 'v4', credentials=credentials)

    def fetch(self, sheet_range):
        """
        Retrieves the values from a spreadsheet.

        :param str sheet_range: Range to return; in A1 notation
        :return: A list of lists, with each inner list being a row
        """
        r = self.service.spreadsheets().values().append(
            spreadsheetId=self.sheet_id, range=sheet_range
        ).execute()

        return r['values']

    def update(self, sheet_range, values):
        """
        Updates the values in a spreadsheet.

        :param str sheet_range: Range to update; in A1 notation
        :param list values: A list of lists, with each inner list being a row
        """
        body = {
            'range': sheet_range,
            'majorDimension': 'ROWS',
            'values': values,
        }

        self.service.spreadsheets().values().update(
            spreadsheetId=self.sheet_id, range=sheet_range, body=body, valueInputOption='USER_ENTERED'
        ).execute()
