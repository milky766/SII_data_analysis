import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

folder_path = 'C:\\Users\\ymilk\\University\\reserch\\python\\SII_data_analysis\\data\\origin\\adapt\\reflex_with_model\\'
# folder_path = 'C:\\Users\\ymilk\\University\\reserch\\python\\SII_data_analysis\\data\\origin\\adapt\\reflex_with_sensor\\'
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

# 各CSVファイルに対して処理を実行
for file_path in csv_files:
    data = pd.read_csv(file_path)

    pressure_columns = ['pressure_right', 'pressure_left']
    tension_columns = ['tension_right', 'tension_left']
    ms_speed_columns = ['ms_speed_right_model', 'ms_speed_left_model']
    ms_model_columns = ['ms_right_model', 'ms_left_model']
    angle_column = ['angle']

    initial_angle = data['angle'].iloc[0]
    data['angle_adjusted'] = data['angle'] - initial_angle
    data['tension_left_adjusted'] = -data['tension_left']

    # グラフを描画するための時間調整 (12秒から14秒の範囲)
    time_adjusted = data['count'] / 100
    mask = (time_adjusted >= 5) & (time_adjusted <= 6)

    # データをフィルタリング
    data_filtered = data[mask]
    time_filtered = time_adjusted[mask]

    # グラフを作成
    fig, axs = plt.subplots(5, 1, figsize=(10, 15))

    # Joint angle graph
    axs[0].plot(time_filtered, data_filtered['angle_adjusted'], label='Angle', color='green')
    axs[0].set_ylabel('Angle [deg]')
    axs[0].legend(loc='upper right')
    axs[0].grid(True)

    # Muscle stretch speed graph
    axs[1].plot(time_filtered, data_filtered['ms_speed_right_model'], label='Estimated Velocity (Antagonist)', color='blue')
    axs[1].plot(time_filtered, data_filtered['ms_speed_left_model'], label='Estimated Velocity (Agonist)', color='red')
    axs[1].axhline(y=70, color='black', linestyle='--', label='Threshold')
    axs[1].set_ylabel('Estimated Velocity [mm/s]')
    axs[1].legend(loc='upper right')
    axs[1].grid(True)

    # Muscle model graph
    axs[2].plot(time_filtered, data_filtered['ms_right_model'], label='Estimated Length (Antagonist)', color='blue')
    axs[2].plot(time_filtered, data_filtered['ms_left_model'], label='Estimated Length (Agonist)', color='red')
    axs[2].set_ylabel('Estimated Length [mm]')
    axs[2].legend(loc='upper right')
    axs[2].grid(True)

    # Tension graph
    axs[3].plot(time_filtered, data_filtered['tension_right'], label='Δ Voltage (Antagonist)', color='blue')
    axs[3].plot(time_filtered, data_filtered['tension_left_adjusted'], label='Δ Voltage (Agonist)', color='red')
    axs[3].set_ylabel('Δ Voltage [mV]')
    axs[3].legend(loc='upper right')
    axs[3].grid(True)

    # Pressure graph
    axs[4].plot(time_filtered, data_filtered['pressure_right'], label='Pressure (Antagonist)', color='blue')
    axs[4].plot(time_filtered, data_filtered['pressure_left'], label='Pressure (Agonist)', color='red')
    axs[4].set_xlabel('Time [s]')
    axs[4].set_ylabel('Pressure [MPa]')
    axs[4].legend(loc='upper right')
    axs[4].grid(True)

    plt.tight_layout(pad=3.0)
    
    # ファイル名からベース名を取得してPDFファイルとして保存
    output_filename = os.path.join('C:\\Users\\ymilk\\University\\reserch\\python\\SII_data_analysis\\fig\\reflex_all_model', os.path.basename(file_path).replace('.csv', '_reflex_all_plt.pdf'))
    plt.savefig(output_filename)
    plt.close()

    print(f"Saved plot for {file_path} to {output_filename}")
