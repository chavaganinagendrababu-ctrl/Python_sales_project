# Sales Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 📊 Project Overview

This Python project creates an interactive, animated sales analytics dashboard that visualizes key business metrics from retail sales data. The dashboard features 5 comprehensive charts that provide insights into revenue trends, product performance, category distribution, pricing analysis, and regional sales.

Perfect for data analysts, business intelligence professionals, and decision-makers seeking quick insights into sales performance.

## ✨ Key Features

### 📈 5 Key Charts:
1. **Monthly Revenue Trend** - Line chart showing revenue progression throughout the year
2. **Top 10 Products by Revenue** - Bar chart highlighting best-performing products
3. **Revenue Distribution by Category** - Pie chart showing category-wise revenue breakdown
4. **Price vs Profit Analysis** - Scatter plot analyzing pricing strategy effectiveness
5. **Revenue by Region** - Bar chart displaying geographical sales performance

### 🎯 Technical Highlights:
- **Animated Visualization**: Smooth, progressive chart animations for engaging presentations
- **Professional Styling**: Clean, modern design with consistent color schemes and typography
- **Data Processing**: Robust data cleaning and aggregation using pandas
- **Export Options**: Saves both animated GIF and static PNG formats
- **Object-Oriented Design**: Modular, maintainable code structure

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations |
| **Matplotlib** | Data visualization and animation |
| **Seaborn** | Enhanced plotting styles |
| **Pillow** | Image processing |

## 📁 Project Structure

```
├── main.py                      # Main dashboard script
├── Update.dataset.csv           # Sales data input (5,000 records)
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── LICENSE                      # MIT License
├── CHANGELOG.md                 # Version history
├── CONTRIBUTING.md              # Contribution guidelines
├── .gitignore                   # Git ignore rules
├── .gitattributes              # Git attributes
└── project/                     # Virtual environment (not in git)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/chavaganinagendrababu-ctrl/Python_sales_project.git
   cd Python_sales_project
   ```

2. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/macOS
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Dashboard

```bash
python main.py
```

The script will generate:
- `sales_dashboard_animation.gif` - Animated dashboard
- `sales_dashboard_static.png` - Static PNG image

## 📊 Dataset Information

**File:** `Update.dataset.csv`  
**Records:** 5,000 sales transactions  
**Columns:** 13 fields

| Column | Description |
|--------|-------------|
| order_id | Unique order identifier |
| product | Product name |
| category | Product category |
| sub_category | Product subcategory |
| price | Original product price |
| quantity | Units sold |
| discount_percent | Discount applied |
| final_price | Price after discount |
| cost_price | Cost to purchase |
| profit | Profit margin |
| date | Transaction date |
| customer_id | Customer identifier |
| region | Sales region |

## 💡 Use Cases

- **Personal Analysis**: Analyze your own sales data
- **Business Intelligence**: Present sales performance to stakeholders
- **Learning**: Explore data visualization with pandas and matplotlib
- **Template**: Use as a base for similar analytics projects
- **Presentations**: Professional dashboard for client meetings

## 📈 Output Examples

The dashboard generates professional visualizations showing:
- Revenue trends over time
- Product performance rankings
- Category-wise revenue distribution
- Pricing and profit relationships
- Regional sales performance

## 🔧 Configuration

Edit `main.py` to customize:
- Chart colors and styles
- Output file names and formats
- Data processing parameters
- Animation speed and effects

## 📝 Code Example

```python
from main import SalesDashboard

# Initialize dashboard
dashboard = SalesDashboard('Update.dataset.csv')

# Generate visualizations
dashboard.load_data()
dashboard.process_data()
dashboard.create_dashboard()
```

## 🤝 Contributing

This is a personal project, but feel free to fork it, modify it, or use it as a reference for your own work!

**Want to adapt this for your needs?**
1. Fork the repository
2. Modify the code to fit your dataset
3. Customize charts and analysis
4. Share your improvements (optional)

For detailed development setup, see [CONTRIBUTING.md](CONTRIBUTING.md)

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 📞 Support

- **Issues**: Report bugs and request features via GitHub Issues
- **Discussions**: Join discussions for questions and ideas
- **Documentation**: Check README and inline code comments

## 🎓 Learning Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Guide](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)

## 🔄 Version History

See [CHANGELOG.md](CHANGELOG.md) for complete version history and planned features.

## 📊 Current Version

**Version:** 1.0.0  
**Last Updated:** May 26, 2024  
**Status:** Active & Maintained

---

**Made with ❤️ by Chavagani Nagendra Babu**  
*Passionate about Data Analysis & Business Intelligence*
   source project/bin/activate      # Linux/Mac
   ```

3. **Run the Dashboard**:
   ```bash
   python prj.py
   ```

4. **Output**: The script generates both animated and static versions of the dashboard

## 📈 Sample Insights

The dashboard reveals:
- Seasonal revenue patterns and peak months
- Top-performing products driving sales
- Category dominance in the product portfolio
- Profitability analysis across different price points
- Regional market performance and opportunities

## 🎨 Design Philosophy

- **Clean Aesthetics**: Minimalist design with professional color palette
- **Accessibility**: High contrast colors and clear typography
- **Interactivity**: Animated elements for dynamic presentations
- **Scalability**: Modular code structure for easy customization

## 📊 Data Source

The analysis uses retail sales transaction data including:
- Product information and categories
- Pricing and profitability metrics
- Customer demographics and regions
- Transaction dates and quantities

## 🔧 Customization

The `SalesDashboard` class can be easily extended to:
- Add new chart types
- Modify color schemes
- Include additional KPIs
- Change animation parameters
- Export to different formats

## 📝 License

This project is open-source and available for educational and professional use.

---

*Created with ❤️ for data-driven decision making*</content>
<parameter name="filePath">d:\DA Projects\Python_Sales_project\README.md