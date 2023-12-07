from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
import argparse

def job_offer_research(query, api_key):
    params = {
        'engine': 'google_jobs',
        'q': query,
        'api_key': api_key,
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    for job_result in results.get('jobs_results', []):
        print(f"Title: {job_result.get('title')}")
        print(f"Company: {job_result.get('company', 'Google Inc.')}\n")
        print(f"Location: {job_result.get('location')}")
        print(f"Description: {job_result.get('snippet')}")
        print("\n" + "=" * 50 + "\n")

def candidates_research(query, api_key):
    params = {
        'q': query,
        'api_key': api_key,
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    for organic_result in results.get('organic_results', []):
        print(f"Title: {organic_result.get('title')}")
        print(f"URL: {organic_result.get('link')}")
        print(f"Description: {organic_result.get('snippet')}")
        print("\n" + "=" * 50 + "\n")

if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv("SERPAPI_PRIVATE_KEY")
    query = 'site:linkedin.com/in/ AND "Python developer"'
    parser = argparse.ArgumentParser(description='Google researches for candidates or offers.')
    parser.add_argument('type', choices=['candidate', 'offer'], help='What kind of research (candidate or offer)')
    args = parser.parse_args()


    if args.type == 'candidate':
        candidates_research(query, api_key)
    elif args.type == 'offer':
        job_offer_research(query, api_key)
    else:
        print("Type must be 'candidate' or 'offer'")
