# Zaimportowanie potrzebnych bibliotek
import streamlit as st
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
import os

from pyowm.commons.exceptions import NotFoundError
from translate import Translator

# Zainicjalizowanie tłumacza na język polski
translator = Translator(to_lang="pl")

# Ustawienie klucza api dla Openweathermap
os.environ["OPENWEATHERMAP_API_KEY"] = "7765a3a9beef89a51e50796563213773"

# Inicjalizacja modelu językowego OpenAI, podanie klucza api
llm = OpenAI(temperature=0, api_key="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")

# Inicjalizacja narzędzia dla api pogody poza funkcją aplikacji Streamlit, aby uniknąć ponownej inicjalizacji przy każdej iteracji
tools = load_tools(["openweathermap-api"], llm)
weather_agent = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# Streamlit app starts here
def run_weather_app():
    st.title('Pogodynka')
    city = st.text_input('Wprowadź nazwę miasta:', '')
    try:
        if st.button('Pokaż pogodę'):
            # Generowanie zapytania na podstawie danych wejściowych użytkownika
            query = f"What's the weather in {city} now?"
            # Pobranie danych za pomocą agenta na podstawie zapytania
            report = weather_agent.run(query)
            # Wyświetlenie i przetłumaczenie pobranych informacji
            st.text(translator.translate(report))
    except NotFoundError:
        st.text("Nie mam informacji na ten temat")

if __name__ == '__main__':
    run_weather_app()