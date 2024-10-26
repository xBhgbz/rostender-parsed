import csv

def load_into_csv(tenders: list, write_header):
    """Загружает словарь с информацией о тендерах в csv"""
    with open("parsed_tenders.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=list(tenders[0].keys()), quoting=csv.QUOTE_NONNUMERIC
        )
        if write_header:
            writer.writeheader()

        for tender in tenders:
            writer.writerow(tender)