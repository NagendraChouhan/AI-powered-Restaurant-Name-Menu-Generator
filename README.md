# 🍽️ Culina AI
### Where Culinary Creativity Begins

**An AI-Powered Restaurant Name & Menu Generator**

Culina AI is an AI-powered web application that generates elegant restaurant names and curated menu suggestions based on a user's preferred cuisine. Built with **Streamlit, LangChain, Ollama, and Qwen3-VL-8B**, it combines generative AI with a classical, premium-inspired user interface.

The application runs on a locally hosted large language model, enabling restaurant name and menu generation without relying on paid cloud inference APIs.

---

## ✨ Features

- **AI-Powered Restaurant Naming:** Generates creative restaurant names based on the selected cuisine.
- **Personalized Menu Generation:** Suggests seven menu items for the generated restaurant.
- **50+ Cuisine Options:** Includes Indian, Italian, Mexican, Chinese, Japanese, and many more.
- **Elegant User Interface:** Classical restaurant-inspired design with burgundy, gold, and cream accents.
- **LangChain Integration:** Uses sequential chains to connect restaurant name generation with menu creation.
- **Locally Hosted LLM:** Runs Qwen3-VL-8B through Ollama on a local workstation.
- **Remote Model Access:** Allows the Streamlit frontend to communicate with an Ollama server running on another machine.
- **Environment-Based Configuration:** Uses `.env` to manage connection settings.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web frontend |
| LangChain | LLM orchestration and sequential chains |
| Qwen3-VL-8B-Instruct | AI model for generating names and menus |
| Ollama | Local model hosting and inference |
| LangChain OpenAI | OpenAI-compatible API integration |
| python-dotenv | Environment variable management |
| HTML & CSS | Classical UI styling |

## 🏗️ System Architecture

```text
                  User
                   |
                   v
          Streamlit Frontend
                   |
                   v
           Cuisine Selection
                   |
                   v
          LangChain Backend
                   |
                   v
        SequentialChain
                   |
           +-------+--------+
           |                |
           v                |
       LLMChain 1           |
   Restaurant Name          |
           |                |
           v                |
       LLMChain 2 <---------+
       Menu Generation
           |
           v
    Ollama API Server
           |
           v
      Qwen3-VL-8B
           |
           v
   Generated Restaurant
      Name & Menu
```

Both LangChain stages call the Ollama-hosted model. The first stage generates a restaurant name, which becomes an input to the second stage.

## 📂 Project Structure

```text
Culina-AI/
│
├── app.py                 # Streamlit frontend
├── restaurant_chain.py    # LangChain backend
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment settings
├── .gitignore             # Git ignored files
└── README.md              # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Culina-AI.git
cd Culina-AI
```

Replace `YOUR_USERNAME` with your GitHub username and use your actual repository name.

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it.

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The project uses the following Python dependencies:

```text
streamlit
langchain
langchain-core
langchain-classic
langchain-openai
python-dotenv
httpx
```

### 4. Install Ollama

Ollama must be installed on the computer hosting the model.

**Ubuntu / Linux:**

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

For other operating systems, follow the instructions at https://ollama.com.

### 5. Download Qwen3-VL-8B

On the Ollama server machine:

```bash
ollama pull qwen3-vl:8b-instruct
```

Verify that the model is installed:

```bash
ollama list
```

The model uses approximately 6.2 GB of disk space in its Q4_K_M quantized configuration. Additional RAM is required during inference.

### 6. Configure the environment

Create a `.env` file in the project root:

```env
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=qwen3-vl:8b-instruct
OLLAMA_API_KEY=ollama
```

If Ollama is running on another machine, replace `localhost` with that machine's reachable address.

For example:

```env
OLLAMA_URL=http://YOUR_SERVER_IP:11434
OLLAMA_MODEL=qwen3-vl:8b-instruct
OLLAMA_API_KEY=ollama
```

**Security:** Ollama's local API does not require authentication by default. The `ollama` API key is only a compatibility placeholder. Do not expose an unauthenticated Ollama service to the public internet. Use a trusted private network, firewall restrictions, or an SSH tunnel for remote access.

### 7. Run the application

```bash
streamlit run app.py
```

Open the application in your browser:

```text
http://localhost:8501
```

## 🧠 How It Works

**Step 1 — Cuisine Selection**

Users select a cuisine from the searchable, alphabetically sorted dropdown.

**Step 2 — Restaurant Name Generation**

LangChain sends the selected cuisine to Qwen3-VL-8B, requesting a creative restaurant name.

Example input:

```text
Indian
```

Illustrative output:

```text
The Royal Saffron
```

**Step 3 — Menu Generation**

The generated restaurant name is passed into a second LangChain stage, which requests seven menu suggestions.

Illustrative output:

```text
Paneer Tikka
Dal Makhani
Hyderabadi Biryani
Butter Naan
Palak Paneer
Masala Dosa
Gulab Jamun
```

**Step 4 — Result Display**

Streamlit presents the generated restaurant name and menu in an elegant, classical-themed results section.

Actual outputs vary depending on the model's generation.

## 🔗 LangChain Sequential Processing

The application uses `SequentialChain` and `LLMChain` from `langchain-classic`.

```python
chain = SequentialChain(
    chains=[name_chain, food_item_chain],
    input_variables=["cuisine"],
    output_variables=["rest_name", "menu_item"],
    verbose=True
)

result = chain.invoke({"cuisine": "Indian"})
```

The first chain produces `rest_name`, which is passed to the second chain to generate `menu_item`.

**Note:** `LLMChain` and `SequentialChain` are legacy LangChain APIs. Future versions of the project can migrate to LangChain Expression Language (LCEL).

## 🖥️ Deployment Architecture

The application supports a two-system configuration.

**System 1 — AI Inference Server**

- Ubuntu Linux workstation
- Ollama server
- Qwen3-VL-8B-Instruct
- Local CPU or GPU inference

**System 2 — Web Application**

- macOS, Windows, or Linux
- Python and Streamlit
- LangChain backend
- HTTP communication with the AI server

This separates the user interface from model inference, allowing the frontend to run without downloading the full model.

## 🔮 Future Enhancements

- AI-generated restaurant logos
- Restaurant tagline generation
- Menu item descriptions
- Cuisine-specific menu customization
- Multilingual restaurant names
- Restaurant branding recommendations
- Downloadable PDF menus
- Restaurant name and menu history
- Dietary preferences and price-range customization

## 🔒 Security

- Store environment-specific settings in `.env`.
- Do not commit `.env` files containing sensitive credentials.
- Use `.env.example` to document required environment variables.
- Restrict access to your Ollama API when using remote inference.
- Avoid displaying credentials or private configuration values in logs.

## 📜 License

No license has been specified for this project yet. Add an appropriate `LICENSE` file if you intend to define how others may use, modify, or distribute the code.

---

**Culina AI — Where Culinary Creativity Begins**

*Crafting restaurant identities, one cuisine at a time.*# AI-powered-Restaurant-Name---Menu-Generator
