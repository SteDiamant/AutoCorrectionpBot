from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()
import streamlit as st

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),)

prompt = st.text_area("Instructions",
                      height=500,
placeholder=
"""Παρακαλώ αξιολογήστε την παρακάτω εργασία ακολουθώντας τα εξής κριτήρια:
Μορφολογικές πτυχές του κειμένου:
Παρουσία περιεχομένων
Διάρθρωση του κύριου μέρους σε επιμέρους ενότητες
Διατύπωση σαφών συμπερασμάτων
Χρήση και παράθεση βιβλιογραφίας
Περιεχόμενο και ποιότητα ανάλυσης:
Σαφής και καλά οργανωμένη δομή του περιεχομένου
Επαρκής και τεκμηριωμένη επιχειρηματολογία
Ορθή χρήση και ακριβής γραφή επιστημονικής ορολογίας
Ποιοτική ερμηνεία συναφών θεμάτων
Γλωσσική σαφήνεια και ακρίβεια
Παραθέστε την αξιολόγησή σας σε ένα κείμενο έκτασης 15 σειρών, με επιστημονικό ύφος. Στο τέλος, αποδώστε έναν συνολικό βαθμό με άξονα βαθμολόγησης από το 0,1 έως το 1.
""")

assignment = st.text_area("Paste the assignment here",height=200)

if st.button("Submit"):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": f"{prompt}\n{assignment}"}
        ]
    )
    st.write(completion.choices[0].message.content)