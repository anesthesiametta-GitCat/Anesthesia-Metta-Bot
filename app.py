from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# ตั้งค่า LINE
line_bot_api = LineBotApi('PuWBhDKBhBn6jSLARiRBBtSQKjl28MprhEkpG6TgarJ1GYJn4oBy0BvojTcpshrkOc+MaAQ+phsgv86Xyv8s9iYrVEpj8YdaZIDNBABf0pC1gi+fyB02VaPHQVs0q/qHSrm/YBR+FboB+JH0IAI1EQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('846700909539b30ce9ad97b03541a4cc')

# ตั้งค่า Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Anesthesia_Register_Database").sheet1

@app.route("/callback", methods=['POST'])
def callback():
    # รับข้อความจาก LINE
    body = request.get_data(as_text=True)
    # ตรงนี้คือส่วนที่ Python จะไปบันทึกลง Sheet
    # เช่น sheet.append_row([ข้อมูลพยาบาลที่ได้มา])
    return 'OK'

if __name__ == "__main__":
    app.run()