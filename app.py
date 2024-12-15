import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# File to store the default prompt
PROMPT_FILE = "default_prompt.txt"

# Load the default prompt from the file if it exists
if os.path.exists(PROMPT_FILE):
    with open(PROMPT_FILE, "r", encoding="utf-8") as file:
        default_prompt = file.read()
else:
    # Initial default prompt if the file doesn't exist
    default_prompt = """Παρακαλώ αξιολογήστε την παρακάτω εργασία ακολουθώντας τα εξής κριτήρια:
    Μορφολογικές πτυχές του κειμένου: Παρουσία περιεχομένων, Διάρθρωση του κύριου μέρους σε επιμέρους ενότητες, Διατύπωση σαφών συμπερασμάτων, Χρήση και παράθεση βιβλιογραφίας κατά το οποίο πρέπει για κάθε αναφορά στη Βιβλιογραφία να υπάρχει η σχετική παραπομπή στους συγγραφείς μέσα στο κείμενο.
    Περιεχόμενο και ποιότητα ανάλυσης: Σαφής και καλά οργανωμένη δομή με διαχωρισμό του περιεχομένου σε ξεκάθαρες ενότητες όπου κάθε ενότητα αναλύει μία έννοια, Επαρκής και τεκμηριωμένη επιχειρηματολογία, Ορθή χρήση και ακριβής γραφή επιστημονικής ορολογίας
    Ποιοτική ερμηνεία συναφών θεμάτων, Γλωσσική σαφήνεια και ακρίβεια.
    Παραθέστε την αξιολόγησή σε ένα κείμενο έκτασης 15 σειρών, με επιστημονικό ύφος εντοπίζοντας τα θετικά και τα αρνητικά της σημεία και στο τέλος, αποδώστε έναν συνολικό βαθμό με άξονα βαθμολόγησης από το 0,1 έως το 1.
    """
    # Save the initial prompt to the file
    with open(PROMPT_FILE, "w", encoding="utf-8") as file:
        file.write(default_prompt)

# Input field for the instructions prompt
with st.expander("Instructions"):
    prompt = st.text_area("Instructions", value=default_prompt, height=500)

# Button to save the current prompt value as default
if st.button("Save Prompt as Default"):
    with open(PROMPT_FILE, "w", encoding="utf-8") as file:
        file.write(prompt)
    st.success("Prompt saved as default! This will persist after refreshing the page.")

# Assignment input area
assignment = st.text_area("Paste the assignment here", height=200)

# Button to evaluate the assignment
if st.button("Submit"):
    if assignment.strip() == "":
        st.warning("Please paste the assignment before submitting!")
    else:
        try:
            completion = client.chat.completions.create(
                model="o1-preview",
                messages=[
                    {
                        "role": "user",
                        "content": f"Follow the given instructions: {prompt}\nEvaluate the following assignment:\n{assignment}",
                    }
                ],
            )
            st.markdown(completion.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
