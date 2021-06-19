import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application")
mail = outlook.CreateItem(0)

mail.to = 'hazuki@mahodo.com; aiko@mahodo.com'
mail.subject = 'UUUに入材の予定があります'
mail.bodyFormat = 2
mail.body = '''お疲れ様です。
標記の件、UUU(K4U2S)倉庫への入材計画がありますので、
UUUの状況をご連絡します。
'''