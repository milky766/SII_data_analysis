import pandas as pd
import glob
import os

# CSVファイルのパスを取得
file_paths = glob.glob(r'C:\Users\Mizuki\University\Reserch\reflex\control_board_Mizuki\data\adapt\without_reflex\*.csv')

# 出力用のCSVファイル名
output_file_path = r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_without.csv'

# ms_speed_left_modelが最大値を取った場所を特定する関数
def find_max_speed_index(df, column_name='ms_speed_left_model'):
    max_index = df[column_name].idxmax()
    return max_index

# 全てのデータをまとめるリスト
all_data = []

# 各ファイルに対して処理を行う
for file_path in file_paths:
    df = pd.read_csv(file_path)
    
    # ms_speed_left_modelが最大値を取った場所のインデックスを特定
    max_speed_index = find_max_speed_index(df)
    
    # i-50 ~ i+300のデータを抽出
    start_index = max(0, max_speed_index - 50)
    end_index = max_speed_index + 300
    extracted_data = df.iloc[start_index:end_index][['count', 'angle']]
    
    # ファイル名からラベルを作成
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    extracted_data.columns = [f'{base_name}_count', f'{base_name}_angle']
    
    # リストに追加
    all_data.append(extracted_data.reset_index(drop=True))
    
    # 空のデータフレームをリストに追加して、間に空列を挿入
    all_data.append(pd.DataFrame({'': [''] * len(extracted_data)}))

# 各ファイルのデータを横に結合する（インデックスを基準に）
combined_data = pd.concat(all_data, axis=1)

# 余分な空列を除去（最後に追加される空の列を除去）
combined_data.to_csv(output_file_path, index=False)

print(f"Data from {len(file_paths)} files has been combined into {output_file_path} with gaps.")
