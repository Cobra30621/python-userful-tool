import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials 


class GoogleSheetManager:
    # Setting
    # 0. 參考此篇教學，去申請Google API : https://ithelp.ithome.com.tw/articles/10234325
    # 1. 由剛剛建立出的憑證，放置相同目錄以供引入
    auth_json_path = './google_sheet_key.json'

    # 2. 從剛剛建立的sheet，把網址中 https://docs.google.com/spreadsheets/d/〔key〕/edit 的 〔key〕的值代入 
    spreadsheet_key_path = ''

    # 3. Sheet id : 把網址中 https://docs.google.com/spreadsheets/d/key/edit#gid=<sheetID> 的 〔sheetID〕的值代入 
    # 把所有需要Sheet_id者列入
    sheet1_id = 2097225833

    # 我們想要取用的範圍
    gss_scopes = ['https://spreadsheets.google.com/feeds'] 


    # 取得權限
    def auth_gss_client(self, path, scopes):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scopes)
        return gspread.authorize(credentials)

    # 取得表單
    def get_sheet(self, id):
        gss_client = self.auth_gss_client(self.auth_json_path, self.gss_scopes) #呼叫我們的函式

        #我們透過open_by_key這個method來開啟sheet
        workbook = gss_client.open_by_key(self.spreadsheet_key_path)
        sheet = workbook.get_worksheet_by_id(id)
        df = pd.DataFrame(sheet.get_all_records())

        return df, sheet

    # 清除表單
    def clear_worksheet(self, worksheet):
        worksheet.clear()

    # 更新表單
    def update_worksheet(self, df, worksheet):
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
