import streamlit as st
import random

# Title of the app
st.title("Rock, Paper, Scissors Game")

# Subheading
st.subheader("Choose your move!")

# User's choice
user_choice = st.radio("Pick one:", ("Rock", "Paper", "Scissors"))

# Function to determine winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Generate computer's choice
if st.button("Play"):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    st.write(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    st.write(result)

# Footer
st.caption("Enjoy playing!")