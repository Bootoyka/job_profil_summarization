from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

def test_serp():
    api_key = os.getenv("SERPAPI_PRIVATE_KEY")
    params = {
        "engine": "google_jobs",
        "q": "Java Developer",
        "ltype": "1",
        "hl": "en",
        "api_key": f"{api_key}"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    jobs_results = results["jobs_results"]
    print(jobs_results)

if __name__ == '__main__':
    load_dotenv()
    test_serp()
