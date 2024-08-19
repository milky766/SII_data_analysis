import pandas as pd
import matplotlib.pyplot as plt

# xlsxファイルの読み込み
file_path ="C:\\Users\\ymilk\\University\\reserch\\python\\SII_data_analysis\\data\\calculate_error.xlsx"
sheet_name = 'anta_6'

# データを読み込み
df = pd.read_excel(file_path, sheet_name=sheet_name)
df['Time'] = df['Time'] / 1000

# グラフの作成
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['true_encoder'], label='Measured')
plt.plot(df['Time'], df['ms_right_model'], label='Estimated')

# グラフの装飾
plt.xlabel('Time[s]')
plt.ylabel('Length[mm]')
plt.xlim(0, 12)  # 横軸の範囲を0から1200/100に制限
plt.ylim(135,170)
plt.legend(loc='upper left')

# グラフを表示
plt.savefig("C:\\Users\\ymilk\\University\\reserch\\python\\SII_data_analysis\\fig\\reaching_error.pdf")
plt.show()
