import json
import csv


def clean_data(data):
    default_values = {
        'id': '',
        'name': '',
        'category': '',
        'price': 0.0,
        'currency': '',
        'stock': 0,
        'description': '',
        'manufacturer': '',
        'warranty': ''
    }

    cleaned_data = []
    for product in data:
        cleaned_product = {}
        for key, default_value in default_values.items():
            cleaned_product[key] = product.get(key, default_value)

        cleaned_product['price'] = float(cleaned_product['price'])
        if cleaned_product['stock'] is not None:
            cleaned_product['stock'] = int(cleaned_product['stock'])

        cleaned_data.append(cleaned_product)

    return cleaned_data


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


def main():
    with open('electronics_products.json', 'r', encoding='utf-8') as file:
        data = json.load(file)['data']

    cleaned_data = clean_data(data)

    save_to_csv(cleaned_data, 'electronics_products_cleaned.csv')
    print("CSV file has been created successfully.")


if __name__ == "__main__":
    main()
