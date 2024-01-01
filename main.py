from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
import argparse

def job_offer_research(query, api_key, args):
    params = {
        'engine': 'google_jobs',
        'q': query,
        'api_key': api_key,
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    for job_result in results.get('jobs_results', []):
        if args in job_result.get('description'):
            print(job_result)

def candidates_research(query, api_key, args):
    params = {
        'q': query,
        'api_key': api_key,
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    for organic_result in results.get('organic_results', []):
        if args in organic_result.get('snippet'):
            print(organic_result)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv("SERPAPI_PRIVATE_KEY")
    parser = argparse.ArgumentParser(description='Google researches for candidates or offers.')
    parser.add_argument('type', choices=['candidate', 'offer'], help='What kind of research (candidate or offer)')
    parser.add_argument('query', help='The query to search for')
    args = parser.parse_args()


    if args.type == 'candidate':
        candidates_research(f'site:linkedin.com/in/ AND {args.query}', api_key, args.query)
    elif args.type == 'offer':
        job_offer_research(f'site:linkedin.com/in/ AND {args.query}', api_key, args.query)
    else:
        print("Type must be 'candidate' or 'offer'")
