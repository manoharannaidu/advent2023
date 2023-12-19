import pandas as pd

max_balls = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

# filename = "./inputs/puzz3_test_input.txt"
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

blue_dict = {}
red_dict = {}
green_dict = {}
for idx, row in df.iterrows():
    max_blue = []
    max_red = []
    max_green = []
    for col in row.index:
        substr = str(row[col]).strip().split(" ")
        if substr[0] != "None":
            if (substr[1] == "blue"):
                max_blue.append(int(substr[0]))
            if substr[1] == "red":
                max_red.append(int(substr[0]))
            if substr[1] == "green":
                max_green.append(int(substr[0]))
    blue_dict[idx] = max(max_blue)
    red_dict[idx] = max(max_red)
    green_dict[idx] = max(max_green)

if __name__ == "__main__":
    sum = 0
    for b, r, g in zip(blue_dict.values(), red_dict.values(), green_dict.values()):
        sum = sum + (b * r * g)

    print(sum)
