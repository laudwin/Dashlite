import streamlit as st
import streamlit.components.v1 as components
from utils import (
    JIDE_URL,
    query_flowise
)
from utils import TABLE, theme_colors, login
st.title("Data Science Report (Converse)")
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
    st.stop()
    
st.markdown("""
### Chat and Converse with our AI assistant
Chat or click “Start a call” to chat with an AI assistant that has read the full report by Prof Abejide. You can ask it questions about the findings, insights or any theory mentioned. It won't give personal opinions or new advice but only what's in the report.

It’s like having a helpful guide who knows the document inside out!
""")

col1, col2 = st.columns([1, 1])

with col1:
    # Input box for the user to type messages
    if input := st.chat_input("Ask your question..."):
        # Add user's message to chat history
        with st.chat_message("user"):
            st.markdown(input)

        # Call your API (replace with your actual API call)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                data_payload = {"question": input,}
                output = query_flowise(JIDE_URL, data_payload, 90)
                reply = output.get("text", "Oops! No response 😅")
                st.markdown(reply)

with col2:
    # HTML snippet containing the custom widget
    elevenlabs_widget = """
    <elevenlabs-convai agent-id="xIdI2L9Ckruc3v2Imfz6"></elevenlabs-convai><script 
    src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>"""

    # Embed the widget in Streamlit
    components.html(elevenlabs_widget, height=400, width=600)

# Large height to avoid internal scrolling
iframe_html = """
<iframe src="https://jolly-river-0f1d4b303.6.azurestaticapps.net"
        width="100%"
        height="2000px"
        style="border:none;"
        scrolling="no">
</iframe>
"""

components.html(iframe_html, height=2000)

# Add a hyperlink to open the full dashboard
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px;'>
        👉 <a href='https://jolly-river-0f1d4b303.6.azurestaticapps.net' target='_blank'>
        Open full dashboard in a new tab
        </a>
    </div>
    """,
    unsafe_allow_html=True
)