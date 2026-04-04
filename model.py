from llama_cpp import Llama

# Biến lưu trữ model
llm = None

def load_model():
    global llm
    try:
        llm = Llama.from_pretrained(
            repo_id="LiquidAI/LFM2.5-350M-GGUF",
            filename="LFM2.5-350M-BF16.gguf",
            n_ctx=512
        )
    except Exception as e:
        print(f"Error loading model: {str(e)}")


def generate_answer(prompt: str, max_tokens: int = 100):
    if llm is None:
        return "Error: Model is not initialized."
    
    try:
        output = llm(
            f"Question: {prompt} Answer:", 
            max_tokens=max_tokens,
            stop=["\n", "Question:"],
            echo=False
        )
        return output['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error during inference: {str(e)}"