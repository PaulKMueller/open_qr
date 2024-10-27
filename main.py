import streamlit as st
import segno

st.title('Open QR')

url_input = st.text_input('Enter the URL of the QR code image:')

generate_button = st.button('Generate QR code')

if generate_button:
    qr_code = segno.make(url_input)
    data_uri = qr_code.png_data_uri(scale=10)
    st.image(data_uri, use_column_width=True)
