import streamlit as st
import segno

# Set tab title

st.set_page_config(page_title='Open QR', page_icon='openqr_tab_icon.png', layout='centered', initial_sidebar_state='auto')

st.title('Open QR')

st.write('This is a simple web app that generates QR codes from URLs.')
st.write('Enter a URL in the text box below and click the "Generate QR code" button to generate a QR code image.')

st.warning("All of the generating code is open-source. You can make sure yourself, that no data about your links or the generated QR codes are stored anywhere.")

url_input = st.text_input('Enter the URL of the QR code image:')

generate_button = st.button('Generate QR code')

if generate_button:
    qr_code = segno.make(url_input)
    data_uri = qr_code.png_data_uri(scale=10)
    st.image(data_uri, use_column_width=True)
