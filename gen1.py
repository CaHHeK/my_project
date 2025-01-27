import os
import json

# Основная функция генерации файлов
def generate_city_files(template_file, cities_file, output_dir):
    # Чтение HTML-шаблона
    with open(template_file, "r", encoding="utf-8") as file:
        template_content = file.read()

    # Чтение словаря городов из JSON
    with open(cities_file, "r", encoding="utf-8") as file:
        cities = json.load(file)

    # Создание папки для результатов, если ее еще нет
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Генерация HTML-файлов для каждого города
    for city_rus, city_folder_name in cities.items():
        # Создание папки для города
        city_dir = os.path.join(output_dir, city_folder_name)
        os.makedirs(city_dir, exist_ok=True)

        # Замена placeholder на название города
        city_content = template_content.replace("$location$",
                                                f"{city_rus}")

        # Сохранение результата в индексный файл
        output_file = os.path.join(city_dir, "index.html")
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(city_content)

    print(f"Файлы успешно сгенерированы в папке {output_dir}")
 
 

# Настройка путей
template_file_path = "index.html"  # Путь к исходному HTML-файлу
cities_file_path = "cities.json"  # Путь к JSON-файлу с городами
output_directory = "output"  # Папка для сохранения результатов

# Запуск функции
generate_city_files(template_file_path, cities_file_path, output_directory)
