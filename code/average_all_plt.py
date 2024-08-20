import pandas as pd
import matplotlib.pyplot as plt

def adjust_and_plot(df_path, label, color, offset=0):
    # CSVファイルの読み込み
    df = pd.read_csv(df_path)

    # Time [s]列がすでにあることを前提にしているため、そのまま使用
    time = df['Time [s]']
    angle_average = df['angle_average'] - offset  # オフセットを引く
    angle_upper = df['angle_upper'] - offset
    angle_lower = df['angle_lower'] - offset

    # グラフをプロット
    line, = plt.plot(time, angle_average, label=f'{label}', color=color)
    fill = plt.fill_between(time, angle_lower, angle_upper, color=color, alpha=0.2)
    
    return line, fill

# グラフ全体の設定
plt.figure(figsize=(10, 6))

# 1つ目のデータセット（model）の最初の値を取得
# model_df = pd.read_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_model.csv')
# sensor_df = pd.read_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_sensor.csv')
# without_df = pd.read_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_without.csv')

model_df = pd.read_csv(r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\combined_output_angle_adjusted_model.csv')
sensor_df = pd.read_csv(r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\combined_output_angle_adjusted_sensor.csv')
without_df = pd.read_csv(r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\combined_output_angle_adjusted_without.csv')

# オフセットを計算
model_initial_angle = model_df['angle_average'].iloc[0]
sensor_initial_angle = sensor_df['angle_average'].iloc[0]
without_initial_angle = without_df['angle_average'].iloc[0]
offset_model = model_initial_angle - sensor_initial_angle
offset_without = without_initial_angle - sensor_initial_angle

# # modelデータにオフセットを適用してプロット
# line_model, fill_model = adjust_and_plot(
#     r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_model.csv',
#     'Reflex by Model',
#     'blue',
#     offset_model
# )

# line_sensor, fill_sensor = adjust_and_plot(
#     r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_sensor.csv',
#     'Reflex by Sensor',
#     'orange'
# )

# line_without, fill_without = adjust_and_plot(
#     r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_without.csv',
#     'without Reflex',
#     'green',
#     offset_without
# )

# modelデータにオフセットを適用してプロット
line_model, fill_model = adjust_and_plot(
    r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\combined_output_angle_adjusted_model.csv',
    'Reflex by Model',
    'blue',
    offset_model
)

line_sensor, fill_sensor = adjust_and_plot(
    r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\combined_output_angle_adjusted_sensor.csv',
    'Reflex by Sensor',
    'orange'
)

line_without, fill_without = adjust_and_plot(
    r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\combined_output_angle_adjusted_without.csv',
    'without Reflex',
    'green',
    offset_without
)

# 凡例の順序を「Model, Sensor, Without」に変更して表示
plt.legend(handles=[line_model, line_sensor, line_without])

plt.xlabel('Time [s]')
plt.ylabel('Angle [deg]')

# タイトにレイアウトを調整
plt.tight_layout()

# グラフをファイルに保存（余白をなくす）
plt.savefig(r'C:\Users\Mizuki\University\Reserch\reflex\python\fig\time_vs_angle_all.pdf', bbox_inches='tight')

plt.show()
