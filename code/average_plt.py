import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルの読み込み
# df = pd.read_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_model.csv')
# df = pd.read_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_sensor.csv')
df = pd.read_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_without.csv')


# データを数値型に強制変換し、無効な値を除去
df = df.apply(pd.to_numeric, errors='coerce')
df = df.dropna()

# 各行ごとに平均とデータ範囲（最大値と最小値）を計算
angle_average = []
angle_upper = []
angle_lower = []

for index, row in df.iterrows():
    values = row.values
    avg = sum(values) / len(values)  # 平均を計算
    max_val = max(values)  # 最大値を取得
    min_val = min(values)  # 最小値を取得
    angle_average.append(avg)
    angle_upper.append(max_val)
    angle_lower.append(min_val)

# 計算結果をデータフレームに追加
df['angle_average'] = angle_average
df['angle_upper'] = angle_upper
df['angle_lower'] = angle_lower
# count列を1からスタートさせて、それを100で割ってTime [s]に変換
df['Time [s]'] = (pd.Series(range(1, len(df) + 1)) / 100)

# 計算結果を新たなCSVファイルに格納
# output_file_path = r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_model.csv'
# output_file_path = r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_sensor.csv'
output_file_path = r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_without.csv'
df.to_csv(output_file_path, index=False)

# グラフをプロット
plt.figure(figsize=(10, 6))
plt.plot(df['Time [s]'], df['angle_average'], label='Angle Average', color='blue')
plt.fill_between(df['Time [s]'], df['angle_lower'], df['angle_upper'], color='blue', alpha=0.2, label='Data Range')

plt.xlabel('Time [s]')
plt.ylabel('Angle [deg]')
plt.legend()

# グラフをファイルに保存
# graph_output_path = r'C:\Users\Mizuki\University\Reserch\reflex\python\fig\time_vs_angle_model.pdf'
# graph_output_path = r'C:\Users\Mizuki\University\Reserch\reflex\python\fig\time_vs_angle_sensor.pdf'
graph_output_path = r'C:\Users\Mizuki\University\Reserch\reflex\python\fig\time_vs_angle_without.pdf'
plt.savefig(graph_output_path)

plt.show()
