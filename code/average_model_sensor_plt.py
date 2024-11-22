import pandas as pd
import matplotlib.pyplot as plt

# Type 1フォントの設定 (Type 3フォントを回避)
plt.rcParams['pdf.fonttype'] = 42  # PDFでType 1フォントを使用
plt.rcParams['ps.fonttype'] = 42  # PostScriptでType 1フォントを使用
# フォント設定 (デフォルトをサンセリフに設定)
plt.rcParams['font.family'] = 'DejaVu Sans'  # Type 1対応の英語フォントを選択

def adjust_and_plot(df_path, label, color, offset=0):
    # CSVファイルの読み込み
    df = pd.read_csv(df_path)

    # Time [s]列がすでにあることを前提にしているため、そのまま使用
    time = df['Time [s]']
    angle_average = df['angle_average'] - offset  # オフセットを引く
    angle_upper = df['angle_upper'] - offset
    angle_lower = df['angle_lower'] - offset

    # グラフをプロット
    plt.plot(time, angle_average, label=f'{label}', color=color)
    plt.fill_between(time, angle_lower, angle_upper, color=color, alpha=0.2)

# グラフ全体の設定
plt.figure(figsize=(10, 6))

# 1つ目のデータセット（model）の最初の値を取得
# model_df = pd.read_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_model.csv')
# sensor_df = pd.read_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_sensor.csv')
model_df = pd.read_csv(r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\combined_output_angle_adjusted_model.csv')
sensor_df = pd.read_csv(r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\combined_output_angle_adjusted_sensor.csv')

# オフセットを計算
model_initial_angle = model_df['angle_average'].iloc[0]
sensor_initial_angle = sensor_df['angle_average'].iloc[0]
offset_model = model_initial_angle - sensor_initial_angle

# # modelデータにオフセットを適用してプロット
# adjust_and_plot(
#     r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_model.csv',
#     'Reflex by Model',
#     'blue',
#     offset_model
# )

# # sensorデータをそのままプロット
# adjust_and_plot(
#     r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_sensor.csv',
#     'Reflex by Fiber Sensor',
#     'orange'
# )

# modelデータにオフセットを適用してプロット
adjust_and_plot(
    r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\combined_output_angle_adjusted_model.csv',
    'Reflex by Model',
    'red',
    offset_model
)

# sensorデータをそのままプロット
adjust_and_plot(
    r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\combined_output_angle_adjusted_sensor.csv',
    'Reflex by Fiber Sensor',
    'blue'
)

plt.xlabel('Time [s]')
plt.ylabel('Angle [deg]')
plt.legend(loc='upper right',fontsize=14)

# グラフをファイルに保存
plt.savefig(r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\fig\time_vs_angle_model_sensor.pdf',bbox_inches='tight')

plt.show()
