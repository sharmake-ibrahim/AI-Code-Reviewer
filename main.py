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

        import React from "react";
import { Link, useParams } from "react-router-dom"
import data from "../data.json";
import type { Job } from "./Types/Job";
import Header from "./Header";




const Details: React.FC = ()=> {

    const {id} = useParams()

    const details_data = data.find((job:Job)=> job.id === Number(id));

    console.log("this job is clicked", details_data)

    return (

        <>

            <Header/>

   
    <main>
                         
    <section className="job-header">
         <div className="logo" style={{background: details_data?.logoBackground}}>
            <img src= {details_data?.logo} alt=""/>
        </div>
            <div className="txt">
                <strong>{details_data?.company}</strong>
                <p>{details_data?.company}</p>
            </div>

            
               <Link className="details-btn" to= {`${details_data?.apply}`} > Company Site</Link>
    </section>
          <div className="container">
  
            <section className="detials-content">
                 <div className="job-desc">
                    <div className="flex">
                        <p>{details_data?.postedAt}</p>
                        <li>{details_data?.contract}</li>
                    </div>

                    <div className="job-txt">
                        <h1>{details_data?.position}</h1>
                         <Link className="details-btn" to= {`${details_data?.apply}`} > Company Site</Link>
                    </div>
                    <p className="location">{details_data?.location}</p>
                </div>

                <article>
                    <p>{details_data?.description}</p>
                </article>

                <ul className="info-one"> 
                    <strong>Requirements</strong>
                    <p>{details_data?.requirements.content}</p>
                    {details_data?.requirements.items.map( item => <li>{item}</li>)}
                </ul>
                <ol className="info-two"> 
                    <strong>What You Will Do</strong>
                    <p>{details_data?.role.content}</p>
                    {details_data?.role.items.map(item => <li>{item}</li>)}
                </ol> 
            </section>
       
        
        </div>
    </main>
    <footer>
        <div className="container-footer">

       
        <div className="footer-content">
 
            <div className="position">
                        <h1>{details_data?.position}</h1>
                        <p>{details_data?.location}</p>
                    </div>
                     <Link className="btn" to = {`${details_data?.apply}`}>Load More</Link> 
         </div> 

 </div>
    </footer>
        </>
    )
}

export default Details
    """
    
    """ 
def add(x, y):
    return x + y
"""
    print("Code Review:")
    print(review_code(code_snippet, language="React"))