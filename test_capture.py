import cv2
import datetime
import os

# ネットワークカメラ接続方法を確認する
# BoxDriveでいいよね？ Box保存にできるようにする？

# fileName = os.getcwd() + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + ".png"
fileName = "C:/Users/Are-y/OneDrive/Document/without/UUUscreenshot_" + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + ".png"
# 内蔵カメラのデバイスIDは0、USBで接続したカメラは1以降。
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    raise IOError("Cannot open webcam")
# 取得した画像データは変数imageに格納。retは取得成功変数。
ret, image = capture.read()
if not ret:
    errmsg = 'スクリーンショットの取得に失敗しました。'
if ret is True:

    # 取得した画像を出力。fileNameは出力する画像名。
    ret = cv2.imwrite(fileName, image)
    if not ret and not errmsg:
        errmsg = 'スクリーンショットの保存に失敗しました。'
capture.release()
