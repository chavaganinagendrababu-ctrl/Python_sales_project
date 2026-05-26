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
│
├── sales_dashboard_animation.gif    # Generated: Animated dashboard
├── sales_dashboard_static.png       # Generated: Static dashboard
│
└── project/                     # Virtual environment (not in git)
```

**Generated Files (After Running main.py):**
- `sales_dashboard_animation.gif` - Animated visualization
- `sales_dashboard_static.png` - Static image export

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

**Generation Time:** ~30-60 seconds depending on your system  
**Output Size:** ~6-8 MB total (GIF + PNG)

### 📁 Dashboard Output Files

After running the script, you'll find two files in your project directory:

| File | Type | Size | Best For |
|------|------|------|----------|
| `sales_dashboard_animation.gif` | Animated GIF | ~5-6 MB | Presentations, video embeds |
| `sales_dashboard_static.png` | Static Image | ~1-2 MB | Reports, documentation |

**Note:** These are generated files and are not tracked in git (.gitignore excludes them). You can safely delete and regenerate them by running `python main.py` again.

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

### 🎬 Dashboard Outputs

When you run `main.py`, the script generates:

**1. Animated Dashboard (GIF)**
- File: `sales_dashboard_animation.gif`
- Size: ~5-6 MB
- Format: Animated GIF with smooth chart transitions
- Use: Professional presentations, stakeholder meetings, reports

**2. Static Dashboard (PNG)** 
- File: `sales_dashboard_static.png`
- Size: ~1-2 MB
- Format: High-resolution PNG image
- Use: Reports, emails, documentation

Both outputs display the same 5 key charts in a professional, visually appealing layout with:
- Clean typography and branding
- Color-coded data categories
- Clear legends and labels
- Ready for presentations and reports

## � Viewing the Dashboard

After running `python main.py`, open the generated files:

### **Animated Dashboard**
- **File:** `sales_dashboard_animation.gif`
- **Open with:** Any image viewer, web browser, or presentation software
- **Best for:** Animated presentations, email previews

### **Static Dashboard**
- **File:** `sales_dashboard_static.png`
- **Open with:** Any image viewer (Photos, Paint, Preview, etc.)
- **Best for:** Reports, documentation, high-quality output

**Windows Quick Tip:** Double-click the GIF or PNG files to view them instantly!

## 🚀 What Happens When You Run the Script?

1. **Load Data**: Reads `Update.dataset.csv` (5,000 sales records)
2. **Process Data**: Aggregates and calculates key metrics
3. **Create Charts**: Generates 5 professional visualizations:
   - Monthly Revenue Trend
   - Top 10 Products by Revenue
   - Revenue Distribution by Category
   - Price vs Profit Analysis
   - Revenue by Region
4. **Generate Outputs**: 
   - Saves animated version as `sales_dashboard_animation.gif`
   - Saves static version as `sales_dashboard_static.png`
5. **Display Results**: Shows completion message with file locations

**Execution Time:** 30-60 seconds  
**Output Quality:** High-resolution, professional-grade visualizations

## ❓ Troubleshooting

### Dashboard Files Not Generated

**Problem:** Script runs but no GIF/PNG files appear

**Solutions:**
1. Check file permissions in the project folder
2. Ensure `Update.dataset.csv` exists and is readable
3. Try running with admin privileges
4. Check console output for error messages

### Very Slow Execution

**Problem:** Script takes longer than 2 minutes

**Solutions:**
1. This is normal for large datasets (5,000+ records)
2. GIF animation generation is CPU-intensive
3. First run may be slower than subsequent runs

### Memory Issues

**Problem:** "Memory error" or script crashes

**Solutions:**
1. Close other applications
2. Reduce dataset size temporarily for testing
3. Ensure at least 2GB free RAM available
4. Update matplotlib and pillow packages

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