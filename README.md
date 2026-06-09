# AI Code Reviewer

An AI-powered tool that reviews your code and suggests improvements using Claude (Anthropic API).

## Requirements

- Python 3.7+
- Anthropic API key ([get one here](https://console.anthropic.com))

## Installation

1. **Install dependencies:**
   ```bash
   pip install anthropic python-dotenv
   ```

2. **Create a `.env` file** in the project root:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## Usage

Paste your code snippet into `main.py` and run:

```bash
python main.py
```

You can specify the programming language:

```python
print(review_code(code_snippet, language="Python"))
```

## Example Output

```
Code Review:
- Consider adding type hints to function parameters
- Add a docstring to describe what the function does
- Example improvement: def add(x: int, y: int) -> int:
```

## Project Structure

```
AI-Code-Reviewer/
├── main.py        # Main script
├── .env           # API key (not committed)
├── .gitignore
└── README.md
```
