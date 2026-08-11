# 🚀 Python Web Scraping & Data Extraction Portfolio

Welcome to my central repository for **Web Scraping, Data Pipeline & Automation Engineering**. This showcase tracks my 3-month journey building scalable data extraction tools, handling dynamic websites, bypassing anti-bot measures, and exporting production-ready datasets.

---

## 🛠️ Tech Stack & Key Competencies

* **Core Language:** Python 3
* **Libraries & Frameworks:** `requests`, `beautifulsoup4` (BS4)
* **Data Processing & Export:** `csv`, `sys`
* **Key Skills:** HTML Parsing, Multi-Page Pagination, UTF-8 Encoding Handling, HTTP Status Validation, Structured Data Export (Excel / CSV Compatible)

---

## 📂 Project Showcase

### 📌 Project 1: Quotes & Author Metadata Scraper (Week 1)
> **Automated extraction of quotes, authors, and category tags.**

* **Target Site:** [Quotes to Scrape](https://quotes.toscrape.com/)
* **Script File:** [`quotes_scraper.py`](./quotes_scraper.py)
* **Sample Output Dataset:** [`quotes.csv`](./quotes.csv)

#### Key Technical Highlights:
* **Encoding Optimization:** Reconfigured stdout stream to `UTF-8` using `sys.stdout.reconfigure()` to avoid cross-platform encoding bugs.
* **Efficient Tag Parsing:** Utilized Python list comprehension (`', '.join([...])`) to combine dynamic dynamic multi-element tags into clean strings.
* **Clean Terminal Output:** Formatted string outputs with structured separators for quick debugging and logging.

---

### 📌 Project 2: Multi-Page E-Commerce Catalog Scraper with CSV Pipeline (Week 2)
> **Paginated data extraction pipeline saving e-commerce data directly into Excel-friendly CSV formats.**

* **Target Site:** [Books to Scrape](https://books.toscrape.com/)
* **Script File:** [`project2_books.py`](./project2_books.py)
* **Sample Output Dataset:** [`books_data.csv`](./books_data.csv)

#### Key Technical Highlights:
* **Automated Pagination Loop:** Built a dynamic loop scraping across multiple catalog pages (`page-1` to `page-5`).
* **Robust Attribute Extraction:** Extracted full, unabbreviated book titles directly from HTML `title` attributes rather than truncated text nodes.
* **HTTP Error Handling:** Implemented status code validation (`response.status_code == 200`) to guarantee execution safety against broken URLs.
* **Excel-Compatible Data Export:** Exported datasets using `utf-8-sig` encoding to preserve special currency symbols (e.g., `£`) when opened in Microsoft Excel.

---

## 📊 Sample Data Output Preview (`books_data.csv`)

| Title | Price | Availability |
| :--- | :--- | :--- |
| A Light in the Attic | £51.77 | In stock |
| Tipping the Velvet | £53.74 | In stock |
| Soumission | £50.10 | In stock |

---

## ⚙️ How to Run These Projects Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mdhossainali866-cloud/3-month-scraping-journey.git
