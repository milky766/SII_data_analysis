import pandas as pd
import glob
import os

# CSVファイルのパスを取得（20個のCSVファイルを対象）
file_paths = glob.glob(r'C:\Users\Mizuki\University\Reserch\reflex\control_board_Mizuki\data\adapt\reflex_with_model\*.csv')
# file_paths = glob.glob(r'C:\Users\Mizuki\University\Reserch\reflex\control_board_Mizuki\data\adapt\reflex_with_sensor\*.csv')

# 出力用のCSVファイル名
output_file_path = r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_model.csv'
# output_file_path = r'C:\Users\Mizuki\University\Reserch\reflex\python\data\combined_output_angle_sensor.csv'

# m5_Ia_model_+列が初めて0以外になったところを特定する関数
def find_first_nonzero_index(df, column_name='m5_Ia_model_+'):
#def find_first_nonzero_index(df, column_name='m5_Ia_+'):
    nonzero_indices = df[df[column_name] != 0].index
    
    if len(nonzero_indices) > 0:
        first_nonzero_index = nonzero_indices[0]
    else:
        first_nonzero_index = len(df) - 1  # 条件を満たさない場合は最後の行を使用
    
    return first_nonzero_index

# 全てのデータをまとめるリスト
all_data = []

# 各ファイルに対して処理を行う
for file_path in file_paths:
    df = pd.read_csv(file_path)
    
    # 初めて0以外になった場所のインデックスを特定
    first_nonzero_index = find_first_nonzero_index(df)
    
    # i-50 ~ i+300のデータを抽出
    start_index = max(0, first_nonzero_index - 50)
    end_index = first_nonzero_index + 300
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
combined_data = combined_data.iloc[:, :-1]

# 1つのCSVファイルに書き出し
combined_data.to_csv(output_file_path, index=False)

print(f"Data from {len(file_paths)} files has been combined into {output_file_path} with gaps.")
