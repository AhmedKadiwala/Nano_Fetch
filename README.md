# Nano_Fetch
NanoFetch is an intelligent Python tool that fetches and summarizes research papers from PubMed. Leveraging OpenAI's LLM, it enhances search queries, identifies non-academic authors, and generates concise summaries—automatically saving results to a structured CSV.
# 📄 NanoFetch - Smarter Research Paper Retrieval

**NanoFetch** is an intelligent Python tool that fetches, processes, and summarizes research papers from PubMed. Leveraging advanced LLM (Large Language Model) capabilities, it enhances search flexibility and generates concise summaries—streamlining research workflows effortlessly.

---

## 🚀 Features

- **🔍 Flexible Query Processing:**
  - Utilizes LLMs to enhance and refine search queries, ensuring better and broader research paper discovery.

- **📑 Automated Summarization:**
  - Summarizes abstracts of fetched research papers using OpenAI's advanced LLM, offering quick insights.

- **🏢 Non-Academic Author Detection:**
  - Identifies and highlights non-academic authors and their company affiliations.

- **📄 CSV Output:**
  - Saves all results in a well-structured CSV file (`result-paper-fetcher.csv`).

- **⚡ Graceful Error Handling:**
  - Automatically skips LLM features if the OpenAI API quota is exhausted and logs clear warnings.

- **🛠️ Debugging Support:**
  - Enable detailed debug logging to monitor the process effectively.

---

## 🛠️ Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/nanofetch.git
   cd nanofetch
   ```

2. **Install Dependencies:**
   Ensure you have Python 3.8+ and Poetry installed.
   ```bash
   poetry install
   ```

3. **Set Your OpenAI API Key:**
   ```powershell
   $env:OPENAI_API_KEY="your-openai-api-key-here"
   ```
   Or add it permanently to your environment variables.

4. **Run the Script:**
   ```powershell
   python .\paper-fetcher.py "your research query" -f result-paper-fetcher.csv -d
   ```

---

## ⚙️ Command-Line Options

| Argument  | Description                               | Example                                            |
|-----------|-------------------------------------------|----------------------------------------------------|
| `query`   | The search query for PubMed.               | "nanobots in surgery"                              |
| `-f`      | (Optional) Filename to save results.       | `-f result-paper-fetcher.csv`                      |
| `-d`      | (Optional) Enable debug logging.           | `-d`                                               |

---

## ✅ Example Usage

```powershell
python .\paper-fetcher.py "use of nanobots in medical industries" -f result-paper-fetcher.csv -d
```

---

## 🤖 How LLM Enhances the Project

1. **Query Enhancement:**
   - Automatically refines user queries using OpenAI's GPT-3.5-turbo for more flexible and accurate PubMed searches.

2. **Summarization:**
   - Summarizes research abstracts to provide concise overviews of each paper.

3. **Fallback Logic:**
   - If the OpenAI API quota is exhausted, the system gracefully skips LLM steps without breaking the process.

---

## 🧰 Project Structure

```
nanofetch/
├── paper-fetcher.py      # Main Python script
├── result-paper-fetcher.csv # Output file
├── README.md             # Project documentation
├── pyproject.toml        # Poetry dependency management
└── ...
```

---

## ⚠️ Troubleshooting

- **Quota Exhaustion:**
  - If the OpenAI API quota is exceeded, LLM features will be skipped, and a warning will be logged.

- **`ModuleNotFoundError`:**
  - Ensure all dependencies are installed with `poetry install`.

- **`OPENAI_API_KEY` Error:**
  - Confirm the API key is correctly set in your environment variables.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## 📬 Contact

For any questions or feedback, reach out to [Ahmed Kadiwala](mailto:kadiwalaahmed7864@gmail.com).

---

**NanoFetch** – Simplifying research, one query at a time 🚀
