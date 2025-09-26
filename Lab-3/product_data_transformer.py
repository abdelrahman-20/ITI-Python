# 4) Product Data Transformer (lambda, map, filter, zip)
#    - Ask user for a list of product names (comma-separated).
#    - Ask user for a list of product prices (comma-separated).
#    - Process them by:
#         - Pairing product with price.
#         - Filtering out items where price <= 0.
#         - Transforming each pair into a dictionary {"product": name, "price": price, "discounted": price * 0.9}.
#    - Save the final result as JSON into "products.json".
#    - Print a preview of the first 5 results.

import json


def product_data_transformer():
    while True:
        # Get Product Names And Prices As Input:
        product_names = input("Enter product names (comma-separated): ").split(",")
        product_prices = input("Enter product prices (comma-separated): ").split(",")

        try:
            prices = list(map(float, product_prices))
        except ValueError:
            print("Invalid price input. Please enter numeric values.")
            continue

        # Pair Each Product With Its Price
        product_pairs = zip(product_names, prices)

        # Filter The Prices:
        filtered_products = filter(lambda x: x[1] > 0, product_pairs)

        # Final Result In Dictionaries
        result = list(
            map(
                lambda x: {
                    "product": x[0].strip().lower(),
                    "price": round(x[1], 2),
                    "discountedF": round(x[1] * 0.9, 2),
                },
                filtered_products,
            )
        )

        # Save Results in JSON File
        with open("products.json", "w") as jsonFile:
            json.dump(result, jsonFile)

        # Print a preview of the first 5 results
        print("Preview of the first 5 products:")
        for product in result[:5]:
            print(product)


if __name__ == "__main__":
    product_data_transformer()
