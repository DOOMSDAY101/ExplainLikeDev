# ExplainLikeDev

**ExplainLikeDev** is an AI-powered developer tool that explains code based on the user’s experience level, provides improvement suggestions, and highlights potential mistakes.  
It’s built with **LangChain**, **FastAPI**, and supports multiple LLM providers such as **Ollama**, **OpenAI**, and can easily be extended to **Google Gemini**.

## Table of Contents

1. [Demo](#demo)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Project Structure](#project-structure)
5. [Usage](#usage)
6. [Future Enhancements](#future-enhancements)
7. [Contributing](#contributing)
8. [License](#license)

---

## Demo

> **Coming soon:** deploy online and provide a live demo link.

Example API usage:

```json
POST /api/explain
{
  "code": "def add(a, b): return a + b",
  "experience_level": "Beginner"
}

Response:

{
  "explanation": "This function adds two numbers together...",
  "improvements": "- Add type hints\n- Use descriptive variable names",
  "common_mistakes": "- Does not handle non-numeric input"
}
```

---

## Features

- Explain code based on **Beginner**, **Intermediate**, or **Advanced** experience levels
- Provide **improvement suggestions** for readability, maintainability, and performance
- Identify **common mistakes** and pitfalls
- **LLM-agnostic architecture**: swap Ollama, OpenAI, Gemini, etc. without changing core logic
- Clean and modular **FastAPI backend**
- Ready for **frontend integration** (React/Next.js, Vue, etc.)

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip / virtualenv
- Ollama installed for local development (or another LLM provider)
- OpenAI API key (optional if using OpenAI)

### Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/explainlike-dev.git
cd explainlike-dev

# Create virtual environment
python -m venv venv

# Activate venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3

# Optional if using OpenAI
OPENAI_API_KEY=your_openai_api_key
```

### Run the Backend

```bash
uvicorn app.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Test health check:

```
GET http://127.0.0.1:8000/health
Response: {"status": "ok"}
```

---

## Project Structure

```
explainlike-dev/
│
├── app/
│   ├── api/
│   │   └── explain.py          # FastAPI endpoint
│   ├── core/
│   │   ├── explainer.py        # Explanation / improvement / mistakes chains
│   │   └── llm.py              # LLM factory for Ollama / OpenAI / Gemini
│   └── main.py                 # FastAPI app
├── prompts.md                  # Blueprint for all prompt chains
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
└── README.md                   # Project documentation
```

---

## Usage

1. **Call `/api/explain`** endpoint with JSON payload:

```json
{
  "code": "def multiply(a, b): return a * b",
  "experience_level": "Intermediate"
}
```

2. **Receive JSON response** with:

- `explanation` – code explanation tailored to experience level
- `improvements` – actionable improvement suggestions
- `common_mistakes` – potential pitfalls

3. **Integrate with frontend** to display results in a code editor, tabs, or sections.

---

## How It Works

1. **prompts.md**: defines detailed instructions for each AI chain (Explanation, Improvements, Common Mistakes)
2. **LangChain PromptTemplates**: concise actionable prompts sent to the LLM
3. **LLM chains**: run the AI workflow using your chosen LLM (Ollama / OpenAI / Gemini)
4. **FastAPI endpoint**: receives code + experience level → returns structured JSON with all outputs

---

## Future Enhancements

- Frontend UI with **Monaco code editor**
- Support for multiple languages detection automatically
- Session memory to **remember user experience level** across requests
- File uploads and GitHub integration
- Deployment to Vercel / Render / Railway for a live demo
- Logging and analytics of user queries

---

## Contributing

Contributions are welcome! Steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Push to your branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## License

This project is **MIT Licensed** – see [LICENSE](LICENSE) for details.
