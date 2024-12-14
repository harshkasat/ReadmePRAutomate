from fastapi import FastAPI
from pydantic import BaseModel, AnyUrl, validator
from main import readme_automate
import re

app = FastAPI()

class GithubUrl(BaseModel):
    github_url: AnyUrl

    @validator('github_url')
    def validate_github_url(cls, v):
        if not re.match(r'^https://github\.com/[^/]+/[^/]+$', str(v)):
            raise ValueError('Invalid GitHub URL')
        return v

@app.post('/')
def automate_github_readme(url: GithubUrl):
    
    response = readme_automate(str(url.github_url))
    return {'response': response}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)