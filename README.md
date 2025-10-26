# Vendor Analytics Dashboard

## 📊 Overview
Vendor Analytics is a comprehensive data analytics solution designed to help businesses optimize their vendor relationships, inventory management, and pricing strategies. This project provides insights into vendor performance, product profitability, and inventory turnover through interactive dashboards and detailed reports.

## 🏗️ Project Structure
```
Vendor_Analytics/
├── data/                      # Raw data files
│   ├── begin_inventory.csv    # Initial inventory records
│   ├── end_inventory.csv      # Ending inventory records
│   ├── purchase_prices.csv    # Product purchase pricing
│   ├── purchases.csv          # Purchase transactions
│   ├── sales.csv             # Sales transactions
│   └── vendor_invoice.csv     # Vendor invoice details
├── logs/                     # Log files
├── notebooks/                # Jupyter notebooks for analysis
│   ├── Data_Ingestion(csv-to-sql).ipynb
│   ├── Exploraory Data Analysis.ipynb
│   ├── Testing.ipynb
│   └── Vendor Performance Analysis.ipynb
├── output/                   # Generated reports and outputs
│   ├── BrandPerformance.csv
│   ├── LowTurnOver.csv
│   ├── PurchaseContribution.csv
│   └── vendor_sales_summary.csv
├── inventory.db              # SQLite database
├── get_vendor_summary.py     # Script to generate vendor summaries
├── ingestion_db.py          # Database ingestion utilities
└── README.md                # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Jupyter Notebook/Lab (for running analysis notebooks)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Vendor_Analytics
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
   
   If requirements.txt doesn't exist, install the following packages:
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter scipy sqlalchemy
   ```

### Database Setup
1. Ensure all CSV files are placed in the `data/` directory
2. Run the data ingestion notebook to populate the SQLite database:
   ```bash
   jupyter notebook notebooks/Data_Ingestion(csv-to-sql).ipynb
   ```
   
   Or run the Python script directly:
   ```bash
   python ingestion_db.py
   ```

## 🗃️ Data Model

### Key Entities
- **Vendors**: Information about product suppliers
- **Products**: Details of items in inventory
- **Purchases**: Records of products bought from vendors
- **Sales**: Records of products sold to customers
- **Inventory**: Stock level tracking

### Database Schema
```sql
-- Vendors
CREATE TABLE vendors (
    VendorNumber INT PRIMARY KEY,
    VendorName TEXT,
    Brand INT
);

-- Products
CREATE TABLE products (
    Brand INT,
    Description TEXT,
    Size TEXT,
    -- Additional product attributes
);

-- Purchases
CREATE TABLE purchases (
    PurchaseID TEXT,
    VendorNumber INT,
    PurchaseDate DATE,
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    TotalAmount DECIMAL(12,2),
    -- Additional purchase fields
);

-- Sales
CREATE TABLE sales (
    SaleID TEXT,
    SaleDate DATE,
    ProductID INT,
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    TotalAmount DECIMAL(12,2),
    -- Additional sales fields
);
```

## 📈 Key Features

### 1. Vendor Performance Analysis
- Track vendor performance metrics
- Analyze purchase patterns and volumes
- Evaluate vendor profitability and reliability

### 2. Inventory Management
- Monitor stock levels and turnover rates
- Identify slow-moving items
- Optimize reorder points and quantities

### 3. Pricing Strategy
- Analyze price elasticity
- Compare purchase vs. sales prices
- Identify margin improvement opportunities

### 4. Sales Analytics
- Track sales trends and patterns
- Analyze product performance
- Generate sales forecasts

## 🛠️ Usage

### Running the Analysis
1. Open the Jupyter notebooks in the `notebooks/` directory
2. Execute cells in sequence to perform analyses
3. Visualizations and reports will be generated within the notebooks

### Generating Reports
```python
# Example: Generate vendor performance report
from get_vendor_summary import generate_vendor_report

generate_vendor_report(vendor_id=1234, output_file='vendor_1234_report.html')
```

## 📊 Sample Outputs

### Vendor Performance Dashboard
- Vendor ranking by sales volume and profitability
- Trend analysis of purchase and sales data
- Performance metrics and KPIs

### Inventory Reports
- Stock level analysis
- Turnover rates by product category
- Reorder recommendations

### Financial Analysis
- Gross margin analysis
- Cost of goods sold (COGS) breakdown
- Profitability by vendor and product

## 📦 Dependencies

### Core Dependencies
- Python 3.8+
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter
- SQLAlchemy

### Development Dependencies
- flake8 (for code linting)
- pytest (for testing)
- black (for code formatting)

## 🤝 Contributing

### Bug Reports & Feature Requests
Please use the [issue tracker](https://github.com/yourusername/vendor-analytics/issues) to report any bugs or request new features.

### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


---
<div align="center">
  Made with ❤️ by Sarthak
</div>
