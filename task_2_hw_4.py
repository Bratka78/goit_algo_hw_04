

def get_cats_info(path):
    cats = []
    try:
        with open(path,'r', encoding="utf-8") as pets:
            for i in pets:
                animal = i.strip().split(",")
                if len(animal) != 3:
                    continue
                id, name, age = animal
                if not age.isdigit():
                    continue
                cats.append({
                    "id": id,
                    "name": name,
                    "age": int(age)
                })
              
        return cats
    except FileNotFoundError:
        print("File not found")
        return []




cont = get_cats_info(r"C:\Users\Maksym\Desktop\my_projects\homework\goit_algo_hw_04\pats_info.txt")
print(cont)