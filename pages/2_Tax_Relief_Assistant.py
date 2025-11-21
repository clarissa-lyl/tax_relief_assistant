import re
import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# --- Security Config ---
FORBIDDEN_PATTERNS = [
    r"ignore previous instructions",
    r"system prompt",
    r"hidden instructions",
    r"internal instructions",
    r"reveal secret",
    r"output hidden",
    r"hidden",
    r"revealing",
    r"python script",
    r"exfiltrate",
]

SENSITIVE_KEYWORDS = [
    "system instructions",
    "hidden instructions",
    "developer prompt",
    "template value",
    "API Key",
]


def is_suspicious(user_input: str) -> bool:
    """
    Detect if the user input contains prompt injection attempts.
    """
    user_input_lower = user_input.lower()
    return any(re.search(pattern, user_input_lower) for pattern in FORBIDDEN_PATTERNS)


def sanitize_output(output: str) -> str:
    """
    Redact any sensitive keywords accidentally revealed in the output.
    """
    sanitized = output
    for keyword in SENSITIVE_KEYWORDS:
        sanitized = re.sub(keyword, "[REDACTED]", sanitized, flags=re.IGNORECASE)
    return sanitized


# --- Streamlit UI ---
st.title("Tax Relief Assistant")

# --- Login Check ---
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("You must log in first.")
    st.stop()

# --- Conversation History State ---
if "tax_relief_history" not in st.session_state:
    st.session_state["tax_relief_history"] = []

try:
    # --- Load OpenAI API Key ---
    apikey = st.secrets["OPENAI"]["OPENAI_API_KEY"]

    # --- Load FAISS Vectorstore ---
    PERSIST_DIR = "./faiss_db"  # Path to your saved FAISS index
    embeddings = OpenAIEmbeddings(api_key=apikey, model="text-embedding-3-small")
    vectorstore = FAISS.load_local(
        folder_path=PERSIST_DIR,
        embeddings=embeddings,
        allow_dangerous_deserialization=True,  # safe if you created this index
    )

    # --- Create retriever ---
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    # --- Custom prompt for Singapore tax relief eligibility ---
    template = """
    You are a helpful assistant for Singapore personal income tax relief.
    Using only the retrieved tax relief information, determine the user's eligibility
    and provide a clear, direct answer.

    Retrieved context:
    {context}

    Resident's question: {question}

    Instructions:
    - Start with a direct eligibility judgment (Yes/No/Unclear).
    - Briefly explain the reasoning by citing the relevant criteria from the context
      (e.g., residency, income caps, age, dependants, marital status, employment status,
      NSman status, relief caps, YA applicability).
    - If multiple reliefs are relevant, list each with its eligibility and key limits.
    - If information is missing, ask concise follow-up questions to decide eligibility.
    - Do not invent rules not present in the retrieved context.
    """
    qa_prompt = PromptTemplate.from_template(template)

    # --- RetrievalQA chain ---
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1, api_key=apikey)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": qa_prompt},
    )

    # --- Example prompts (clickable) ---
    st.write("Ask about tax relief eligibility, e.g.:")
    example_prompts = [
        "If I am married, having 2 kids and my spouse is an NSmen having a callup in FY24, what are the eligible tax reliefs?",
        "Can I claim Spouse Relief if my spouse has income?",
        "Do I qualify for NSman Self/Parent Relief this year if I attended NS activities?",
    ]

    st.caption("Click an example below or type your own question:")
    cols = st.columns(len(example_prompts))
    selected_example = None
    for i, prompt_text in enumerate(example_prompts):
        if cols[i].button(prompt_text):
            selected_example = prompt_text

    # --- User input via chat ---
    user_prompt = st.chat_input("Ask about Singapore personal income tax relief")

    # --- Disclaimer below chat input ---
    with st.expander("Disclaimer"):
        disclaimer = """
        **IMPORTANT NOTICE**  
        This web application is a prototype developed for educational purposes only.  
        The information provided here is **NOT** intended for real-world usage and should not be relied upon for making decisions, especially financial, legal, or healthcare matters.  

        Furthermore, please be aware that the LLM may generate inaccurate or incorrect information.  
        You assume full responsibility for how you use any generated output.  

        Always consult with qualified professionals for accurate and personalized advice. 
        """
        st.markdown(disclaimer)

    query = selected_example or user_prompt

    if query:
        if is_suspicious(query):
            st.warning(
                "Your query contains suspicious instructions and cannot be processed."
            )
        else:
            with st.spinner("Thinking..."):
                response = qa_chain.run(query)
            sanitized_response = sanitize_output(response)

            # Save to conversation history (keep only last 3)
            st.session_state["tax_relief_history"].append(
                {"question": query, "answer": sanitized_response}
            )
            st.session_state["tax_relief_history"] = st.session_state[
                "tax_relief_history"
            ][-3:]

    # --- Display conversation history as chat (last 3) ---
    if st.session_state["tax_relief_history"]:
        for entry in st.session_state["tax_relief_history"]:
            with st.chat_message("user"):
                st.markdown(entry["question"])
            with st.chat_message("assistant"):
                st.markdown(entry["answer"])

except Exception as e:
    st.error("An error has occurred, please inform the team creators.")
    print(f"Tax Relief Assistant Page Error: {e}")
