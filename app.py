import streamlit as st
import re
import string
import secrets

# Page configuration
st.set_page_config(
    page_title="Password Security Analyzer",
    page_icon="🔐",
    layout="centered"
)

# Title
st.title("🔐 Password Security Analyzer")

st.write(
    "Analyze password strength, receive security recommendations, and generate strong passwords."
)

# Password input
password = st.text_input(
    "Enter your password:",
    type="password"
)

# Password analysis function
def analyze_password(password):
    score = 0
    recommendations = []

    # Length
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
        recommendations.append("Use at least 12 characters for better security.")
    else:
        recommendations.append("Use at least 8 characters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 15
    else:
        recommendations.append("Add lowercase letters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        recommendations.append("Add uppercase letters.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 15
    else:
        recommendations.append("Add numbers.")

    # Special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 20
    else:
        recommendations.append("Add special characters such as !, @, #, or $.")

    # Common weak passwords
    common_passwords = [
        "password",
        "password123",
        "123456",
        "12345678",
        "qwerty",
        "admin",
        "welcome"
    ]

    if password.lower() in common_passwords:
        score = 10
        recommendations.append(
            "Avoid common passwords because they are easy to guess."
        )

    return score, recommendations


# Check password button
if st.button("🔍 Check Password"):

    if password == "":
        st.warning("Please enter a password.")

    else:
        score, recommendations = analyze_password(password)

        st.subheader("Security Analysis")

        # Security score
        st.metric("Security Score", f"{score}/100")

        # Strength result
        if score < 40:
            st.error("🔴 Weak Password")
        elif score < 70:
            st.warning("🟡 Medium Strength Password")
        else:
            st.success("🟢 Strong Password")

        # Recommendations
        st.subheader("💡 Security Recommendations")

        if recommendations:
            for recommendation in recommendations:
                st.write("⚠️ " + recommendation)
        else:
            st.write("✅ Excellent! Your password meets all basic security checks.")


# Password generator
st.divider()

st.subheader("🎲 Strong Password Generator")

if st.button("Generate Strong Password"):

    characters = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*"
    )

    generated_password = "".join(
        secrets.choice(characters)
        for _ in range(16)
    )

    st.code(generated_password)

    st.success(
        "A strong 16-character password has been generated."
    )  

    st.divider()

st.subheader("📘 About This Project")

st.write(
    "This cybersecurity project analyzes password strength based on "
    "length, uppercase letters, lowercase letters, numbers, and special "
    "characters. It provides a security score and recommendations to help "
    "users create stronger passwords."
)

st.write(
    "**Technology Used:** Python, Streamlit"
)

st.write(
    "**Project Type:** Cybersecurity / Password Security"
)