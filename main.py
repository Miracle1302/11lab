import csv


def read_and_process_csv(input_filename, output_filename):
    try:
        # Відкриття вихідного файлу для читання
        with open(input_filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = []
            min_value = float('inf')
            max_value = float('-inf')
            min_country = ""
            max_country = ""

            # Читання даних та пошук мінімальних та максимальних значень
            for row in reader:
                country = row['Country']
                export_percent = row['Exports of goods and services (% of GDP) 2019']
                if export_percent:
                    value = float(export_percent)
                    data.append((country, value))
                    # Оновлення мінімального та максимального значень
                    if value < min_value:
                        min_value = value
                        min_country = country
                    if value > max_value:
                        max_value = value
                        max_country = country

            # Вивід на екран усіх даних
            for country, value in data:
                print(f"{country}: {value}")

        # Запис мінімальних та максимальних значень у новий файл
        with open(output_filename, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Description', 'Country', 'Value'])
            writer.writerow(['Lowest Exports (% of GDP)', min_country, min_value])
            writer.writerow(['Highest Exports (% of GDP)', max_country, max_value])

    except FileNotFoundError:
        print("Error: File not found.")
    except IOError as e:
        print(f"IO Error: {e}")


# Виклик функції з назвами файлів
input_csv = 'input_data.csv'
output_csv = 'output_results.csv'
read_and_process_csv(input_csv, output_csv)

