import streamlit as st
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
import os

from pyowm.commons.exceptions import NotFoundError
from translate import Translator

translator = Translator(to_lang="pl")

os.environ["OPENWEATHERMAP_API_KEY"] = "OPENWEATHERMAP_API_KEY"

llm = OpenAI(temperature=0, api_key="OPENAI_API_KEY")

tools = load_tools(["openweathermap-api"], llm)
weather_agent = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

def run_weather_app():
    st.title('Pogodynka')
    city = st.text_input('Wprowadź nazwę miasta:', '')
    try:
        if st.button('Pokaż pogodę'):
            query = f"What's the weather in {city} now?"
            report = weather_agent.run(query)
            st.text(translator.translate(report))
    except NotFoundError:
        st.text("Nie mam informacji na ten temat")

if __name__ == '__main__':
    run_weather_app()
