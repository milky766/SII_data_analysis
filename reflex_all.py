import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:\\Users\\Mizuki\\University\\Reserch\\reflex\\python\\data\\20240813_14.csv'
data = pd.read_csv(file_path)

pressure_columns = ['pressure_right', 'pressure_left']
tension_columns = ['tension_right', 'tension_left']
ms_speed_columns = ['ms_speed_right_model', 'ms_speed_left_model']
ms_model_columns = ['ms_right_model', 'ms_left_model']
angle_column = ['angle']

initial_angle = data['angle'].iloc[0]
data['angle_adjusted'] = data['angle'] - initial_angle
data['tension_left_adjusted']= -data['tension_left']

# Selecting the relevant columns for each plot

# Plotting the graphs
fig, axs = plt.subplots(5, 1, figsize=(10, 15))
time_adjusted = data['count'] / 100

# # Joint angle graph
# axs[0].plot(time_adjusted , data['angle_adjusted'], label='Angle', color='green')
# # axs[4].set_title('Joint Angle')
# axs[0].set_ylabel('Angle [deg]')
# axs[0].legend(loc='upper left')
# axs[0].grid(True)

# # Muscle stretch speed graph
# axs[1].plot(time_adjusted , data['ms_speed_right_model'], label='Estimated Velocity (Antagonist)', color='blue')
# axs[1].plot(time_adjusted , data['ms_speed_left_model'], label='Estimated Velocity (Agonist)', color='red')
# # axs[1].set_title('Muscle Stretch Speed')
# axs[1].set_ylabel('Estimated Velocity [mm/s]')
# axs[1].legend(loc='upper left')
# axs[1].grid(True)

# # Muscle model graph
# axs[2].plot(time_adjusted , data['ms_right_model'], label='Estimated Length (Antagonist)', color='blue')
# axs[2].plot(time_adjusted , data['ms_left_model'], label='Estimated Length (Agonist)', color='red')
# # axs[2].set_title('Estimated Length')
# axs[2].set_ylabel('Estimated Length [mm]')
# axs[2].legend(loc='upper left')
# axs[2].grid(True)

# # Tension graph
# axs[3].plot(time_adjusted , data['tension_right'], label='Δ Voltage (Antagonist)', color='blue')
# axs[3].plot(time_adjusted , data['tension_left_adjusted'], label='Δ Voltage (Agonist)', color='red')
# # axs[3].set_title('Muscle Stretch Speed')
# axs[3].set_ylabel('Δ Voltage [mV]')#多分mVではない ワンさんに確認
# axs[3].legend(loc='upper left')
# axs[3].grid(True)

# # Pressure graph
# axs[4].plot(time_adjusted , data['pressure_right'], label='Pressure (Antagonist)', color='blue')
# axs[4].plot(time_adjusted , data['pressure_left'], label='Pressure (Agonist)', color='red')
# # axs[4].set_title('Pressure')
# axs[4].set_xlabel('Time [s]')
# axs[4].set_ylabel('Pressure [MPa]')
# axs[4].legend(loc='upper left')
# axs[4].grid(True)


# plt.tight_layout(pad=3.0)
# plt.show()


# 時間を調整 (12秒から14秒の範囲)
mask = (time_adjusted >= 12) & (time_adjusted <= 13)

# データをフィルタリング
data_filtered = data[mask]
time_filtered = time_adjusted[mask]


# Joint angle graph
axs[0].plot(time_filtered, data_filtered['angle_adjusted'], label='Angle', color='green')
axs[0].set_ylabel('Angle [deg]')
axs[0].legend(loc='upper right')
axs[0].grid(True)

# Muscle stretch speed graph
axs[1].plot(time_filtered, data_filtered['ms_speed_right_model'], label='Estimated Velocity (Antagonist)', color='blue')
axs[1].plot(time_filtered, data_filtered['ms_speed_left_model'], label='Estimated Velocity (Agonist)', color='red')
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
plt.savefig('C:\\Users\\Mizuki\\University\\Reserch\\reflex\\python\\fig\\reflex_all.pdf')
plt.show()