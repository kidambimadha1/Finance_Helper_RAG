import requests

def ask_llama(context, query):
    prompt = f"""You are a financial assistant. Based on the below data, answer the question accurately.

Context:
{context}

Question: {query}

Answer:"""

    payload = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        res_json = response.json()

        if "response" in res_json:
            return res_json["response"]
        else:
            return f"[Error from model]: {res_json.get('error', 'No response field')}"

    except Exception as e:
        return f"[LLM Exception]: {str(e)}"
