import os
import openai
import requests
import logging
import csv
import argparse
from typing import List, Dict, Optional

def setup_logging(debug: bool):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_openai():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OpenAI API Key is not set in environment variables.")

def enhance_query_with_llm(query: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert research assistant. Simplify the following query for PubMed search, extracting essential concepts."},
                {"role": "user", "content": query}
            ],
            max_tokens=50,
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except openai.RateLimitError:
        logging.warning("Quota exceeded. Skipping LLM query enhancement.")
        return query
    except Exception as e:
        logging.error(f"LLM query enhancement error: {e}")
        return query

def summarize_text_with_llm(text: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize the following research abstract."},
                {"role": "user", "content": text}
            ],
            max_tokens=100,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except openai.RateLimitError:
        logging.warning("Quota exceeded. Skipping LLM summarization.")
        return "Summary not available due to quota limits."
    except Exception as e:
        logging.error(f"LLM summarization error: {e}")
        return "Summary not available."

def fetch_pubmed_papers(query: str, max_results: int = 100) -> List[Dict]:
    refined_query = enhance_query_with_llm(query)
    logging.info(f"Refined query: {refined_query}")
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": refined_query,
        "retmax": max_results,
        "retmode": "json"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    id_list = response.json()['esearchresult']['idlist']

    papers = []
    for paper_id in id_list:
        papers.append(fetch_paper_details(paper_id))

    return papers

def fetch_paper_details(paper_id: str) -> Dict:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": paper_id,
        "retmode": "json"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    doc = response.json()['result'][paper_id]
    
    authors, companies, email = extract_non_academic_authors(doc)
    abstract = doc.get('title', '')
    summary = summarize_text_with_llm(abstract)

    return {
        "PubmedID": doc.get("uid", "N/A"),
        "Title": doc.get("title", "N/A"),
        "Publication Date": doc.get("pubdate", "N/A"),
        "Non-academic Author(s)": ", ".join(authors) or "None",
        "Company Affiliation(s)": ", ".join(companies) or "None",
        "Corresponding Author Email": email or "Not Available",
        "LLM Summary": summary
    }

def extract_non_academic_authors(doc: Dict) -> (List[str], List[str], str):
    authors = []
    companies = []
    email = ""
    for author in doc.get('authors', []):
        affiliation = author.get('affiliation', '').lower()
        if not any(keyword in affiliation for keyword in ["university", "institute", "college", "labs"]):
            authors.append(author.get('name', "Unknown"))
            companies.append(affiliation)
            if "@" in affiliation:
                email = affiliation.split()[-1]
    return authors, companies, email

def save_to_csv(papers: List[Dict], filename: Optional[str]):
    fieldnames = ['PubmedID', 'Title', 'Publication Date', 'Non-academic Author(s)',
                  'Company Affiliation(s)', 'Corresponding Author Email', 'LLM Summary']
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for paper in papers:
            writer.writerow(paper)

def main():
    parser = argparse.ArgumentParser(description='Fetch and summarize PubMed research papers.')
    parser.add_argument('query', type=str, help='Search query for PubMed.')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug output.')
    parser.add_argument('-f', '--file', type=str, help='Filename to save results (CSV).')

    args = parser.parse_args()
    setup_logging(args.debug)

    try:
        setup_openai()
        logging.info(f"Fetching papers for query: {args.query}")
        papers = fetch_pubmed_papers(args.query)
        
        if args.file:
            save_to_csv(papers, args.file)
            logging.info(f"Saved {len(papers)} papers to {args.file}")
        else:
            for paper in papers:
                print(paper)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()






