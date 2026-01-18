from pathlib import Path

def total_salary(path: str) -> tuple:
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as fh:
            try:
                for i in fh:
                    key, value = i.strip().split(",")
                    total += int(value)
                    count += 1
            except ValueError:
                    print(f"Error in line: {i.strip()} .")
                    return []
            if count == 0:
                print("Empty file")
                return []
            average_salary = round(total / count, 2)
            return total, average_salary
        
    except FileNotFoundError:
        print("File not found")
        return []
            

cont = total_salary(r"C:\Users\Maksym\Desktop\my_projects\homework\goit_algo_hw_04\price.txt")
print(cont)
