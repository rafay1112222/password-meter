import re
import streamlit as st
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 2  # More weight for longer passwords
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Make your password at least 12 characters long.")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    common_passwords = {"password123", "12345678", "qwerty", "letmein", "password1", "abc123", "iloveyou", "admin", "welcome"}
    if password.lower() in common_passwords:
        return "Weak", ["Avoid using common passwords like 'password123'."]
    
    strength_levels = {1: "Very Weak", 2: "Weak", 3: "Moderate", 4: "Moderate", 5: "Strong", 6: "Very Strong"}
    
    return strength_levels.get(score, "Very Weak"), feedback

def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

def main():
    st.title("🔒 Password Strength Meter")
    
    password = st.text_input("Enter your password:", type="password")
    if password:
        strength, feedback = check_password_strength(password)
        
        st.subheader(f"Password Strength: {strength}")
        
        progress = {"Very Weak": 0.2, "Weak": 0.4, "Moderate": 0.6, "Strong": 0.8, "Very Strong": 1.0}
        st.progress(progress.get(strength, 0.1))
        
        if feedback:
            st.warning("\n".join(feedback))
        else:
            st.success("Great! Your password is very strong.")
    
    st.subheader("Generate a Strong Password")
    length = st.slider("Select Password Length", min_value=12, max_value=32, value=16)
    if st.button("Generate Strong Password"):
        st.text(f"Suggested Password: {generate_strong_password(length)}")

if __name__ == "__main__":
    main()