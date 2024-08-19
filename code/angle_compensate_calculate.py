import pandas as pd

# CSVファイルの読み込み
# df = pd.read_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_model.csv')
# df = pd.read_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_sensor.csv')
df = pd.read_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_without.csv')

# r1の最初のangleの値を基準にする
r1_initial_angle = df['20240819_w1_angle'].iloc[0]

# 補正後のデータを保存するための辞書を作成
adjusted_data = {}

for i in range(1, 21):
    # if i == 14:
    #     continue  # 14のときはスキップ
    
    #angle_col = f'20240819_r{i}_angle'
    #angle_col = f'20240819_f{i}_angle'
    angle_col = f'20240819_w{i}_angle'
    
    
    # 各データセットの最初のangleの値を取得
    initial_angle = df[angle_col].iloc[0]
    
    # オフセットを計算してangleデータを補正
    offset = r1_initial_angle - initial_angle
    adjusted_angle = df[angle_col] + offset
    
    # 補正したデータを辞書に保存
    adjusted_data[angle_col] = adjusted_angle

# 補正後のデータをデータフレームに変換
adjusted_df = pd.DataFrame(adjusted_data)

# 補正後のデータをCSVファイルとして保存
# adjusted_df.to_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_model.csv', index=False)
# adjusted_df.to_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_sensor.csv', index=False)
adjusted_df.to_csv(r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_adjusted_without.csv', index=False)
