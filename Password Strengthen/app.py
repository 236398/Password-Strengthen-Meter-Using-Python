import streamlit as st
import re


def check_password_strength(password):
    strength = 0
    remarks = ""
    suggestions = []

    # Criteria for password strength
    length_criteria = len(password) >= 12
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    digit_criteria = bool(re.search(r"\d", password))
    special_criteria = bool(re.search(r"[@$!%*?&]", password))

    # Evaluating password strength
    if length_criteria:
        strength += 1
    else:
        suggestions.append(
            "🔹 Use at least 12 characters for stronger security."
        )
    if uppercase_criteria:
        strength += 1
    else:
        suggestions.append("🔹 Include at least one uppercase letter.")
    if lowercase_criteria:
        strength += 1
    else:
        suggestions.append("🔹 Include at least one lowercase letter.")
    if digit_criteria:
        strength += 1
    else:
        suggestions.append("🔹 Include at least one number.")
    if special_criteria:
        strength += 1
    else:
        suggestions.append(
            "🔹 Include at least one special character (@$!%*?&)."
        )

    # Strength messages
    strength_levels = [
        "🚨 Very Weak", "❌ Weak", "⚠️ Moderate", "✅ Strong", "🌟 Very Strong"
    ]
    remarks = strength_levels[strength]

    return strength, remarks, suggestions


def main():
    st.set_page_config(
        page_title="Password Strength Checker",
        page_icon="🔐",
        layout="centered"
    )

    st.markdown("""
        <div style="text-align: center;">
            <h1 style='color: #FF5733;'>🔐 Password Strength Checker</h1>
            <p style='color: #555;'>Ensure your password is strong and secure
            with real-time .</p>
            <hr style='border: 1px solid #FF5733;'>
        </div>
    """, unsafe_allow_html=True)

    password = st.text_input(
        "Enter your password",
        type="password",
        help=("Your password should contain a mix of uppercase, lowercase, "
              "numbers, and symbols.")
    )

    if password:
        strength, remarks, suggestions = check_password_strength(password)

        st.markdown(
            (
                f"<h3 style='color: #3498db; text-align: center;'>"
                f"💡 Strength Score: {strength}/5</h3>"
            ),
            unsafe_allow_html=True
        )
        st.markdown(
            f"<h3 style='color: #27ae60; text-align: center;'>"
            f"🔍 Password Strength: {remarks}</h3>",
            unsafe_allow_html=True
        )

        if strength < 3:
            st.error(
                "⚠️ Your password is weak. "
                "Consider the following improvements:"
            )
            for suggestion in suggestions:
                st.markdown(
                    f"<li style='color: #e74c3c;'>{suggestion}</li>",
                    unsafe_allow_html=True
                )
        elif strength == 5:
            st.success("🎉 Your password is very strong! Great job!")
        else:
            st.info("🔎 Your password is decent, but you can make it even "
                    "stronger!")

    st.markdown("""
        <div style="text-align: center; margin-top: 20px; color: #888;">
            <small>Developed with ❤️ using Streamlit</small>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
