import streamlit as st
import pandas as pd

from tender_parser.categories import Categories
from tender_parser.parser import get_tenders_from_rostender

st.set_page_config(page_title="Авиационные тендеры", layout="wide")
st.title("Авиационные тендеры с сайта rostender.info")

st.subheader("Настройки поиска тендеров")
st.text("Дата создания")
left, right = st.columns(2)
date_to = left.date_input("От")
date_from = right.date_input("До")

options = Categories.get_tenders_fields()
result = st.multiselect("Отрасли тендеров", options, placeholder="Выберите несколько опций")

left1, right1 = st.columns(2)
if left1.button("Поиск"):
    if len(result) == 0:
        st.markdown("Отрасли не выбраны.")
    else:
        with st.spinner('Получаем тендеры...'):
            get_tenders_from_rostender(result, date_to.strftime("%d.%m.%Y"), date_from.strftime("%d.%m.%Y"))
        try:
            table = pd.read_csv("parsed_tenders.csv", delimiter=',')
        except:
            st.markdown("Тендеры не найдены.")
        else:
            st.table(table)
            with open('parsed_tenders.csv') as f:
                right1.download_button('Скачать CSV', f,  file_name='tenders.csv')  # Defaults to 'text/plain'
