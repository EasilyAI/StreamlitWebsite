from dotenv import load_dotenv
from openai import OpenAI
import os
env_path = os.path.join(os.path.dirname(__file__),'..','streamlitWeb','.env')

load_dotenv(dotenv_path=env_path)
class OpenAIClient:
    def __init__(self, 
                organization=os.getenv('OPEN_AI_ORG_ID'),
                api_key=os.getenv('OPEN_AI_API_KEY')):
        self.client = OpenAI(            
            organization=organization,
            api_key=api_key
        )
    
    def call_model(self,  prompt, model_name = "gpt-3.5-turbo-instruct", max_tokens=100):
        response = self.client.completions.create(
            model=model_name,
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()