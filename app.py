from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator
import re
from main import readme_automate

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RepositoryRequest(BaseModel):
    repositoryName: str

    # Optional validation if needed
    @validator('repositoryName')
    def validate_repository_name(cls, v):
        if not re.match(r'^https://github\.com/[^/]+/[^/]+$', str(v)):
            raise ValueError('Invalid GitHub URL')
        if not v or len(v.strip()) == 0:
            raise ValueError('Repository name cannot be empty')
        return v.strip()

@app.post('/')
async def automate_github_readme(request: RepositoryRequest):
    try:
        # Your README automation logic here
        response = readme_automate(str(request.repositoryName))
        response = {
            "repositoryName": request.repositoryName,
            "message": f"Process To Generate the README PR: {request.repositoryName}",
            "status": response,
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)