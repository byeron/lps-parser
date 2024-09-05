import pandas as pd


if __name__ == "__main__":
    a = pd.read_csv("data/230927-1_LPS-4.csv", index_col=0, header=0)
    b = pd.read_csv("data/231212-1_LPS-4.csv", index_col=0, header=0)
    c = pd.read_csv("data/240328-1_LPS-4.csv", index_col=0, header=0)

    # a のindexを230927(重複あり)にする
    a.index = ["230927" for _ in range(len(a))]

    # b のindexを231212(重複あり)にする
    b.index = ["231212" for _ in range(len(b))]

    # c のindexを240328(重複あり)にする
    c.index = ["240328" for _ in range(len(c))]

    # 3つのデータを結合
    df = pd.concat([a, b, c])

    # 保存
    df.to_csv("output/eachday.csv")
