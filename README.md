# Fashion Product ETL Pipeline: Automated Web Scraping, Data Cleaning, and Multi-Repository Data Storage

### Project Overview
This project focuses on building an end-to-end Extract, Transform, Load (ETL) pipeline for fashion product data sourced from an e-commerce website. The pipeline automated data collection through web scraping, performs data cleaning and transformation, and stores the processed data in multiple repositories for further analysis and reporting.

The project follows software engineering best practices through modular code organization, automated testing, error handling, and separation of ETL stages into independent modules.

## Problem Statement
Fashion product information available on e-commerce websites is often presented as unstructured web content that cannot be directly used for analytical purposes.

Several data quality issues were identified:
- Invalid product names such as "Unknown Product"
- Missing prices represented as "Price Unavailable"
- Missing ratings represented as "Not Rated"
- Inconsistent formats for rating, color counts, sizes, and gender information
- Duplicate records and potential null values

Without a structured ETL process, collecting and preparing data for analysis would be time-consuming and error-prone.

## Objectives
This project aims to:
- Extract fashion product data from multiple web pages automatically.
- Collect product attributes including:
  - Title
  - Price
  - Rating
  - Colors
  - Size
  - Gender
- Record extraction timestamps.
- Improved data quality by removing invalid and incomplete records.
- Convert product prices from USD to Indonesian Rupiah (IDR).
- Store clean data in multiple repositories for future access and analysis.
- Implement automated testing to ensure pipeline reliability.

## Data Source
### Source Website
**Fashion Studio Scraping Website**
https://fashion-studio.dicoding.dev

### Data Collected
The scraper collected data from pages 1-50 (approximately 1k records), including:
| Attribute | Description |
| --------- | ----------- |
| Title | Product name |
| Price | Product price (USD) |
| Rating | Product rating |
| Colors | Available color variations |
| Size | Product size |
| Gender | Target gender category |
| Timestamp | Extraction timestamp |

## Tools & Technologies
### Programming Language
- Python

### Data Collection
- Request
- BeautifulSoup4

### Data Processing
- Pandas

### Database
- PostgreSQL
- SQLAlchemy
- Psycopg2

### Cloud / Storage
- Google Sheets API
- CSV

### Testing
- Pytest
- Coverage

### Additional Tools
- Google Cloud Service Account
- Git & GitHub

## Methodology / Process
### 1. Extract
Developed a web scraper using `Requests` and `BeautifulSoup` to collect product information from all available pages.

Key activities:
- Sent HTTP requests to website pages
- Parsed HTML content
- Extracted product attributes
- Recorded extraction timestamps
- Implemented exception handling for network and parsing errors


### 2. Transform
Performed data cleaning and standardization:

#### Data Quality Checks
Removed:
- Unknown Product
- Price Unavailable
- Not Rated
- Invalid rating

#### Data Standardization
Converted:
- **Price** from `$102.15` to `1634400 IDR` using `1 USD = Rp16,000`
- **Rating** from `Rating: ⭐ 4.8 / 5` to `4.8`
- **Colors** from `3 Colors` to `3`
- **Size** from `Size: XL` to `XL`
- **Gender** from `Gender: Women` to `Women`

#### Additional Cleaning
- Removed null values
- Removed duplicate records
- Converted columns into appropriate data types

### 3. load
Stored processed data into multiple repositories:
- **CSV**: Local flat-file storage
- **PostgreSQL**: Relational database for structured storage and querying.
- **Google Sheets**: Cloud-based spreadsheet for reporting and collaboration.


## Key Findings / Insights
Based on the ETL process:

### Data Quality Issues were Significant
A noticeable portion of scraped records contained:
- Unknown product names
- Missing prices
- Missing ratings

These records required removal before analysis.

### Multi-Step Cleaning was Necessary
raw web data included multiple formatting inconsistencies that made direct analysis impossible without transformation.

Examples:
- Currency stored as text strings
- Ratings embedded within descriptive text
- Product attributes mixed with labels

### Automated Data Collection Improved Efficieny
The scraper successfully processed approximately 1k records across 50 website pages automatically, eliminating the need for manual collection.

### Multi-Repository Storage Increased Accessibility
Data became accessible for:
- Analytical querying through PostgreSQL
- Spreadsheet-based reporting through Google Sheets
- Offline storage through CSV exports

## Skills Demonstrated
- Web Scraping
- ETL Pipeline Development
- Data Cleaning & Preprocessing
- Data Validation
- Python Programming
- PostgreSQL
- SQL
- Google Sheets API
- API Integration
- Unit Testing (Pytest)
- Error Handling
- Data Engineering Fundamentals
- Data Quality Management
