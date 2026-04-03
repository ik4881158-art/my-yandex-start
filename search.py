import os

def search(folder, query):
    results = []
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            with open(os.path.join(folder, filename), "r", encoding="utf-8") as f:
                text = f.read()
                # считаем сколько раз слово встречается
                count = text.lower().count(query.lower())
                if count > 0:
                    results.append((filename, count))
    
    # сортируем - кто больше упоминает, тот выше
    results.sort(key=lambda x: x[1], reverse=True)
    return results

query = input("Что ищем? ")
found = search(".", query)

if found:
    print(f"\nНайдено в {len(found)} файлах:\n")
    for i, (filename, count) in enumerate(found, 1):
        print(f"  #{i} {filename} — упоминаний: {count}")
else:
    print("Ничего не найдено")
