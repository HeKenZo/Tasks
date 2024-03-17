import os
import json


def collect_tbt_values(folder_path):
    tbt_data = {}
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            tbt_values = extract_tbt_values(file_path)
            if tbt_values:
                tbt_data[file_name] = tbt_values
    return tbt_data


def extract_tbt_values(file_path):
    tbt_values = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for key, value in data.items():
            if isinstance(value, str) and value.startswith('TBT:'):
                tbt_values[key] = value
    return tbt_values


def write_result_file(tbt_data, result_file_path):
    with open(result_file_path, 'w', encoding='utf-8') as result_file:
        json.dump(tbt_data, result_file, indent=4, ensure_ascii=False)


def main():
    translations_folder_path = 'translations'

    tbt_data = collect_tbt_values(translations_folder_path)
    print(tbt_data)

    result_file_path = 'result_file.json'
    write_result_file(tbt_data, result_file_path)
    print(f"Result file '{result_file_path}' has been generated.")


if __name__ == "__main__":
    main()
