import json
import csv

def write_available_products(products, fields):
    with open("available_products.csv", "w") as fd:
        writer = csv.DictWriter(fd, fields)
        writer.writeheader()
        writer.writerows(products)

def load_data():
    data = json.load(open("data.json"))
    available_products = []
    for bundle in data["Bundles"]:
        if not bundle.get("Products") or len(bundle["Products"]) == 0:
            print("error, no clue to product availability")
            continue
        if bundle["Products"][0].get("IsAvailable") is None:
            print("error, no clue to product availability")
            continue
        if bundle["Products"][0]["IsAvailable"] == True:
            available_products.append({
                "Name": bundle["Name"],
                "Stockcode": bundle["Products"][0]["Stockcode"],
                "Barcode": bundle["Products"][0]["Barcode"],
                "Price": round(float(bundle["Products"][0]["Price"]), 1)
            })
            print("You can buy {} at our store at {}".format(
                bundle["Name"][:30],
                round(float(bundle["Products"][0]["Price"]), 1)
            ))
            continue

        print("Not available {} ({})".format(
            bundle["Products"][0]["Stockcode"],
            bundle["Name"][:30]
        ))
    write_available_products(available_products, ["Name", "Stockcode", "Barcode", "Price"])

def main():
    load_data()

if __name__ == "__main__":
    main()