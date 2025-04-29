# 🚄 Railway Network Optimization using Kruskal's Algorithm

This project is a Streamlit-based interactive visualization tool to demonstrate **Minimum Spanning Tree (MST)** construction using **Kruskal’s Algorithm**. It is designed to help you optimize a railway network by minimizing the total cost to connect all cities.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue" />
  <img src="https://img.shields.io/badge/Streamlit-%E2%9D%A4-red" />
  <img src="https://img.shields.io/badge/Algorithm-Kruskal-green" />
  <img src="https://img.shields.io/badge/Visualization-PyVis-orange" />
</p>

---

## 📌 Features

- 🏙️ Default graph of 6 cities and predefined routes
- 🛠️ Option to create custom railway networks interactively
- 📉 Uses **Kruskal's Algorithm** to find the Minimum Spanning Tree (MST)
- 🌐 Interactive network visualization using **PyVis**
- 💰 Displays total cost of the optimized railway network
- 📈 Shows connection details in a clean table

---

## 🚀 Getting Started

### 🔧 Installation

Make sure you have Python 3.9 or higher.

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/railway-kruskal-network.git
cd railway-kruskal-network
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install streamlit networkx pyvis pandas
```

---

### ▶️ Run the App

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 🧠 How It Works

- The app offers two modes:
  - ✅ **Default mode**: Uses a predefined complex graph of 6 cities and 9 connections.
  - ✍️ **Custom mode**: Lets the user input number of cities and define edges and costs dynamically.

- The graph is visualized using `PyVis`, and MST is calculated using `Kruskal's Algorithm`, implemented with a Union-Find data structure.

---

## 🖼️ Screenshots

| Default Mode | Custom Input Mode |
|--------------|------------------|
| ![default](assets/default_view.png) | ![custom](assets/custom_view.png) |

---

## 📂 Project Structure

```
.
├── app.py              # Main Streamlit application
├── railway_network.html # Generated interactive graph (auto-created)
├── requirements.txt    # Required Python packages
└── README.md           # This file
```

---

## 📚 References

- [Kruskal's Algorithm - GeeksforGeeks](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [PyVis for NetworkX](https://pyvis.readthedocs.io/en/latest/)

---

## 🙌 Acknowledgments

Built with ❤️ using Python, Streamlit, and PyVis.

---

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---