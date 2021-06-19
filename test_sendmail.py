import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application")
mail = outlook.CreateItem(0)

mail.to = 'sho_takano@global.komatsu'
mail.subject = 'UUUに入材の予定があります'
mail.bodyFormat = 2
mail.body = "コンポG各位<br><br>\
    お疲れ様です。<br>\
    標記の件、UUU(K4U2S)倉庫への入材計画がありますので、\
    UUUの状況をご連絡します。<br>\
    <img src='photo/komatsu.jpg'>"

mail.Send()