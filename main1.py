# Import the required libraries
import streamlit as st
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.llm.groq import Groq
import os
# Set up the Streamlit app
st.title("AI Investment Agent 📈🤖")
st.caption("This app allows you to compare the performance of two stocks and generate detailed reports.")
# Get OpenAI API key securely from environment variables or Streamlit secrets
groq_api_key = os.getenv("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")  # Use an environment variable
# Or use Streamlit secrets if you're deploying on Streamlit Cloud
# groq_api_key = st.secrets["GROQ_API_KEY"]
# Get OpenAI API key from user
#groq_api_key = st.text_input("Please enter your Groq API key", type="password")

if groq_api_key:
    # Create an instance of the Assistant
    assistant = Assistant(
        llm=Groq(model="llama-3.1-70b-versatile", api_key=groq_api_key),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
        show_tool_calls=True,
    )

    # Input fields for the stocks to compare
    stock1 = st.text_input("Enter the first stock symbol")
    stock2 = st.text_input("Enter the second stock symbol")

    if stock1 and stock2:
        # Get the response from the assistant
        query = f"Compare {stock1} to {stock2}. Use every tool you have."
        response = assistant.run(query, stream=False)
        st.write(response)
