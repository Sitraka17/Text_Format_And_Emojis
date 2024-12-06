streamlit as st
from streamlit_js_eval import streamlit_js_eval

# Set up the app title
st.title("Emoji Selector App")

# List of 20 emojis to choose from
emoji_list = [
    "😀", "😂", "😊", "😍", "😎",
    "🤓", "🥳", "😇", "🤩", "😜",
    "🥺", "😡", "😭", "😱", "😈",
    "🤖", "👻", "👽", "🤠", "💩"
]

# Display each emoji in a clickable box
st.write("### Click on an emoji to copy it:")
cols = st.columns(5)  # Arrange emojis in a grid with 5 columns

# Display emojis in the grid and add click functionality
for i, emoji in enumerate(emoji_list):
    with cols[i % 5]:
        if st.button(emoji, key=emoji):
            streamlit_js_eval(js_expressions="navigator.clipboard.writeText(${emoji})")
            st.success(f"Copied to clipboard: {emoji}")

# Instructions
st.info("Click on any emoji to copy it to the clipboard!")
