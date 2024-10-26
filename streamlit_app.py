import streamlit as st
import pandas as pd

from tender_parser.categories import Categories
from tender_parser.parser import get_tenders_from_rostender

st.set_page_config(page_title="Авиационные тендеры", layout="wide")
get_tenders_from_rostender(Categories.get_tenders_fields(), "24.10.2024", "24.10.2024")

table = pd.read_csv("parsed_tenders.csv", delimiter=',')
st.title("Авиационные тендеры с сайта rostender.info")

st.table(table)
