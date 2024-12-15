from openai import OpenAI
import os

import streamlit as st

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),)
with st.expander("Instructions"):
    prompt = st.text_area("Instructions",
                        height=500,
    value=
    """Παρακαλώ αξιολογήστε την παρακάτω εργασία ακολουθώντας τα εξής κριτήρια:
    Μορφολογικές πτυχές του κειμένου: Παρουσία περιεχομένων, Διάρθρωση του κύριου μέρους σε επιμέρους ενότητες, Διατύπωση σαφών συμπερασμάτων, Χρήση και παράθεση βιβλιογραφίας κατά το οποίο πρέπει για κάθε αναφορά στη Βιβλιογραφία να υπάρχει η σχετική παραπομπή στους συγγραφείς μέσα στο κείμενο.
    Περιεχόμενο και ποιότητα ανάλυσης: Σαφής και καλά οργανωμένη δομή με διαχωρισμό του περιεχομένου σε ξεκάθαρες ενότητες όπου κάθε ενότητα αναλύει μία έννοια, Επαρκής και τεκμηριωμένη επιχειρηματολογία, Ορθή χρήση και ακριβής γραφή επιστημονικής ορολογίας
    Ποιοτική ερμηνεία συναφών θεμάτων, Γλωσσική σαφήνεια και ακρίβεια.
    Παραθέστε την αξιολόγησή σε ένα κείμενο έκτασης 15 σειρών, με επιστημονικό ύφος εντοπίζοντας τα θετικά και τα αρνητικά της σημεία και στο τέλος, αποδώστε έναν συνολικό βαθμό με άξονα βαθμολόγησης από το 0,1 έως το 1.

    """)

assignment = st.text_area("Paste the assignment here",height=200)

if st.button("Submit"):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": f"Follow the given instruction{prompt}In order to evaluate the following assignment.\n{assignment}"}
        ]
    )
    with st.container(border=True):
        st.markdown(completion.choices[0].message.content)
        
