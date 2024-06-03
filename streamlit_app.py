import streamlit as st
from st_paywall import add_auth

st.set_page_config(layout="wide")
st.title("The most Fantabulous SaaS Ever! 🚀")

add_auth(required=True)

st.write(f"Subscription Status: {st.session_state.user.subscribed}")
st.write("🎉 Yay! You're all set and subscribed! 🎉")
st.write(f"By the way, your email is: {st.session_state.email}")



