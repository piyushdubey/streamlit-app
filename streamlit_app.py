import streamlit as st
import mymodel as m

st.write("""
# Expenses
""")

st.write(m.run(window=15))

window = st.slider("Test Slider")
st.write(m.run(window=window))