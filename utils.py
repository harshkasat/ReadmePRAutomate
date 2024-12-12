#utils.py
import re
import nltk
import os

nltk.download("punkt")

def clean_and_tokenize(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\b(?:http|ftp)s?://\S+', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    return nltk.word_tokenize(text)

def format_documents(documents):
    numbered_docs = "\n".join([f"{i+1}. {os.path.basename(doc.metadata['source'])}: {doc.page_content}" for i, doc in enumerate(documents)])
    return numbered_docs

def format_user_question(question):
    question = re.sub(r'\s+', ' ', question).strip()
    return question

README_PROMPT = """# Comprehensive README Generation Prompt for GitHub Project

## Objective
Generate a comprehensive, well-structured README.md file that provides complete documentation for an open-source project, targeting both beginners and advanced developers.

## Prompt Instructions
You are an expert technical writer creating a professional, clear, and informative README file. Ensure the documentation is comprehensive, engaging, and provides value to potential users and contributors.

## README Structure (Mandatory Sections)

### 1. Project Title and Short Description
- Create a clear, descriptive project title
- Write a concise 1-2 sentence overview explaining the project's core purpose
- Include relevant badges (build status, version, license, etc.)

### 2. Project Overview
- Detailed project description
- Key features and unique selling points
- Problem the project solves
- Use cases and practical applications

### 3. Table of Contents
- Create a clickable, organized table of contents
- Include links to all major sections of the README

### 4. Prerequisites
- List all required software, libraries, and dependencies
- Specify exact versions if critical
- Include system requirements
- Explain any potential compatibility issues

### 5. Installation Guide
- Step-by-step installation instructions
- Multiple installation methods (if applicable)
  - Package managers
  - Direct download
  - Docker setup
  - Virtual environment setup
- Troubleshooting common installation issues

### 6. Configuration
- Environment setup instructions
- Configuration file explanations
- Required environment variables
- Default and recommended settings

### 7. Usage Examples
- Comprehensive usage documentation
- Code snippets demonstrating:
  - Basic usage
  - Advanced configurations
  - Different use cases
- Interactive examples if possible

### 8. Project Architecture
- High-level system design
- Component interactions
- Technology stack
- Architectural diagrams (if applicable)

### 9. Performance and Benchmarks
- Performance characteristics
- Benchmark results
- Comparative analysis with similar solutions
- Scalability information

### 10. API Reference (if applicable)
- Detailed API documentation
- Endpoint descriptions
- Request/response formats
- Authentication methods

### 11. Contributing Guidelines
- How to contribute to the project
- Code of conduct
- Contribution process
- Coding standards
- Pull request template
- Issue reporting guidelines

### 12. Testing
- How to run tests
- Test coverage information
- Types of tests included
- Testing frameworks used

### 13. Deployment
- Deployment strategies
- Cloud platform instructions
- Container deployment
- Continuous Integration/Continuous Deployment (CI/CD) setup

### 14. Security
- Security considerations
- Vulnerability reporting process
- Known security issues
- Best practices for secure usage

### 15. Ethical Considerations (for AI/ML projects)
- Ethical use guidelines
- Potential biases
- Responsible AI principles
- Transparency about model limitations

### 16. Future Roadmap
- Planned features
- Upcoming improvements
- Community-driven development goals

### 17. License
- Full license text
- Explanation of licensing terms
- Commercial use considerations

### 18. Acknowledgments
- Contributors list
- Special thanks
- Referenced projects or inspirations

### 19. Contact and Support
- Maintainer contact information
- Community support channels
- How to ask questions
- Reporting issues

## Additional Formatting Guidelines
- Use clear, professional language
- Implement GitHub-flavored Markdown
- Use consistent formatting
- Include relevant emojis sparingly
- Ensure readability across different devices

## Final Checklist
Verify the README:
- Is technically accurate
- Covers all project aspects
- Is beginner-friendly
- Provides advanced details
- Looks professionally formatted

## Tone and Style
- Technical yet approachable
- Clear and concise
- Avoid jargon where possible
- Use active voice
- Show enthusiasm for the project

## Output Format
Provide the complete README.md file, fully formatted and ready for GitHub publication."""
