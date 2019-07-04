import shutil
import os
from glob import glob
import pandas as pd

#####処理1:準備
#csvの読み込み
df_data_path=pd.read_csv('./data_path.csv')

#リスト化
list_to_path=df_data_path['path'].values.tolist()
list_from_path=df_data_path['file_name'].values.tolist()

#フォルダpathの指定
path_download_dir='./download/{}'              #コピー元のフォルダ
path_s3='./s3/'                                #コピー先のフォルダ

#####処理2:フォルダ初期化
#s3フォルダが既に存在する場合は削除する
if os.path.exists(path_s3):
    shutil.rmtree(path_s3)                     #フォルダの削除

#新たにs3フォルダを作成
os.makedirs(path_s3)

for path in list_to_path:
    os.makedirs(path,exist_ok=True)            #フォルダの作成(既に存在するフォルダは作成しない)

#####処理3:ファイルコピー
#コピー先のパスのイテレーション数を初期化
k=0

for i in list_from_path:                       #コピーするファイルでイテレーション
    from_file_path=path_download_dir.format(i) #コピーするファイルパス
    to_s3_path=list_to_path[k]                 #コピー先のパス
    k=k+1                                      #コピー先のパスのイテレーション
    #ファイルの存在確認エラーハンドリング
    if os.path.exists(from_file_path):         #コピーするファイルが存在するか確認
        shutil.copy(from_file_path,to_s3_path) #ダウンロードファイルから指定のフォルダにコピーする
    else:
        print('{}が存在しません'.format(from_file_path))

#####処理4:ファイルの最終確認
#ToDo:s3フォルダにファイルが格納されていることを確認する
