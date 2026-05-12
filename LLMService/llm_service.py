import config as config
from groq import Groq

class LLMService:

    def __init__(self, llm_provider):
          self.llm_provider = llm_provider

    # method used to call a llm as per its respective llm provider
    def generate_result (self, prompt):
          try :
            if self.llm_provider == "grok":
                return self.generate_result_using_grok(prompt)
            
          except Exception as ex:
            print("Exception is: ", str(ex))
            return None

    # method used to call call llm using grok
    def generate_result_using_grok (self, prompt):
          
        _client = Groq(api_key = config.api_key)

        _response = _client.chat.completions.create(
                    model = "llama-3.1-8b-instant",
                    messages = [
                        {"role": "system", "content": "You are a file summarizer."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature = 0.4,
                    max_tokens = 600
                )

        return _response.choices[0].message.content