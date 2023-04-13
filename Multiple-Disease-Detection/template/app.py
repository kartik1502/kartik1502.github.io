import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

loaded_model = pickle.load(open('models/trained_model.sav', 'rb'))

def parkinsons_prediction(input_data):
    input_data = np.asarray(input_data)

    input_data_reshaped = input_data.reshape(1, -1)

    result = loaded_model.predict(input_data_reshaped)

    if result[0] == 0:
        return "The person dose not have Parkinson's Disease"
    else:
        return "The person has Parkinson's Disease"
    
from io import BytesIO
from reportlab.pdfgen import canvas

def generate_report(diagnosis, input_data):
    buffer = BytesIO()  
    pdf = canvas.Canvas(buffer)  
    pdf.setTitle("Parkinson's Disease Prediction Report")  
    pdf.setFont("Helvetica", 12)  
    pdf.drawString(50, 750, "Parkinson's Disease Prediction Report")
    pdf.drawString(50, 700, f"Diagnosis: {diagnosis}")
    y = 650 
    for key, value in input_data.items():
        pdf.drawString(50, y, f"{key}: {value}")
        y -= 25
    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer

st.set_page_config(page_icon="https://img.icons8.com/fluency/48/null/caduceus.png", page_title="Multiple Disease Detection")
with st.sidebar:
    choice = option_menu('Multiple Disease Detection',['Parkinson\'s Disease','Chronic Kidney Disease'])

if choice == 'Parkinson\'s Disease':
    st.title("Parkinson's Disease Detection")
    
    default_value = ''
      

    with st.form("my_form"):
        col1, col2, col3, col4 = st.columns(4)

    with col1:
        Name =st.text_input('Name:')
        if Name.isalpha():
            pass
        else:
            st.write("Enter the valid name")
    with col2:
        Age = st.text_input('Age')
        if Age.isnumeric():
            try:
                if int(Age) <= 0:
                    st.write("Please enter valid input")
            except ValueError:
                st.write("Invalid input. Please enter valid number")
            pass
        else:
            st.write("Please enter a valid age")
    with col3:
        fo = st.text_input('MDVP: Fo(Hz)', default_value)
    with col4:
        fhi = st.text_input('MDVP: Fhi(Hz)', default_value)
    with col1:
        flo = st.text_input('MDVP: Flo(Hz)', default_value)
    with col2:
        Jitter_percent = st.text_input('MDVP: Jitter(%)', default_value)
    with col3:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)', default_value)
    with col4:
        RAP = st.text_input('MDVP: RAP', default_value)
    with col1:
        PPQ = st.text_input('MDVP: PPQ', default_value)
    with col2:
        DDP = st.text_input('Jitter: DDP', default_value)
    with col3:
        Shimmer = st.text_input('MDVP: Shimmer', default_value)
    with col4:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)', default_value)
    with col1:
        APQ3 = st.text_input('Shimmer: APQ3', default_value)
    with col2:
        APQ5 = st.text_input('Shimmer: APQ5', default_value)
    with col3:
        APQ = st.text_input('MDVP: APQ', default_value)
    with col4:
        DDA = st.text_input('Shimmer: DDA', default_value)
    with col1:
        NHR = st.text_input('NHR', default_value)
    with col2:
        HNR = st.text_input('HNR', default_value)
    with col3:
        RPDE = st.text_input('RPDE', default_value)
    with col4:
        DFA = st.text_input('DFA', default_value)
    with col1:
        spread1 = st.text_input('spread1', default_value)
    with col2:
        spread2 = st.text_input('spread2', default_value)
    with col3:
        D2 = st.text_input('D2', default_value)
    with col4:
        PPE = st.text_input('PPE', default_value)
    with col1:
        form_button = st.form_submit_button(label='Predict Disease')

    input_data = {
            'MDVP: Fo(Hz)': fo,
            'MDVP: Fhi(Hz)': fhi,
            'MDVP: Flo(Hz)': flo,
            'MDVP: Jitter(%)': Jitter_percent,
            'MDVP: Jitter(Abs)': Jitter_Abs,
            'MDVP: RAP': RAP,
            'MDVP: PPQ': PPQ,
            'Jitter: DDP': DDP, 
            'MDVP: Shimmer': Shimmer,
            'MDVP: Shimmer(dB)': Shimmer_dB,
            'Shimmer: APQ3': APQ3,
            'Shimmer: APQ5': APQ5,
            'MDVP: APQ': APQ,
            'Shimmer: DDA': DDA,
            'NHR': NHR,
            'HNR': HNR,
            'RPDE': RPDE,
            'DFA': DFA,
            'spread1': spread1,
            'spread2': spread2,
            'D2': D2,
            'PPE': PPE
        }

    diagnosis = ''
    if all([fo.replace('-', '').replace('.', '').isdigit(), 
            fhi.replace('-', '').replace('.', '').isdigit(),
            flo.replace('-', '').replace('.', '').isdigit(),
            Jitter_percent.replace('-', '').replace('.', '').isdigit(),
            Jitter_Abs.replace('-', '').replace('.', '').isdigit(),
            RAP.replace('-', '').replace('.', '').isdigit(),
            PPQ.replace('-', '').replace('.', '').isdigit(),
            DDP.replace('-', '').replace('.', '').isdigit(),
            Shimmer.replace('-', '').replace('.', '').isdigit(),
            Shimmer_dB.replace('-', '').replace('.', '').isdigit(),
            APQ3.replace('-', '').replace('.', '').isdigit(),
            APQ5.replace('-', '').replace('.', '').isdigit(),
            APQ.replace('-', '').replace('.', '').isdigit(),
            DDA.replace('-', '').replace('.', '').isdigit(),
            NHR.replace('-', '').replace('.', '').isdigit(),
            HNR.replace('-', '').replace('.', '').isdigit(),
            RPDE.replace('-', '').replace('.', '').isdigit(),
            DFA.replace('-', '').replace('.', '').isdigit(),
            spread1.replace('-', '').replace('.', '').isdigit(),
            spread2.replace('-', '').replace('.', '').isdigit(),
            D2.replace('-', '').replace('.', '').isdigit(),
            PPE.replace('-', '').replace('.', '').isdigit()]):
        if form_button:
            diagnosis = parkinsons_prediction([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE])
            st.success(diagnosis)
            pdf_buffer = generate_report(diagnosis, input_data)
            st.download_button(label="Download Report", data=pdf_buffer.getvalue(), file_name=f"{Name}.pdf", mime="application/pdf")
    
    else:
        st.write("Please enter valid Input")
