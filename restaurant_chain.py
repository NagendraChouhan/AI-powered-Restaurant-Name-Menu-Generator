
import os
import urllib.request
from urllib.parse import urlparse

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import SequentialChain, LLMChain

# ==========================================
# 1. Load environment variables
# ==========================================

load_dotenv()

SERVER = os.environ["OLLAMA_URL"].rstrip("/")
MODEL_NAME = os.environ["OLLAMA_MODEL"]
API_KEY = os.environ["OLLAMA_API_KEY"]

# ==========================================
# 2. Bypass proxy for local Ollama server
# ==========================================

server_host = urlparse(SERVER).hostname

if not server_host:
    raise ValueError("Invalid OLLAMA_URL in .env")

existing_no_proxy = os.environ.get("NO_PROXY", "")

no_proxy_hosts = [
    server_host,
    "localhost",
    "127.0.0.1"
]

os.environ["NO_PROXY"] = ",".join(
    filter(None, [existing_no_proxy, *no_proxy_hosts])
)

os.environ["no_proxy"] = os.environ["NO_PROXY"]

# ==========================================
# 3. Check Ollama server connectivity
# ==========================================

def check_ollama_connection():
    print("Testing Ollama connection...")

    try:
        with urllib.request.urlopen(
            SERVER + "/api/tags",
            timeout=10
        ) as response:

            if response.status == 200:
                print("Ollama server connected successfully!")

    except Exception as e:
        raise ConnectionError(
            f"Cannot connect to Ollama server: {e}"
        ) from e


# ==========================================
# 4. Initialize Qwen model
# ==========================================

llm = ChatOpenAI(
    model=MODEL_NAME,
    base_url=SERVER + "/v1",
    api_key=API_KEY,
    temperature=0.2,
    max_tokens=300,
    timeout=600,
    max_retries=1
)

# ==========================================
# 5. Restaurant name and menu generator
# ==========================================

def generate_rest_namd_and_item(cuisine):

    # Chain 1: Generate restaurant name
    name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template=(
            "Suggest one fancy and unique name for a "
            "{cuisine} restaurant. "
            "Return only the restaurant name."
        )
    )

    name_chain = LLMChain(
        llm=llm,
        prompt=name_prompt,
        output_key="rest_name"
    )

    # Chain 2: Generate menu items
    food_prompt = PromptTemplate(
        input_variables=["rest_name"],
        template=(
            "Suggest exactly 7 menu items for a "
            "restaurant named {rest_name}. "
            "Return only a comma-separated list."
        )
    )

    food_item_chain = LLMChain(
        llm=llm,
        prompt=food_prompt,
        output_key="menu_item"
    )

    # Sequential chain
    chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=["cuisine"],
        output_variables=["rest_name", "menu_item"],
        verbose=True
    )

    print("Sending request to Qwen...")

    result = chain.invoke({
        "cuisine": cuisine
    })

    return result


# ==========================================
# 6. Run program
# ==========================================

if __name__ == "__main__":

    check_ollama_connection()

    result = generate_rest_namd_and_item("Indian")

    print("\nRestaurant Name:")
    print(result["rest_name"])

    print("\nMenu Items:")
    print(result["menu_item"])
