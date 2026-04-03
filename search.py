import os

# Мой первый мини-поисковик
# Ищет слово во всех текстовых файлах в папке

def search(folder, query):
    results = []
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            with open(os.path.join(folder, filename), "r", encoding="utf-8") as f:
                text = f.read()
                if query.lower() in text.lower():
                    results.append(filename)
    return results

query = input("Что ищем? ")
found = search(".", query)

if found:
    print(f"Найдено в {len(found)} файлах:")
    for f in found:
        print(f"  - {f}")
else:
    print("Ничего не найдено")
