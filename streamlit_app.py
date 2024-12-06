import streamlit as st
from streamlit_js_eval import streamlit_js_eval

# Set up the app title
st.title("Emoji Selector App")

# Categorized emoji list
emoji_categories = {
    "Emotions": ["😀", "😂", "😊", "😍", "😎", "🤓", "🥳", "😇", "🤩", "😜"],
    "Animals": ["🐶", "🐱", "🦁", "🐮", "🐸", "🐼", "🐨", "🐷", "🐵", "🦄"],
    "Food": ["🍎", "🍕", "🍔", "🍩", "🍣", "🍪", "🍰", "🍉", "🍇", "🍓"],
    "Activities": ["⚽", "🏀", "🎸", "🎮", "🎨", "🎤", "🎲", "🚴", "🏊", "🏋️"],
    "Objects": ["💡", "📱", "💻", "📚", "🖊️", "🖍️", "📷", "🎥", "🎧", "⏰"],
    "Symbols": ["❤️", "✨", "🌟", "🔥", "💧", "🎈", "🎉", "✅", "❌", "🔔"],
}

# Display instructions
st.write("### Click on an emoji to copy it to the clipboard:")

# Iterate through categories and display emojis in a grid
for category, emojis in emoji_categories.items():
    st.write(f"#### {category}")
    cols = st.columns(5)  # Arrange emojis in a grid with 5 columns
    for i, emoji in enumerate(emojis):
        with cols[i % 5]:
            if st.button(emoji, key=f"{category}_{emoji}"):
                streamlit_js_eval(js_expressions=f"navigator.clipboard.writeText('{emoji}')")
                st.success(f"Copied to clipboard: {emoji}")

# Instructions
st.info("Click on any emoji to copy it to the clipboard!")
