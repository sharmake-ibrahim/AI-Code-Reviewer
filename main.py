import os
from anthropic import Anthropic  
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def review_code(code: str, language: str = "Python") -> str:
    if not code.strip():
        return "Error: Empty code provided."
    try:
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"Review the following {language} code and suggest improvements with examples:\n\n{code}"
                }
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"Error reviewing code: {str(e)}"

if __name__ == "__main__":
    code_snippet = """ 
            const burger = document.querySelector('.burger i');
            const nav = document.querySelector('.nav');

            function toggleNav() {
                burger.classList.toggle('fa-bars');
                burger.classList.toggle('fa-times');
                nav.classList.toggle('nav-active');
            }

            burger.addEventListener('click', function() {
                toggleNav();
            });

            const toggleLinks = () => {
            const links = document.querySelectorAll(".navlink");
            console.log(links);

            links.forEach((link,_)=> {
                link.addEventListener("click", ()=> {
                

                toggleNav();
                })
            })"""
    
    """ 
def add(x, y):
    return x + y
"""
    print("Code Review:")
    print(review_code(code_snippet, language="JavaScript"));