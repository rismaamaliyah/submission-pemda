# Automated Fashion Market Data Collection and ETL Workflow

## Overview
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
