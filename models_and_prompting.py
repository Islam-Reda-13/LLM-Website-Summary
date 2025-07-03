import os
from dotenv import load_dotenv
from openai import OpenAI
from web_scraping import website


load_dotenv(override=True)
os.environ['OpenAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
open_router_api = os.getenv('OPENROUTER_API_KEY')

openai = OpenAI(base_url="https://openrouter.ai/api/v1",api_key=open_router_api)


MODEL_QWEN = 'qwen/qwen-2.5-72b-instruct:free'
MODEL_DEEPSEEK = 'deepseek/deepseek-r1:free'
MODEL_LLAMA = 'meta-llama/llama-3.3-70b-instruct:free'


system_prompt = "You are an assistant that analyzes the contents of a company website landing page \
and creates a short summary about the content for prospective customers, investors and recruits. Respond in markdown."




def stream_qwen(prompt: str) -> str:
    messages=[
            {'role': 'system', 'content' : system_prompt},
            {'role': 'user','content':prompt}
        ]
    response = openai.chat.completions.create(
        model = MODEL_QWEN,
        messages=messages,
        stream=True
    )
    result = ""
    for chunk in response:
        result += chunk.choices[0].delta.content or ""
        yield result
        



def stream_deepseek(prompt: str) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
      ]
    stream = openai.chat.completions.create(
        model=MODEL_DEEPSEEK,
        messages=messages,
        stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result



def stream_llama(prompt: str) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
      ]
    stream = openai.chat.completions.create(
        model=MODEL_LLAMA,
        messages=messages,
        stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result



def stream_summary(company_name, url, model):
    prompt = f"Please generate a summary for the content about {company_name} page. Here is their landing page:\n"
    prompt += website(url).get_content()
    if model=="Qwen":
        result = stream_qwen(prompt)
    elif model=="Deepseek":
        result = stream_deepseek(prompt)
    elif model=="Llama":
        result = stream_llama(prompt)    
    else:
        raise ValueError("Unknown model")
    yield from result        