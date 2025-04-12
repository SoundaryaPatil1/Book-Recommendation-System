
import streamlit as st

# ✅ Mock recommendation function — Replace with your real model logic
def recommend_books_to_user(user_id):
    # Example logic — replace this with actual recommendation engine
    if user_id not in [1, 2, 3]:  # Simulated valid users
        return "User ID not found in the system."
    return [f"Book Recommendation {i+1}" for i in range(5)]

# ✅ Streamlit UI
st.title("📚 Book Recommendation System")

user_input = st.text_input("Enter User ID")

if user_input:
    try:
        user_id = int(user_input)
        recommendations = recommend_books_to_user(user_id)
        if isinstance(recommendations, str):
            st.error(recommendations)
        else:
            st.success(f"Top recommendations for User {user_id}:")
            for book in recommendations:
                st.write(f"📖 {book}")
    except ValueError:
        st.error("Please enter a valid numeric User ID")
