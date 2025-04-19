import streamlit as st

def main():
    st.title("BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI) easily.")

    # Get user inputs
    weight = st.number_input("Enter your weight in kilograms:", min_value=0.0, step=0.1, format="%.2f")
    height_cm = st.number_input("Enter your height in centimeters:", min_value=0.0, step=0.1, format="%.2f")
    
    # When the button is clicked
    if st.button("Calculate BMI"):
        if height_cm > 0:
            # Convert height to meters
            height_m = height_cm / 100
            # Calculate BMI
            bmi = weight / (height_m ** 2)
            st.write(f"Your BMI is **{bmi:.2f}**")
            
            # Provide a simple interpretation
            if bmi < 18.5:
                st.write("You are underweight.")
            elif bmi < 25:
                st.write("You have a normal weight.")
            elif bmi < 30:
                st.write("You are overweight.")
            else:
                st.write("You are obese.")
        else:
            st.error("Please enter a valid height greater than zero.")

if __name__ == '__main__':
    main()