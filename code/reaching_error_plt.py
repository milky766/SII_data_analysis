import pandas as pd
import matplotlib.pyplot as plt

# Type 1フォントの設定 (Type 3フォントを回避)
plt.rcParams['pdf.fonttype'] = 42  # PDFでType 1フォントを使用
plt.rcParams['ps.fonttype'] = 42  # PostScriptでType 1フォントを使用
# フォント設定 (デフォルトをサンセリフに設定)
plt.rcParams['font.family'] = 'DejaVu Sans'  # Type 1対応の英語フォントを選択

# xlsxファイルの読み込み
# file_path ="C:\\Users\\ymilk\\University\\reserch\\python\\SII_data_analysis\\data\\calculate_error.xlsx"
file_path =r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\origin\calculate_error_acryl.xlsx'
sheet_name = 'ago_4'

# データを読み込み
df = pd.read_excel(file_path, sheet_name=sheet_name)
df['Time'] = df['Time'] / 1000

# グラフの作成
plt.figure(figsize=(10,6))
plt.plot(df['Time'], df['ms_left_model'], label='Estimation by Model', color='red')
plt.plot(df['Time'], df['ms_left_sensor_estimate'], label='Estimation by Fiber Sensor', color='blue')
plt.plot(df['Time'], df['true_encoder'], label='Linear Encoder', color='green')

# 2.5秒の時点に黒の点線を追加
plt.axvline(x=2.7, color='black', linestyle='--', linewidth=1)
# テキストを追加
plt.text(6.1, 157, 'Strain Gauge Loses Tension', verticalalignment='center', horizontalalignment='right', fontsize=11, color='black')
# 横軸に2.7のラベルを追加
plt.xticks(list(plt.xticks()[0]) + [2.7])  # 現在のラベルに2.7を追加
# グラフの装飾
plt.xlabel('Time [s]')
plt.ylabel('Length [mm]')
plt.xlim(0, 12)  # 横軸の範囲を0から1200/100に制限
plt.ylim(130,165)
plt.legend(loc='upper right',fontsize=14)

# グラフを表示
plt.savefig("C:\\Users\\ymilk\\University\\reserch\\python\\SII_data_analysis\\fig\\reaching_error.pdf",bbox_inches='tight')
plt.show()
