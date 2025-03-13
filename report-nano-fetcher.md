# 📊 NanoFetch Project Report

## 📝 Introduction

**NanoFetch** is an advanced Python tool designed to streamline the process of fetching, analyzing, and summarizing research papers from PubMed. The project leverages OpenAI's Large Language Models (LLMs) to enhance search queries and summarize research abstracts, ensuring efficient and meaningful data retrieval.

---

## 🚀 Approach

The primary objective of NanoFetch was to:
1. **Simplify the Research Process** by automating the retrieval and summarization of academic papers from PubMed.
2. **Enhance Search Flexibility** using LLMs to refine user queries and ensure broader, more accurate search results.
3. **Identify Non-Academic Authors** and highlight their company affiliations for deeper insight into the authorship of research papers.
4. **Provide Structured Data** by saving the results into a clean, well-organized CSV file for easy analysis.

---

## ⚙️ Methodology

### 1. **Query Processing**
- User inputs a flexible search query.
- The query is enhanced using OpenAI's LLM to extract key concepts and ensure better search results.
- **Fallback Logic:** If the OpenAI API quota is exhausted, the original query is used without enhancement.

### 2. **Data Fetching**
- Utilized PubMed's E-utilities API to search for and fetch relevant research papers based on the refined query.
- For each identified paper, detailed information including title, publication date, and authorship details were retrieved.

### 3. **Non-Academic Author Detection**
- The system scanned author affiliations to identify non-academic contributors (e.g., company names vs. academic institutions).
- Extracted and listed company affiliations and corresponding author emails where available.

### 4. **LLM Summarization**
- Abstracts from the fetched research papers were summarized using OpenAI's LLM to provide quick insights.
- **Fallback Logic:** If the API quota was exhausted, summaries were marked as "Summary not available due to quota limits."

### 5. **Data Storage**
- All relevant data was saved into a structured CSV file named `result-paper-fetcher.csv`, containing fields such as:
  - PubMed ID
  - Title
  - Publication Date
  - Non-Academic Authors
  - Company Affiliations
  - Corresponding Author Email
  - LLM Summary

### 6. **Error Handling & Logging**
- Detailed logging was implemented to:
  - Track API requests and responses.
  - Capture errors (e.g., quota exhaustion, API failures).
  - Maintain transparency for debugging purposes.

---

## ✅ Results

- Successfully retrieved and summarized research papers from PubMed based on flexible user queries.
- LLM-enhanced queries provided broader and more relevant research results.
- Automated summarization allowed for quick understanding of complex research papers.
- Identified and extracted data about non-academic authors and their company affiliations.
- Gracefully handled API quota exhaustion by falling back to basic functionalities without breaking the process.
- All results were saved in a structured, analysis-ready CSV file.

---

## 🔍 Observations & Learnings

- **LLM Integration:** Enhanced the overall quality of results but depends on quota availability.
- **Flexible Query Handling:** Made the search process more intuitive and user-friendly.
- **Fallback Logic:** Essential for ensuring uninterrupted data processing, especially during quota limits.
- **Logging:** Helped in effective debugging and provided transparency in the process.

---

## 📈 Recommendations for Future Enhancements

1. **Improve Summarization Depth:** Utilize more advanced models for deeper summarization.  
2. **Implement Caching:** To avoid redundant API calls for repeated queries.  
3. **User Interface (Optional):** Create a web-based interface for easier usage.  
4. **Dynamic Error Handling:** Introduce better error categorization for API responses.

---

## 🎯 Conclusion

NanoFetch has successfully demonstrated an efficient, intelligent, and robust solution for automating research paper retrieval and summarization. The integration of LLMs significantly enhances the search process and abstract summarization, making the tool a valuable asset for academic and industrial research purposes.

---

**NanoFetch** – Empowering smarter, faster research with AI 🚀

