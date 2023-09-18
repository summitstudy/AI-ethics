import pandas as pd

def save(sex, age, person,quiz1,quiz2,quiz3):
    idx = len(pd.read_csv("database.csv"))
    new_df = pd.DataFrame({"sex":sex,
                           "age":age,
                           "person":person,
                           "quiz1":quiz1,
                           "quiz2":quiz2,
                           "quiz3":quiz3}, 
                          index = [idx])
    new_df.to_csv("database.csv",mode = "a", header = False)
    return None

def load_list():
    house_list = []
    df = pd.read_csv("database.csv")
    for i in range(len(df)):
        house_list.append(df.iloc[i].tolist())
    print(house_list)
    return house_list

def now_index():
    df = pd.read_csv("database.csv")
    return len(df)-1


def load_house(idx):
    df = pd.read_csv("database.csv")
    house_info = df.iloc[idx]
    return house_info


if __name__ =="__main__":
    load_list()