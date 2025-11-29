from dotenv import load_dotenv
import os

load_dotenv()

print("GROQ =", os.getenv("GROQ_API_KEY"))
print("TAVILY =", os.getenv("TAVILY_API_KEY"))
