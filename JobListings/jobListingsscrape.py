import requests

def fetch_jobs(keyword, api_key, cse_id, location=None, job_type=None):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': f"{keyword} {location if location else ''} {job_type if job_type else ''}",
        'num': 10
    }
    response = requests.get(url, params=params)
    results = response.json()
    
    jobs = []
    for item in results.get('items', []):
        title = item.get('title')
        link = item.get('link')
        snippet = item.get('snippet')
        
        # Filter based on additional criteria (e.g., contains certain keywords)
        if 'developer' in title.lower():
            jobs.append({
                'title': title,
                'link': link,
                'snippet': snippet
            })
    
    return jobs

# Replace with your actual API key and CSE ID
api_key = 'AIzaSyDnVndOjZ4_XckKLJkza_cvbLpJOkluiWU'
cse_id = '25f7cc982384c491b'

keyword = 'TIBCO developer'
location = 'Washington'
job_type = 'full-time'
job_listings = fetch_jobs(keyword, api_key, cse_id, location, job_type)

for job in job_listings:
    print(f"Title: {job['title']}")
    print(f"Link: {job['link']}")
    print("Snippet:", job['snippet'])
    print("-----")
