import streamlit as st
from bbquote.lib import get_quote

st.markdown('## Breaking Bad Quotes')
st.write(get_quote())