from pydantic import BaseModel
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import json # Daha fazla bilgi icin https://docs.langchain.com/oss/python/langchain/models#json-schema

SYSTEM_PROMPT = "Sen Türkiye Cumhuriyeti Mahkemeleri için tasarlanmış bir yargıç" \
"Karar destek sistemisin. İsmin LEXTR. Yalnızca Türkiye Cumhuriyeti Hukuku Gözeterek" \
"Hukuki Silojizm adımlarını takip ederek durumları hukuki açdıan ele alır ve değerlendirirsin."

TEMPERATURE = 0.3 # Hukuki meseleler düsük temperature'de kalsa daha iyi olabilir.
TIMEOUT = 30
MAX_TOKENS = 1000

def main():
    model = ChatGoogleGenerativeAI(model="gemini-3.0-pro",
                                   temperature = TEMPERATURE,
                                   timeout = TIMEOUT,
                                   max_tokens = MAX_TOKENS
                                   )
    
    for chunk in model.stream("Why do parrots have colorful feathers?"):
        print(chunk.text, end="|", flush=True)

if __name__ == "__main__":
    main()
