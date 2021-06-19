import cv2
import datetime
import pyodbc
import pandas as pd
import pathlib
import lib.PyUtils


def main():
    errmsg = ''
    getOrder()
    if judge():
        print('Some work will be delivered tomorrow!')
        getScreenshot()
        sendMail()
    else:
        print('No work will be delivered...')


def getOrder():
    print('get order from rikatsuyo server!')
    SQL_TEMPLATE = "DELETE FROM [dbo].[顧客]"       # SQL原本
    editSql = SQL_TEMPLATE                          # SQL原本に置換をかける
    lib.PyUtils.ExecuteSQLBySQLServer(editSql)      # DELETE文の発行
    # dbに突っ込むデータが入っているCSVはUTF-8
    path = pathlib.Path(__file__).parent / "customer.csv"
    df = pd.read_csv(path)


    # 選択クエリを発行
    SQL_TEMPLATE = ("SELECT * FROM [dbo].[顧客]")     # SQL原本
    editSql = SQL_TEMPLATE                          # SQL原本に置換をかける
    df = lib.PyUtils.ReadQueryBySQLServer(editSql)  # SELECT文の発行
    for line in df.values:
        print(','.join(line))                       # SQL結果を調理して提供 


def judge():
    threeWorkingDaysLater(n)
    print('judge whether any work will be delivered')
    return True


def threeWorkingDaysLater(n):

    print('next working day is ****/**/**!')


def getScreenshot():
    image = captureScreenshot()
    return image


def captureScreenshot():

    fileName = "C:/Users/Are-y/OneDrive/Document/without/UUUscreenshot_" + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + ".png"
    # 内蔵カメラのデバイスIDは0、USBで接続したカメラは1以降。
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        raise IOError("Cannot open webcam")
    # 取得した画像データは変数imageに格納。retは取得成功変数。
    ret, image = capture.read()
    if ret == True:

        # 取得した画像を出力。fileNameは出力する画像名。
        ret = cv2.imwrite(fileName, image)
        if not ret:
            errmsg = 'スクリーンショットの取得もしくは保存に失敗しました。'
    capture.release()

    return image


def sendMail():
    print('you send a mail!')


main()

# echo "# UUUwarehouse" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/FukkinHikidashi/UUUwarehouse.git
# git push -u origin main
# …or push an existing repository from the command line
# git remote add origin https://github.com/FukkinHikidashi/UUUwarehouse.git
# git branch -M main
# git push -u origin main