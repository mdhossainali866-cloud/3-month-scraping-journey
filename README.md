<div align="center">

# 🚀 Automated Data Pipeline & Web Scraping Journey

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Pipeline-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/Data_Export-CSV_%2F_JSON-orange?style=for-the-badge)

**A 3-Month Production-Grade Showcase of Web Scraping, Hidden API Parsing, Data Pipeline Engineering & Automation.**

[Explore Projects](#-project-showcase) • [Tech Stack](#-tech-stack--architecture) • [How to Run](#-environment-setup)

---

</div>

## 🏗️ System Architecture & Workflow

```text
┌────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│  Target Source │ ──> │ Extraction Pipeline  │ ──> │ Data Transformation │
│ (HTML/REST API)│     │  (Requests / BS4)    │     │  (Pandas/CSV/JSON)   │
└────────────────┘     └──────────────────────┘     └──────────────────────┘
                                                               │
                                                               ▼
                                                    ┌──────────────────────┐
                                                    │  Historical Logging  │
                                                    │   (UTF-8-SIG CSV)    │
                                                    └──────────────────────┘
```

---

## 🛠️ Tech Stack & Architecture

| Category | Tools / Libraries | Usage |
| :--- | :--- | :--- |
| **Core Language** | Python 3 | Main Script Execution & Automation |
| **Data Fetching** | `requests` | HTTP Protocol Handling, Status Handling, REST API Queries |
| **HTML Parsing** | `beautifulsoup4` | DOM Tree Traversal, Dynamic Attribute Extraction |
| **Data Engine** | `csv`, `json`, `os` | Historical Append Logging, Payload Extraction, UTF-8 Management |
| **Time & Delays** | `datetime`, `time` | Precise Datetime File Stamping & Polite Throttling |

---

## 📂 Project Showcase

### 📌 Week 1: Quotes & Author Metadata Scraper
* **Type:** Static HTML Scraper
* **Source:** [Quotes to Scrape](https://quotes.toscrape.com/)
* **Files:** [`quotes_scraper.py`](./quotes_scraper.py) | [`quotes.csv`](./quotes.csv)

**Key Highlights:**
* Handled cross-platform standard output stream encoding via `sys.stdout.reconfigure(encoding='utf-8')`.
* Clean string serialization for multi-element metadata using Python list comprehensions.

---

### 📌 Week 2: Multi-Page E-Commerce Catalog Scraper
* **Type:** Paginated HTML Scraper
* **Source:** [Books to Scrape](https://books.toscrape.com/)
* **Files:** [`project2_books.py`](./project2_books.py) | [`books_data.csv`](./books_data.csv)

**Key Highlights:**
* Implemented dynamic multi-page pagination loops across sequential catalog endpoints.
* Extracted unabbreviated product titles from raw HTML attributes rather than truncated visual elements.
* Exported datasets using `utf-8-sig` encoding to prevent character corruption when opened in Microsoft Excel.

---

### 📌 Week 3: Real-Time Crypto Tracker & Time-Series Engine
* **Type:** Hidden/Public REST API Scraper
* **Source:** CoinGecko Public REST API
* **Files:** [`project3_crypto.py`](./project3_crypto.py) | [`crypto_history.csv`](./crypto_history.csv)

**Key Highlights:**
* **Bypassed DOM Parsing:** Directly targeted JSON API endpoints for zero-latency, structure-safe data fetching.
* **Smart Historical Logging Engine:** Used File I/O checks (`os.path.isfile`) with append mode (`'a'`) to build a historical time-series dataset without duplicate header rows.
* **Financial Data Formatting:** Applied precision float formatting (`:,.2f`) for formatted currency outputs in USD ($) and BDT (৳).

---

### 📌 Week 4: Multi-Source Hybrid Tech News Aggregator
* **Type:** Hybrid Data Pipeline (REST API + Dynamic HTML Scraping)
* **Sources:** [Hacker News Firebase API](https://hacker-news.firebaseio.com/) | [Dev.to](https://dev.to/)
* **Files:** [`tech_news_scraper.py`](./tech_news_scraper.py) | [`tech_news_2026-08-29.csv`](./tech_news_2026-08-29.csv)

**Key Highlights:**
* **Hybrid Extraction Architecture:** Combined JSON REST API querying and HTML DOM Parsing into a single unified extraction pipeline.
* **Dynamic Datetime File Stamping:** Automated daily dataset exports using `datetime.now()` to construct time-stamped CSV filenames.
* **Relative URL Normalization:** Implemented link prefix logic to resolve full HTTP paths for relative Dev.to post links.
* **Rate Limiting Handling:** Configured polite request pauses (`time.sleep`) to adhere to API consumption best practices.

---

## 📊 Live Sample Data Output Preview (`crypto_history.csv`)

| Timestamp | BTC_USD | BTC_BDT | ETH_USD | ETH_BDT | SOL_USD | SOL_BDT |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2026-08-16 20:36:00** | $65,420.50 | ৳7,850,460.00 | $3,450.20 | ৳414,024.00 | $145.80 | ৳17,496.00 |

---

## ⚙️ Environment Setup & Execution

```bash
# 1. Clone the repository
git clone [https://github.com/mdhossainali866-cloud/3-month-scraping-journey.git](https://github.com/mdhossainali866-cloud/3-month-scraping-journey.git)

# 2. Navigate into project folder
cd 3-month-scraping-journey

# 3. Install required packages
pip install requests beautifulsoup4

# 4. Run Projects
python project3_crypto.py
python tech_news_scraper.py
```