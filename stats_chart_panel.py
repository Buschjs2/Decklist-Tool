from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
import pyqtgraph as pg

class StatsChartPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setMaximumHeight(300)

        # CMC Histogram
        self.layout.addWidget(QLabel("<b>Mana Curve (CMC)</b>"))
        self.cmc_plot = pg.PlotWidget(title="Mana Curve")
        self.cmc_plot.setLabel('left', 'Card Count')
        self.cmc_plot.setLabel('bottom', 'CMC')
        self.cmc_plot.showGrid(x=True, y=True)
        self.layout.addWidget(self.cmc_plot)

        # Color Identity Bar Chart
        self.layout.addWidget(QLabel("<b>Color Identity</b>"))
        self.color_plot = pg.PlotWidget(title="Color Identity")
        self.color_plot.setLabel('left', 'Card Count')
        self.color_plot.setLabel('bottom', 'Color Identity')
        self.color_plot.showGrid(x=True, y=True)
        self.layout.addWidget(self.color_plot)

    def update_charts(self, deck, metadata):
        self.cmc_plot.clear()
        self.color_plot.clear()

        color_counts = {}
        cmc_bins = [0] * 12  # 0–10, 11+

        for name, qty in deck:
            info = metadata.get(name, {})
            type_line = info.get("type_line", "").lower()

            # Exclude lands
            if "land" in type_line:
                continue

            cmc = info.get("cmc", 0)
            if not isinstance(cmc, (int, float)):
                cmc = 0
            cmc_index = min(int(cmc), 11)
            cmc_bins[cmc_index] += qty

            ci = info.get("color_identity", [])
            label = "Colorless" if not ci else " / ".join(sorted(ci))
            color_counts[label] = color_counts.get(label, 0) + qty

        # Update CMC chart
        x = list(range(len(cmc_bins)))
        bar_item = pg.BarGraphItem(x=x, height=cmc_bins, width=0.6, brush="#4e9eea")
        self.cmc_plot.addItem(bar_item)
        self.cmc_plot.getPlotItem().getAxis('bottom').setTicks([[(i, str(i) if i < 11 else "11+") for i in x]])

        # Update Color Identity chart
        labels = list(color_counts.keys())
        heights = list(color_counts.values())
        x_ticks = list(enumerate(labels))
        bar_item2 = pg.BarGraphItem(x=list(range(len(labels))), height=heights, width=0.6, brush="#3bae62")
        self.color_plot.addItem(bar_item2)
        self.color_plot.getPlotItem().getAxis('bottom').setTicks([x_ticks])
