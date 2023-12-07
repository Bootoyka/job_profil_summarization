from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
import argparse


def generate_random_description(job_title):
    job_descriptions = {
        "Python Developer": (
            "As an accomplished Python developer, I bring a wealth of experience in crafting robust and scalable "
            "software solutions. My expertise lies in designing and implementing sophisticated backend systems, "
            "APIs, and data processing pipelines. I am well-versed in deploying best practices for software "
            "development, ensuring clean, efficient, and maintainable code. My commitment to excellence and my "
            "strong problem-solving skills make me a valuable asset to any team or project."
        ),
        "Software Engineer": (
            "In the realm of software engineering, I am recognized as an innovative professional dedicated to "
            "building systems that stand the test of time. My proficiency spans a diverse array of programming "
            "languages and technologies, allowing me to navigate the complexities of full-stack development with "
            "seamless ease. From database design to user interface implementation, my skills contribute to the "
            "creation of robust and high-performance software solutions."
        ),
        "Data Scientist": (
            "Embarking on the fascinating journey of data science, I bring a wealth of expertise in analyzing and "
            "interpreting intricate datasets. My skills encompass the realm of machine learning, statistical "
            "analysis, and data visualization. With a proven track record, I specialize in deriving actionable "
            "insights that drive informed decision-making. As a data scientist, I am passionate about unlocking "
            "the potential within data to propel organizations forward."
        ),
    }

    return job_descriptions.get(job_title, "Dynamic and skilled professional in the technology industry.")

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
        print(f"Description: {job_result.get('description')}")
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
        if "Python" or "Developer" in organic_result.get('title'):
            print(f"Description: {generate_random_description('Python Developer')}")
        elif "Software" or "Engineer" in organic_result.get('title'):
            print(f"Description: {generate_random_description('Software Engineer')}")
        elif "Data" or "Scientist" in organic_result.get('title'):
            print(f"Description: {generate_random_description('Data Scientist')}")
        else:
            print("Description: Dynamic and skilled professional in the technology industry.")
        print("\n" + "=" * 50 + "\n")

if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv("SERPAPI_PRIVATE_KEY")
    parser = argparse.ArgumentParser(description='Google researches for candidates or offers.')
    parser.add_argument('type', choices=['candidate', 'offer'], help='What kind of research (candidate or offer)')
    parser.add_argument('query', help='The query to search for')
    args = parser.parse_args()
    query = f'site:linkedin.com/in/ AND {args.query}'


    if args.type == 'candidate':
        candidates_research(query, api_key)
    elif args.type == 'offer':
        job_offer_research(query, api_key)
    else:
        print("Type must be 'candidate' or 'offer'")
