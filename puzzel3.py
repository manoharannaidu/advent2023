import pandas as pd

max_balls = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

filename = "./inputs/puzzel3_input.txt"

df = (
    pd.DataFrame(
        [
            line
            .replace("\n", "")
            .replace(":", ",")
            .replace(";", ",")
            .split(",")
             for line in open(filename)
        ]
    ).assign(
        id = lambda df: df[0].str.replace("Game ", ""),
    )
    .drop([0], axis=1)
    .set_index("id")
)

drop_idx = []
for idx, row in df.iterrows():
    for col in row.index:
        substr = str(row[col]).strip().split(" ")
        if "blue" in substr:
            if int(substr[0]) > 14:
                drop_idx.append(int(idx))
        if "red" in substr:
            if int(substr[0]) > 12:
                drop_idx.append(int(idx))
        if "green" in substr:
            if int(substr[0]) > 13:
                drop_idx.append(int(idx))

if __name__ == "__main__":
    print(sum(set(df.index.astype(int)) - set(drop_idx)))
