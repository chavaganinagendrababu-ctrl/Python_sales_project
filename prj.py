"""
Sales Dashboard Analysis
========================

This script creates an attractive and professional animated dashboard
visualizing sales data with 5 key charts:

1. Monthly Revenue Trend
2. Top 10 Products by Revenue
3. Revenue Distribution by Category
4. Price vs Profit Analysis
5. Revenue by Region

Author: [Your Name]
Date: [Current Date]
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

# Set professional style
plt.style.use('seaborn-v0_8')
plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'figure.titlesize': 16,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10
})


class SalesDashboard:
    """
    A professional sales dashboard class for visualizing sales analytics.
    """

    def __init__(self, data_path):
        """
        Initialize the dashboard with data.

        Args:
            data_path (str): Path to the CSV data file
        """
        self.df = self._load_and_clean_data(data_path)
        self._prepare_data()

    def _load_and_clean_data(self, path):
        """
        Load and clean the sales data.

        Args:
            path (str): Path to CSV file

        Returns:
            pd.DataFrame: Cleaned dataframe
        """
        df = pd.read_csv(path)
        df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y', errors='coerce')
        df['cost_price'] = df['cost_price'].fillna(df['cost_price'].mean())
        df['price'] = df['price'].fillna(df['price'].mean())
        df['region'] = df['region'].fillna(df['region'].mode()[0])
        df['revenue'] = df['final_price'] * df['quantity']
        df['month'] = df['date'].dt.month
        return df

    def _prepare_data(self):
        """Prepare aggregated data for charts."""
        self.monthly_sales = self.df.groupby('month')['revenue'].sum().reindex(range(1, 13), fill_value=0)
        self.top_products = self.df.groupby('product')['revenue'].sum().sort_values(ascending=False).head(10)
        self.category_sales = self.df.groupby('category')['revenue'].sum()
        self.region_sales = self.df.groupby('region')['revenue'].sum()
        self.profit_price = self.df[['price', 'profit']].dropna()

    def create_dashboard(self):
        """
        Create the animated dashboard with 5 charts in card style.

        Returns:
            tuple: (figure, animation) objects
        """
        # Create figure with clean card layout
        fig = plt.figure(figsize=(20, 13), facecolor='#ffffff')
        fig.suptitle('Sales Analysis Dashboard',
                    fontsize=28, fontweight='bold', color='#2c3e50', y=0.99,
                    bbox=dict(facecolor='white', edgecolor='#d0d0d0', boxstyle='round,pad=0.4', alpha=0.9))

        # Define grid with custom spacing for card-style layout
        gs = fig.add_gridspec(2, 3, hspace=0.32, wspace=0.28,
                             top=0.88, bottom=0.08, left=0.06, right=0.96)

        # Chart 1: Monthly Revenue (Line Chart) - top left
        ax1 = fig.add_subplot(gs[0, 0])
        self.line, = ax1.plot([], [], marker='o', color='#3498db',
                             linewidth=3, markersize=7, markerfacecolor='white',
                             markeredgewidth=2.5, markeredgecolor='#3498db')
        ax1.set_xlim(1, 12)
        ax1.set_ylim(0, self.monthly_sales.max() * 1.1)
        ax1.set_title('Monthly Revenue Trend', fontweight='bold', color='#2c3e50', pad=20, fontsize=15)
        ax1.set_xlabel('Month', fontsize=12)
        ax1.set_ylabel('Revenue ($)', fontsize=12)
        ax1.grid(True, alpha=0.2, linestyle='--', linewidth=0.5)
        ax1.set_facecolor('#fafafa')
        ax1.set_xticks(range(1, 13))
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.spines['left'].set_color('#e0e0e0')
        ax1.spines['bottom'].set_color('#e0e0e0')

        # Chart 2: Top Products (Bar Chart) - top center (larger)
        ax2 = fig.add_subplot(gs[0, 1])
        ax2.set_position(ax2.get_position().translated(0, -0.015))
        ax2.set_title('Top 10 Products by Revenue', fontweight='bold', color='#2c3e50', pad=20, fontsize=15)
        ax2.set_xlabel('Product', fontsize=12)
        ax2.set_ylabel('Revenue ($)', fontsize=12)
        ax2.set_facecolor('#fafafa')
        ax2.tick_params(axis='x', rotation=45)
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.spines['left'].set_color('#e0e0e0')
        ax2.spines['bottom'].set_color('#e0e0e0')

        # Chart 3: Category Distribution (Pie Chart) - top right
        ax3 = fig.add_subplot(gs[0, 2])
        ax3.set_title('Revenue by Category', fontweight='bold', color='#2c3e50', pad=20, fontsize=15)
        ax3.set_facecolor('#fafafa')

        # Chart 4: Price vs Profit (Scatter Plot) - bottom left
        ax4 = fig.add_subplot(gs[1, 0])
        self.scatter = ax4.scatter([], [], c='#e74c3c', alpha=0.6,
                                  edgecolors='white', linewidth=0.8, s=70)
        price_min, price_max = self.profit_price['price'].min(), self.profit_price['price'].max()
        profit_min, profit_max = self.profit_price['profit'].min(), self.profit_price['profit'].max()
        margin = 0.05
        ax4.set_xlim(price_min * (1-margin), price_max * (1+margin))
        ax4.set_ylim(profit_min * (1-margin), profit_max * (1+margin))
        ax4.set_title('Price vs Profit Analysis', fontweight='bold', color='#2c3e50', pad=20, fontsize=15)
        ax4.set_xlabel('Price ($)', fontsize=12)
        ax4.set_ylabel('Profit ($)', fontsize=12)
        ax4.grid(True, alpha=0.2, linestyle='--', linewidth=0.5)
        ax4.set_facecolor('#fafafa')
        ax4.spines['top'].set_visible(False)
        ax4.spines['right'].set_visible(False)
        ax4.spines['left'].set_color('#e0e0e0')
        ax4.spines['bottom'].set_color('#e0e0e0')

        # Chart 5: Revenue by Region (Bar Chart) - bottom right
        ax5 = fig.add_subplot(gs[1, 2])
        ax5.set_title('Revenue by Region', fontweight='bold', color='#2c3e50', pad=20, fontsize=15)
        ax5.set_xlabel('Region', fontsize=12)
        ax5.set_ylabel('Revenue ($)', fontsize=12)
        ax5.set_facecolor('#fafafa')
        ax5.spines['top'].set_visible(False)
        ax5.spines['right'].set_visible(False)
        ax5.spines['left'].set_color('#e0e0e0')
        ax5.spines['bottom'].set_color('#e0e0e0')

        # Colors for charts
        self.pie_colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6',
                          '#1abc9c', '#34495e', '#e67e22']
        self.bar_colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6',
                          '#1abc9c', '#34495e', '#e67e22', '#95a5a6', '#f1c40f']

        # Animation parameters
        self.total_frames = 120

        # Store axes references
        self.axes = [ax1, ax2, ax3, ax4, ax5]
        self.fig = fig

        # Add card styling with rounded corners and shadows
        self._add_card_backgrounds(fig, [ax1, ax2, ax3, ax4, ax5])

        # Initialize dashboard content before animation begins
        self._init_dashboard()

        # Create animation
        anim = animation.FuncAnimation(fig, self._update_frame,
                                     init_func=self._init_dashboard,
                                     frames=self.total_frames, interval=100,
                                     repeat=False, blit=False)

        return fig, anim

    def _add_card_backgrounds(self, fig, axes):
        """
        Add card-style backgrounds with rounded corners to charts.

        Args:
            fig: Matplotlib figure object
            axes: List of axes to style
        """
        for ax in axes:
            pos = ax.get_position()
            # Draw card background behind the axes
            fancy_box = FancyBboxPatch(
                (pos.x0 - 0.008, pos.y0 - 0.008),
                pos.width + 0.016,
                pos.height + 0.016,
                boxstyle='round,pad=0.01',
                edgecolor='#d0d0d0',
                facecolor='#ffffff',
                linewidth=1.5,
                transform=fig.transFigure,
                zorder=0,
                clip_on=False
            )
            fig.patches.append(fancy_box)
            ax.set_zorder(1)

    def _init_dashboard(self):
        """
        Draw the initial dashboard state so the chart is visible immediately.

        Returns:
            list: artists that are initialized
        """
        # Initial line state
        self.line.set_data(self.monthly_sales.index[:1], self.monthly_sales.values[:1])

        # Initial scatter state
        if not self.profit_price.empty:
            initial_offset = np.column_stack((
                self.profit_price['price'].iloc[:1].to_numpy(),
                self.profit_price['profit'].iloc[:1].to_numpy()
            ))
            self.scatter.set_offsets(initial_offset)

        # Initial bar and pie content
        self.axes[1].clear()
        self.top_products.iloc[:1].plot(
            kind='bar',
            color=self.bar_colors[:1],
            ax=self.axes[1],
            edgecolor='white',
            linewidth=0.5
        )
        self.axes[1].set_title('Top 10 Products by Revenue', fontweight='bold', color='#2c3e50', fontsize=14, pad=16)
        self.axes[1].set_xlabel('Product', fontsize=11)
        self.axes[1].set_ylabel('Revenue ($)', fontsize=11)
        self.axes[1].tick_params(axis='x', rotation=45)
        self.axes[1].set_facecolor('white')
        self.axes[1].spines['top'].set_visible(False)
        self.axes[1].spines['right'].set_visible(False)

        self.axes[2].clear()
        wedges, texts, autotexts = self.axes[2].pie(
            self.category_sales.values[:1],
            labels=self.category_sales.index[:1],
            autopct='%1.1f%%',
            colors=self.pie_colors[:1],
            startangle=140,
            wedgeprops={'edgecolor': 'white', 'linewidth': 2}
        )
        self.axes[2].set_title('Revenue by Category', fontweight='bold', color='#2c3e50', fontsize=14, pad=16)
        self.axes[2].set_facecolor('white')
        plt.setp(autotexts, size=9, weight="bold", color="white")
        plt.setp(texts, size=10)

        self.axes[4].clear()
        self.region_sales.iloc[:1].plot(
            kind='bar',
            color=self.bar_colors[:1],
            ax=self.axes[4],
            edgecolor='white',
            linewidth=0.5
        )
        self.axes[4].set_title('Revenue by Region', fontweight='bold', color='#2c3e50', fontsize=14, pad=16)
        self.axes[4].set_xlabel('Region', fontsize=11)
        self.axes[4].set_ylabel('Revenue ($)', fontsize=11)
        self.axes[4].set_facecolor('white')
        self.axes[4].spines['top'].set_visible(False)
        self.axes[4].spines['right'].set_visible(False)

        return [self.line, self.scatter]


    def _update_frame(self, frame):
        """
        Update function for animation.

        Args:
            frame (int): Current frame number

        Returns:
            list: Artists to update
        """
        progress = (frame + 1) / self.total_frames

        # Update Line Chart
        months = max(1, min(len(self.monthly_sales), int(progress * len(self.monthly_sales))))
        self.line.set_data(self.monthly_sales.index[:months], self.monthly_sales.values[:months])

        # Update Bar Chart (Top Products)
        bar_count = max(1, min(len(self.top_products), int(progress * len(self.top_products))))
        self.axes[1].clear()
        self.top_products.iloc[:bar_count].plot(
            kind='bar',
            color=self.bar_colors[:bar_count],
            ax=self.axes[1],
            edgecolor='white',
            linewidth=0.5
        )
        self.axes[1].set_title('Top 10 Products by Revenue', fontweight='bold', color='#2c3e50', fontsize=14, pad=16)
        self.axes[1].set_xlabel('Product', fontsize=11)
        self.axes[1].set_ylabel('Revenue ($)', fontsize=11)
        self.axes[1].tick_params(axis='x', rotation=45)
        self.axes[1].set_facecolor('white')
        self.axes[1].spines['top'].set_visible(False)
        self.axes[1].spines['right'].set_visible(False)

        # Update Pie Chart
        pie_count = max(1, min(len(self.category_sales), int(progress * len(self.category_sales))))
        self.axes[2].clear()
        wedges, texts, autotexts = self.axes[2].pie(
            self.category_sales.values[:pie_count],
            labels=self.category_sales.index[:pie_count],
            autopct='%1.1f%%',
            colors=self.pie_colors[:pie_count],
            startangle=140,
            wedgeprops={'edgecolor': 'white', 'linewidth': 2}
        )
        self.axes[2].set_title('Revenue by Category', fontweight='bold', color='#2c3e50', fontsize=14, pad=16)
        self.axes[2].set_facecolor('white')
        plt.setp(autotexts, size=9, weight="bold", color="white")
        plt.setp(texts, size=10)

        # Update Scatter Plot
        scatter_count = max(1, min(len(self.profit_price), int(progress * len(self.profit_price))))
        offsets = np.column_stack((
            self.profit_price['price'].iloc[:scatter_count].to_numpy(),
            self.profit_price['profit'].iloc[:scatter_count].to_numpy()
        ))
        self.scatter.set_offsets(offsets)

        # Update Region Bar Chart
        region_count = max(1, min(len(self.region_sales), int(progress * len(self.region_sales))))
        self.axes[4].clear()
        self.region_sales.iloc[:region_count].plot(
            kind='bar',
            color=self.bar_colors[:region_count],
            ax=self.axes[4],
            edgecolor='white',
            linewidth=0.5
        )
        self.axes[4].set_title('Revenue by Region', fontweight='bold', color='#2c3e50', fontsize=14, pad=16)
        self.axes[4].set_xlabel('Region', fontsize=11)
        self.axes[4].set_ylabel('Revenue ($)', fontsize=11)
        self.axes[4].set_facecolor('white')
        self.axes[4].spines['top'].set_visible(False)
        self.axes[4].spines['right'].set_visible(False)

        return [self.line, self.scatter]

    def save_dashboard(self, fig, anim, output_type='gif'):
        """
        Save the dashboard as image or animation.

        Args:
            fig: Matplotlib figure
            anim: Animation object
            output_type (str): 'gif' or 'png'
        """
        if output_type == 'gif':
            try:
                anim.save("sales_dashboard_animation.gif", writer="pillow", fps=10, dpi=150)
                print("✅ Saved animated dashboard to 'sales_dashboard_animation.gif'")
            except Exception as e:
                print(f"❌ Could not save animation: {e}")
                self._save_static(fig)
        else:
            self._save_static(fig)

    def _save_static(self, fig):
        """Save static version of dashboard."""
        fig.savefig("sales_dashboard_static.png", dpi=300, bbox_inches='tight',
                   facecolor='#f8f9fa', edgecolor='none')
        print("✅ Saved static dashboard to 'sales_dashboard_static.png'")


def main():
    """
    Main function to run the sales dashboard.
    """
    print("🚀 Creating Professional Sales Dashboard...")

    # Create dashboard
    dashboard = SalesDashboard("Update.dataset.csv")
    fig, anim = dashboard.create_dashboard()

    # Save dashboard
    dashboard.save_dashboard(fig, anim, output_type='gif')

    # Display if possible
    try:
        plt.show()
    except:
        print("ℹ️  Display not available, dashboard saved to file.")

    plt.close(fig)
    print("🎉 Dashboard creation complete!")


if __name__ == "__main__":
    main()
