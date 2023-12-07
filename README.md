SerpApi Google Research Tool
This Python script allows you to perform Google searches using the SerpApi service to find either job offers or candidate profiles. It utilizes the serpapi library to interact with the SerpApi API.

## Prerequisites
Python 3.x installed
SerpApi API key. You can obtain it by signing up at https://serpapi.com/
A .env file containing your SerpApi API key. See the section below on how to set up your environment variables.
## Setup
1. Clone this repository:
```bash
git clone https://github.com/your-usernam/job_profil_summarization.git
```
Don't forget to change your username here
2. Navigate to the project directory:
```bash
cd serpapi-google-research-tool
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Create a .env file in the project directory and add your SerpApi API key:
```bash
SERPAPI_PRIVATE_KEY=your_serpapi_api_key_here
```

Replace your_serpapi_api_key_here with your actual SerpApi API key.

## Usage
Run the script main.py from the command line with the desired search type and query:

```bash
python main.py candidate "Python developer"
```

or 

```bash
python main.py offer "software engineer"
```

