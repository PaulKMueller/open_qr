import streamlit as st
import segno

# Set tab title

st.set_page_config(page_title='Open QR', page_icon='openqr_tab_icon.png', layout='centered', initial_sidebar_state='auto')

st.title('Open QR')

url_input = st.text_input('Enter the URL of the QR code image:')

generate_button = st.button('Generate QR code')

if generate_button:
    qr_code = segno.make(url_input)
    data_uri = qr_code.png_data_uri(scale=10)
    st.image(data_uri, use_column_width=True)
