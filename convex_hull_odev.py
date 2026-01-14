import random
import time
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# =====================================================
# ORIENTATION
# =====================================================
def orientation(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


# =====================================================
# GRAHAM SCAN — O(N log N)
# =====================================================
def graham_scan(points):
    points = sorted(points)
    if len(points) <= 1:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


# =====================================================
# BRUTE FORCE — O(N³)
# =====================================================
def brute_force_hull(points):
    hull = set()
    n = len(points)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            p, q = points[i], points[j]
            left = right = False

            for r in points:
                val = orientation(p, q, r)
                if val > 0:
                    left = True
                elif val < 0:
                    right = True

            if not (left and right):
                hull.add(p)
                hull.add(q)

    return list(hull)


# =====================================================
# GUI
# =====================================================
class ConvexHullGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Convex Hull Karşılaştırması")
        self.root.geometry("1200x850")
        self.root.configure(bg="#0f172a")

        self.points = []
        self.setup_style()
        self.create_widgets()
        self.generate_and_draw_points()

    # -------------------------------------------------
    # STYLE
    # -------------------------------------------------
    def setup_style(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Card.TFrame", background="#020617")
        style.configure("TLabel", background="#020617", foreground="#e5e7eb")
        style.configure("Title.TLabel", font=("Segoe UI", 11, "bold"))
        style.configure("Accent.TButton", background="#2563eb", foreground="white")
        style.map("Accent.TButton", background=[("active", "#1d4ed8")])

    # -------------------------------------------------
    # WIDGETS
    # -------------------------------------------------
    def create_widgets(self):
        # ---- CONTROL PANEL ----
        control = ttk.Frame(self.root, style="Card.TFrame", padding=12)
        control.pack(fill=tk.X, padx=15, pady=10)

        ttk.Label(control, text="N (Nokta Sayısı):", style="Title.TLabel").pack(side=tk.LEFT)
        self.n_entry = ttk.Entry(control, width=8)
        self.n_entry.insert(0, "100")
        self.n_entry.pack(side=tk.LEFT, padx=5)

        ttk.Button(control, text="Yeni Noktalar", command=self.generate_and_draw_points)\
            .pack(side=tk.LEFT, padx=5)

        ttk.Button(control, text="Graham Scan", command=self.draw_graham)\
            .pack(side=tk.LEFT, padx=5)

        ttk.Button(control, text="Brute Force", command=self.draw_brute)\
            .pack(side=tk.LEFT, padx=5)

        ttk.Button(control, text="Performans", command=self.performance_test)\
            .pack(side=tk.LEFT, padx=5)

        # ---- GRAPH ----
        graph_frame = ttk.Frame(self.root, style="Card.TFrame", padding=10)
        graph_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        self.fig = plt.Figure(figsize=(8, 6), facecolor="#121E55")
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor("#071349")

        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # ---- TIME LABEL ----
        self.time_label = ttk.Label(
            self.root,
            text="Algoritma Çalışma Süresi: -",
            font=("Segoe UI", 12, "bold"),
            foreground="#38bdf8",
            background="#0f172a"
        )
        self.time_label.pack(pady=10)

    # -------------------------------------------------
    # POINTS
    # -------------------------------------------------
    def generate_and_draw_points(self):
        self.ax.clear()

        N = int(self.n_entry.get())
        self.points = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(N)]

        x, y = zip(*self.points)
        self.ax.scatter(x, y, color="#60a5fa", label="Noktalar")

        self.ax.set_title(f"Rastgele Noktalar (N={N})", color="white")
        self.ax.tick_params(colors="white")
        self.ax.legend()
        self.ax.grid(True, alpha=0.3)

        self.canvas.draw()
        self.time_label.config(text="Algoritma Çalışma Süresi: -")

    # -------------------------------------------------
    # GRAHAM
    # -------------------------------------------------
    def draw_graham(self):
        self.ax.clear()
        x, y = zip(*self.points)
        self.ax.scatter(x, y, color="gray")

        start = time.perf_counter()
        hull = graham_scan(self.points)
        elapsed = (time.perf_counter() - start) * 1000

        hx, hy = zip(*(hull + [hull[0]]))

        self.ax.plot(hx, hy, color="#22c55e", linewidth=2, label="Graham Scan")

        self.ax.set_title("Convex Hull – Graham Scan", color="white")
        self.ax.legend()
        self.ax.grid(True, alpha=0.3)
        self.canvas.draw()

        self.time_label.config(text=f"Graham Scan Süresi: {elapsed:.3f} ms")

    # -------------------------------------------------
    # BRUTE FORCE
    # -------------------------------------------------
    def draw_brute(self):
        self.ax.clear()
        x, y = zip(*self.points)
        self.ax.scatter(x, y, color="gray")

        start = time.perf_counter()
        hull = graham_scan(brute_force_hull(self.points))
        elapsed = (time.perf_counter() - start) * 1000

        hx, hy = zip(*(hull + [hull[0]]))
        self.ax.plot(hx, hy, color="#ef4444", linewidth=2, label="Brute Force")

        self.ax.set_title("Convex Hull – Brute Force", color="white")
        self.ax.legend()
        self.ax.grid(True, alpha=0.3)
        self.canvas.draw()

        self.time_label.config(text=f"Brute Force Süresi: {elapsed:.3f} ms")

    # -------------------------------------------------
    # PERFORMANCE
    # -------------------------------------------------
    def performance_test(self):
        Ns = [0, 100, 200, 300, 400, 500]
        bf, gs = [], []

        for n in Ns:
            pts = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(n)]

            t0 = time.perf_counter()
            brute_force_hull(pts)
            bf.append(time.perf_counter() - t0)

            t0 = time.perf_counter()
            graham_scan(pts)
            gs.append(time.perf_counter() - t0)

        plt.figure(figsize=(9, 4))
        plt.plot(Ns, bf, "o-", label="Brute Force")
        plt.plot(Ns, gs, "s-", label="Graham Scan")
        plt.xticks([0, 100, 200, 300, 400, 500])
        plt.xlabel("N")
        plt.ylabel("Süre (s)")
        plt.title("Performans Karşılaştırması")
        plt.grid(True)
        plt.legend()
        plt.show()


# =====================================================
# MAIN
# =====================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = ConvexHullGUI(root)
    root.mainloop()
