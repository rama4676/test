import streamlit as st

st.title("Example")
with st.sidebar:
    st.write("demo")

s = st.text_input("enter the name")

c = st.chat_input("enter the query")


# Use st.markdown to add custom CSS
st.markdown("""
    <style>
        .stButton {
            background-color: #4CAF50;  /* Green background */
            border: none;
            color: black;  /* Text color */
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            cursor: pointer;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Now you can create a button with the custom class
if st.button('Custom Styled Button', key='custom', help="This is a custom styled button"):
    st.write("Button clicked!")


st.markdown("""
    <style>
        .stButton {
            
        }
    </style>
""", unsafe_allow_html=True)
st.button("sub")
with st.expander("pop over"):
    st.write("hi")
    
