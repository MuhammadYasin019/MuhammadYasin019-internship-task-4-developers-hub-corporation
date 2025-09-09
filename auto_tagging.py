import os
import sys
import asyncio
import json
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# Fix async loop issue on Windows
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#  Load API key
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY") or ""

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.0)

# Define prompt (only one variable: ticket_text )
prompt = ChatPromptTemplate.from_template(
    """
You are a support ticket classifier. Always return JSON only.

Ticket:
{ticket_text}

Available tags: billing, login, payment, refund, bug, feature_request, account, password, performance, other

Return the TOP 3 most probable tags with numeric scores (0 to 1).
Output JSON exactly like this:
{{"tags": ["billing", "refund", "payment"], "scores": [0.85, 0.65, 0.42]}}
"""
)

chain = LLMChain(llm=llm, prompt=prompt)

#  Streamlit app
def main():
    st.set_page_config(page_title=" Auto-Tagging Support Tickets", layout="centered")
    st.title(" Auto-Tagging Support Tickets (Gemini + LangChain)")

    ticket_text = st.text_area("Paste a support ticket:", height=200)

    if st.button("Classify"):
        if not ticket_text.strip():
            st.error("Please enter a ticket text.")
        else:
            with st.spinner("Classifying..."):
                raw = chain.run(ticket_text)

            #  Clean response (remove ```json ... ``` wrappers)
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.strip("`")
                raw = raw.replace("json", "", 1).strip()

            try:
                data = json.loads(raw)
                tags = data.get("tags", [])
                scores = data.get("scores", [])
                st.subheader(" Predicted Tags")
                for t, s in zip(tags, scores):
                    st.write(f"- **{t}** (score: {s:.2f})")
            except json.JSONDecodeError:
                st.error(" Invalid JSON response")
                st.code(raw)

if __name__ == "__main__":
    main()
