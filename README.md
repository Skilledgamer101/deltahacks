# SwiftApps
## Overview
Welcome to the AutoFill Job Application Assistant project! This tool is designed to streamline the job application process by automating the completion of complex questions on job applications with personalized responses.

## Features
1. **Automated Responses**: The program is engineered to automatically generate responses tailored to complex questions commonly found in job applications.

2. **Resume Analysis with Google Cloud Vision AI**: Utilizing Google Cloud Vision AI, the tool can extract text from over 100 pages of a resume PDF, ensuring comprehensive data capture.

3. **Cohere API Integration**: Interacting seamlessly with the Cohere API, the system analyzes the resume and generates detailed responses to specific questions.

4. **Selenium Automation**: The tool employs Selenium to retrieve questions from the form and autonomously populates them with the generated responses, saving time and effort.

## Getting Started
To get started with SwiftApps, follow these simple steps:

### Installation: Clone the repository to your local machine.

`git clone https://github.com/Skilledgamer101/deltahacks.git`

### Dependencies: Install the necessary dependencies.

`pip install -r requirements.txt`

### Configuration
1. Sign up for a Google Cloud Account
2. Save a PDF version of the resume to Google Cloud Storage
3. Run the `main.py` program in the Google Cloud Shell
4. Enter the link to the PDF which you saved in Google Cloud Storage (should start with gs://...)
5. Enter the same link as the storage destination but remove the ".pdf" part from the end
6. The program should extract all of the text from the resume and save a .txt file in the Google Cloud Shell current working directory
7. Transfer this file to your local computer (e.g., via Git)
8. Install all of the requirements for this program locally (as described above)
9. Run the `fill.py` program on your local computer
10. Enter your Cohere API key
11. Enter path to chromedriver (the one provided in this repository works with Google Chrome Version 120.0.6099.217 (Official Build) (64-bit))
12. Enter a link to the Google Form which you'd like to fill

## Sample Links

1. [Google Form Link](https://docs.google.com/forms/d/e/1FAIpQLSdhxqopQPUkUWsntlTyMolWr4Ab4NMuDiGHT4_gaGE4GIR1eg/viewform?pli=1)


## Contributing
We welcome contributions! If you have suggestions, bug reports, or would like to add new features, please open an issue or submit a pull request.
