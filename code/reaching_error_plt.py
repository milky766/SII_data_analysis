import pandas as pd
import matplotlib.pyplot as plt

# xlsxファイルの読み込み
file_path =r"C:\Users\Mizuki\University\Reserch\reflex\python\data\origin\calculate_error_acryl.xlsx"
# file_path =r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\origin\calculate_error_acryl.xlsx'
sheet_name = 'ago_4'

# データを読み込み
df = pd.read_excel(file_path, sheet_name=sheet_name)
df['Time'] = df['Time'] / 1000

# グラフの作成
plt.figure(figsize=(10,6))
plt.plot(df['Time'], df['ms_left_model'], label='Estimation with Model', color='red')
plt.plot(df['Time'], df['ms_left_sensor_estimate'], label='Estimation with Fiber Sensor', color='blue')
plt.plot(df['Time'], df['true_encoder'], label='Linear Encoder', color='green')

# 2.5秒の時点に黒の点線を追加
plt.axvline(x=2.7, color='black', linestyle='--', linewidth=1)
# テキストを追加
plt.text(6.7, 157, 'Strain Gauge Loses Tension', verticalalignment='center', horizontalalignment='right', fontsize=13, color='black')
# 横軸に2.7のラベルを追加
plt.xticks(list(plt.xticks()[0]) + [2.7])  # 現在のラベルに2.7を追加
# グラフの装飾
plt.xlabel('Time [s]',fontsize=16)
plt.ylabel('Length [mm]',fontsize=16)
plt.xlim(0, 12)  # 横軸の範囲を0から1200/100に制限
plt.ylim(130,165)
plt.legend(loc='upper right',fontsize=13)

# グラフを表示
# plt.savefig("C:\\Users\\ymilk\\University\\reserch\\python\\SII_data_analysis\\fig\\reaching_error.pdf",bbox_inches='tight')

plt.savefig(r"C:\Users\Mizuki\University\Reserch\reflex\python\fig\reaching_error.pdf",bbox_inches='tight')
plt.show()
