import pandas as pd
import numpy as np

# ファイルの読み込み
file_path = r"C:\Users\HosodaLab2\University\Reserch\reflex\SII_data_analysis\data\origin\calculate_error_acryl.xlsx"
xls = pd.ExcelFile(file_path)

# ago_1シートを読み込む
df = pd.read_excel(xls, sheet_name='ago_1')
df_filtered = df[(df['Time'] >= 0) & (df['Time'] <= 12000)]

# 平均平方2乗誤差 (MSE) の計算
mse = ((df_filtered['true_encoder'] - df_filtered['ms_left_model']) ** 2).mean()

# 平方根平均二乗誤差 (RMSE) の計算
rmse = np.sqrt(mse)

# RMSEを新しい列に追加
df_filtered['RMSE'] = rmse


# データの保存（必要に応じてファイルに保存する場合）
output_file_path = r"C:\Users\HosodaLab2\University\Reserch\reflex\SII_data_analysis\data\origin\calculate_error_acryl_rmse.xlsx"
df.to_excel(output_file_path, index=False)
