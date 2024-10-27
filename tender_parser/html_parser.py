from bs4 import BeautifulSoup as bs

# number description date-start date-finish address price customer category


def parsing_tenders(source_data) -> list:
    """Парсит страницу html и возвращает данные о тендерах"""

    soup = bs(source_data, "html.parser")
    tenders_info = []

    tenders = soup.find_all("div", class_="tender-row__wrapper")
    for tender in tenders:
        number = (
            tender.find("span", class_="tender__number")
            .get_text(strip=True)
            .replace("\xa0", " ")
            .split("№")[1] if tender.find("span", class_="tender__number") else ""
        )
        description = (
            tender.find("a", class_="tender-info__description")
            .get_text(strip=True)
            .replace("\xa0", " ") if tender.find("a", class_="tender-info__description") else ""
        )
        date_start = (
            tender.find("span", class_="tender__date-start")
            .get_text(strip=True)
            .replace("\xa0", " ").split(" ")[1] if tender.find("span", class_="tender__date-start") else ""
        )
        date_finish = (
            tender.find("span", class_="tender__countdown-text")
            .get_text(strip=True)
            .replace("\xa0", " ")
            .split(")")[1] if tender.find("span", class_="tender__countdown-text") else ""
        )
        address = (
            tender.find("div", class_="tender-address")
            .get_text(strip=True)
            .replace("\xa0", " ") if tender.find("div", class_="tender-address") else ""
        )
        price = (
            tender.find("div", class_="starting-price__price")
            .get_text(strip=True)
            .replace("\xa0", " ")
            .split(" ₽")[0] if tender.find("div", class_="starting-price__price") else ""
        )
        category = (
            tender.find("a", class_="list-branches__link")
            .get_text(strip=True)
            .replace("\xa0", " ") if tender.find("a", class_="list-branches__link") else ""
        )

        try:
            if len(date_start) > 10:
                date_start = date_start[:10] + " " + date_start[10:]
            if len(date_finish) > 10:
                date_finish = date_finish[:10] + " " + date_finish[10:]
            info = {
                "Номер": number,
                "Название": description,
                "Дата создания": date_start,
                "Дата окончания": date_finish,
                "Адрес": address,
                "Начальная цена": price,
                "Отрасли": category,
            }

            tenders_info.append(info)

        except AttributeError:
            continue

    return tenders_info
