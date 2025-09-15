import streamlit as st
import subprocess
from utils import log_command

st.title("🚀 CommandHub - Central Command & Tool Platform")

command = st.text_input("Enter the system command:")

if st.button("Execute"):
    if command:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            st.success("✅ Command executed successfully!")
            st.text_area("Output:", result.stdout)
            log_command(command)
        except subprocess.CalledProcessError as e:
            st.error(f"❌ Error:\n{e.stderr}")
    else:
        st.warning("⚠️ Please enter a valid command.")
