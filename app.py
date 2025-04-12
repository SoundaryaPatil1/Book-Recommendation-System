
import streamlit as st

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
