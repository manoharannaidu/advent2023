import pandas as pd

filename = "./inputs/day4_test_input.txt"
# filename = "./inputs/day4_input.txt"

df = (
    pd.DataFrame(
        [
            line
            .replace("\n", "")
            .replace("Card ", "")
            .replace(":", "|")
            .split("|")
             for line in open(filename)
        ]
    ).set_index([0])
)

print(df)

# sum = 0
for idx, row in df.iterrows():
    winning_nums = str(row[1]).strip().split(" ")
    winning_nums = [
        num 
         for num in winning_nums
         if num != ""
    ]
    my_nums = str(row[2]).strip().split(" ")
    my_nums = [
        num 
         for num in my_nums
         if num != ""
    ]
    # print(my_nums)
    wins = set(my_nums).intersection(set(winning_nums))
    print(wins)
#     wins = wins - set("")
#     if (len(wins) != 0):
#         # print(len(wins))
#         # print(f"{wins}", (2**(len(wins) - 1)))
#         sum = sum + (2 ** (len(wins) - 1))
#
# print(sum)
