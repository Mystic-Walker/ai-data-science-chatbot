import os

import streamlit as st
from dotenv import load_dotenv
from google import genai


# -----------------------------------
# Configuration
# -----------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error(
        "Gemini API key not found. "
        "Please add GEMINI_API_KEY to the .env file."
    )
    st.stop()


MODEL_NAME = "gemini-3.5-flash-lite"


SYSTEM_INSTRUCTION = """
You are an experienced Data Science Staff Engineer and technical assistant.

Your areas of expertise include:
- Python
- SQL
- Statistics
- Data Analysis
- Machine Learning
- Deep Learning
- Generative AI
- Large Language Models (LLMs)
- Data Visualization
- Model Evaluation
- Python and ML debugging
- Code explanation

Your responsibilities:

1. Provide technically accurate and practical answers.
2. Explain technical concepts clearly.
3. Provide Python or SQL code when requested.
4. Explain important parts of generated code.
5. Give step-by-step solutions for Data Science problems.
6. Recommend suitable approaches and explain why they are appropriate.
7. Help debug Python, SQL, and Machine Learning problems.
8. If a question is unclear or missing important information,
   ask for clarification rather than making unsupported assumptions.
9. Maintain the context of the current conversation.
10. Respond professionally like an experienced Data Science Staff member.

Prefer clear explanations, practical examples, and concise code.
"""


# -----------------------------------
# Gemini Client
# -----------------------------------

@st.cache_resource
def get_client():
    return genai.Client(api_key=api_key)


client = get_client()


# -----------------------------------
# Streamlit Page
# -----------------------------------

st.set_page_config(
    page_title="AI Data Science Staff Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Data Science Staff Assistant")

st.caption(
    f"Powered by Google Gemini • Model: {MODEL_NAME}"
)


# -----------------------------------
# Sidebar
# -----------------------------------

with st.sidebar:

    st.header("⚙️ Model Settings")

    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.1,
        help=(
            "Lower values produce more focused responses. "
            "Higher values produce more varied responses."
        )
    )

    st.write(f"Current temperature: **{temperature:.1f}**")

    st.divider()

    st.write("**Model**")
    st.code(MODEL_NAME)

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# -----------------------------------
# Conversation State
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------------
# Welcome Message
# -----------------------------------

if not st.session_state.messages:

    st.info(
        """
        👋 **Welcome!**

        I can help with:

        • Python  
        • SQL  
        • Statistics  
        • Data Analysis  
        • Machine Learning  
        • Deep Learning  
        • Generative AI  
        • LLMs  
        • Model Evaluation  
        • Debugging  
        • Code Explanation

        Ask me a Data Science question to get started.
        """
    )


# -----------------------------------
# Display Previous Messages
# -----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------------
# Chat Input
# -----------------------------------

user_prompt = st.chat_input(
    "Ask me anything about Data Science..."
)


if user_prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                # Build conversation context
                conversation = SYSTEM_INSTRUCTION + "\n\n"

                for message in st.session_state.messages:

                    if message["role"] == "user":
                        conversation += (
                            f"User: {message['content']}\n\n"
                        )

                    else:
                        conversation += (
                            f"Assistant: {message['content']}\n\n"
                        )

                # Gemini API request
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=conversation,
                    config={
                        "temperature": temperature
                    }
                )

                # Validate response
                if response.text:

                    answer = response.text

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                else:

                    st.warning(
                        "Gemini returned an empty response. "
                        "Please try again."
                    )

                    st.session_state.messages.pop()

            except Exception as e:

                error_message = str(e)

                if "429" in error_message:
                    st.error(
                        "Gemini API rate limit reached. "
                        "Please wait a moment and try again."
                    )

                elif "401" in error_message or "403" in error_message:
                    st.error(
                        "Gemini API authentication failed. "
                        "Please check your API key."
                    )

                elif "503" in error_message:
                    st.error(
                        "Gemini service is temporarily unavailable. "
                        "Please try again shortly."
                    )

                else:
                    st.error(
                        f"Gemini API error: {error_message}"
                    )

                # Remove failed user message
                st.session_state.messages.pop()