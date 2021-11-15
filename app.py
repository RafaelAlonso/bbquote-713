import streamlit as st
from bbquote.lib import get_quote

st.title('bbquote')
st.markdown('## Breaking Bad Quotes')
st.write(get_quote())