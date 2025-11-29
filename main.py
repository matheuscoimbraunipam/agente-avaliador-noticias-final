import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="/workspaces/agente-avaliador-noticias-final/.env", override=True)

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from tools.search_tool import get_search_tool
from tools.sentiment_tool import analisar_sentimento
from utils.token_monitor import MonitorDeTokens


def main():
    print("Assistente Avaliador de Notícias (LangChain + Groq + Tavily)")


    monitor = MonitorDeTokens()

    while True:
        tema = input("\nDigite um tema para buscar notícias (ou 'sair'):\n\nTema: ")

        if tema.lower() == "sair":
            print("\nEncerrando...")
            break

        print("\nBuscando notícias...")

      
        tavily = get_search_tool()
        resultados = tavily.search(query=tema)

       
        if not resultados or "results" not in resultados or len(resultados["results"]) == 0:
            print("Nenhuma notícia encontrada.")
            continue

     
        noticias_texto = ""
        for item in resultados["results"]:
            noticias_texto += f"- {item['content']}\n"

      
        sentimento = analisar_sentimento(noticias_texto)

      
        mensagem_texto = (
            "Notícias encontradas:\n"
            + noticias_texto +
            "\n\nSentimento detectado:\n"
            + sentimento +
            "\n\nExplique como um avaliador profissional."
        )

        mensagem = HumanMessage(content=mensagem_texto)

      
        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            api_key=os.environ["GROQ_API_KEY"]
        )

        resposta = llm.invoke([mensagem])

     
        monitor.atualizar(mensagem_texto, resposta.content)

       
        print("\n--- RESULTADO FINAL ---")
        print(resposta.content)


if __name__ == "__main__":
    main()
