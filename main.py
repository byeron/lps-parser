import pandas as pd
import os

if __name__ == "__main__":
    output_dir = "output"

    # data dir内のcsvファイルを読み込む
    files = os.listdir("data")
    for file in files:
        path = os.path.join("data", file)
        df = pd.read_csv(path, index_col=0, header=0)

        # index名を-で分割し、0番目の要素を取得
        df.index = df.index.str.split("-").str[0]
        print(df)

        # output dirにcsvファイルを保存
        output_name = file.split(".")[0]
        output_name = output_name.split("-")[0] + "_" + output_name.split("-")[1].split("_")[1] + ".csv"
        output_path = os.path.join(output_dir, output_name)
        print(f"output_path: {output_path}")
        df.to_csv(output_path)
