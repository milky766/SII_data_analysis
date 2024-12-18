import pandas as pd
import matplotlib.pyplot as plt

<<<<<<< HEAD
# Type 1フォントの設定 (Type 3フォントを回避)
plt.rcParams['pdf.fonttype'] = 42  # PDFでType 1フォントを使用
plt.rcParams['ps.fonttype'] = 42  # PostScriptでType 1フォントを使用
# フォント設定 (デフォルトをサンセリフに設定)
plt.rcParams['font.family'] = 'DejaVu Sans'  # Type 1対応の英語フォントを選択

file_path = r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\origin\adapt\reflex_with_model\20240819_r20.csv'
#file_path = r'C:\Users\HosodaLab2\University\Reserch\reflex\SII_data_analysis\data\origin\adapt\reflex_with_model\20240819_r20.csv'
=======
# file_path = r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\data\origin\adapt\reflex_with_model\20240819_r20.csv'
# file_path = r'C:\Users\HosodaLab2\University\Reserch\reflex\SII_data_analysis\data\origin\adapt\reflex_with_model\20240819_r20.csv'
file_path = r'C:\Users\Mizuki\University\Reserch\reflex\python\data\origin\adapt\reflex_with_model\20240819_r20.csv'
>>>>>>> ae7708c8c90af95cbb84f325210d1e6bb494bbcd
data = pd.read_csv(file_path)

pressure_columns = ['pressure_right', 'pressure_left']
tension_columns = ['tension_right', 'tension_left']
ms_speed_columns = ['ms_speed_right_model', 'ms_speed_left_model']
ms_model_columns = ['ms_right_model', 'ms_left_model']
angle_column = ['angle']

initial_angle = data['angle'].iloc[0]
data['angle_adjusted'] = data['angle'] 
# data['angle_adjusted'] = data['angle'] - initial_angle

# analog signal to tension
data['tension_left_scaled'] = data['tension_left'] * (-80/65535)
data['tension_right_scaled'] = data['tension_right'] * (80/65535)

# Selecting the relevant columns for each plot

# Plotting the graphs
fig, axs = plt.subplots(5, 1, figsize=(10, 13))
time_adjusted = data['count'] / 100

# 時間を調整 (12秒から14秒の範囲)
mask = (time_adjusted >= 5.1) & (time_adjusted <= 6.1)

# データをフィルタリング
data_filtered = data[mask]
time_filtered = time_adjusted[mask]

# 時間を0から始まるように調整
time_filtered = time_filtered - time_filtered.iloc[0]

# Joint angle graph
axs[0].plot(time_filtered, data_filtered['angle_adjusted'], label='Angle', color='green')
axs[0].set_ylabel('Angle [deg]',fontsize=14)
axs[0].legend(loc='upper right',fontsize=12)
axs[0].grid(True)

# Muscle stretch speed graph
axs[1].plot(time_filtered, data_filtered['ms_speed_left_model'], label='Estimated Velocity (Agonist)', color='#FFA500')  # Orange
axs[1].plot(time_filtered, data_filtered['ms_speed_right_model'], label='Estimated Velocity (Antagonist)', color='#1E3A8A')  # Dark Blue
axs[1].axhline(y=75, color='black', linestyle='--', label='Threshold = 75 [mm/s]')
axs[1].set_ylabel('Estimated Velocity [mm/s]',fontsize=12)
axs[1].legend(loc='upper right',fontsize=12)
axs[1].grid(True)

# Muscle model graph
axs[2].plot(time_filtered, data_filtered['ms_left_model'], label='Estimated Length (Agonist)', color='#FFA500')  # Orange
axs[2].plot(time_filtered, data_filtered['ms_right_model'], label='Estimated Length (Antagonist)', color='#1E3A8A')  # Dark Blue
axs[2].set_ylabel('Estimated Length [mm]',fontsize=12)
axs[2].legend(loc='upper right',fontsize=12)
axs[2].grid(True)

# Tension graph
axs[3].plot(time_filtered, data_filtered['tension_left_scaled'], label='Δ Voltage (Agonist)', color='#FFA500')  # Orange
axs[3].plot(time_filtered, data_filtered['tension_right_scaled'], label='Δ Voltage (Antagonist)', color='#1E3A8A')  # Dark Blue
axs[3].set_ylabel('Δ Voltage [mV]',fontsize=14)
axs[3].legend(loc='upper right',fontsize=12)
axs[3].grid(True)

# Pressure graph
axs[4].plot(time_filtered, data_filtered['pressure_left'], label='Pressure (Agonist)', color='#FFA500')  # Orange
axs[4].plot(time_filtered, data_filtered['pressure_right'], label='Pressure (Antagonist)', color='#1E3A8A')  # Dark Blue
axs[4].set_xlabel('Time [s]',fontsize=12)
axs[4].set_ylabel('Pressure [MPa]',fontsize=14)
axs[4].legend(loc='upper right',fontsize=12)
axs[4].grid(True)

# Adjust layout to minimize margins
plt.tight_layout(pad=0.5)
plt.subplots_adjust(left=0.07, right=0.99, top=0.99, bottom=0.04)

<<<<<<< HEAD
plt.savefig(r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\fig\reflex_all_model\20240819_r20_reflex_all_plt.pdf')
#plt.savefig(r'C:\Users\HosodaLab2\University\Reserch\reflex\SII_data_analysis\fig\reflex_all_model\20240819_r20_reflex_all_plt.pdf')
plt.show()
=======
# plt.savefig(r'C:\Users\ymilk\University\reserch\python\SII_data_analysis\fig\reflex_all_model\20240819_r20_reflex_all_plt.pdf')
# plt.savefig(r'C:\Users\HosodaLab2\University\Reserch\reflex\SII_data_analysis\fig\reflex_all_model\20240819_r20_reflex_all_plt.pdf')
plt.savefig(r'C:\Users\Mizuki\University\Reserch\reflex\python\fig\reflex_all_model\20240819_r20_reflex_all_plt.pdf')
plt.show()
>>>>>>> ae7708c8c90af95cbb84f325210d1e6bb494bbcd
