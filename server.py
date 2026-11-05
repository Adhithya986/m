import http.server
import socketserver
import webbrowser
import os
import urllib.parse
import ctypes
from ctypes import wintypes

PORT = 8888
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# ----------------- NATIVE WINDOWS CLIPBOARD (Zero-interaction copy) ----------------- #
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

kernel32.GlobalAlloc.argtypes = [wintypes.UINT, ctypes.c_size_t]
kernel32.GlobalAlloc.restype = wintypes.HGLOBAL

kernel32.GlobalLock.argtypes = [wintypes.HGLOBAL]
kernel32.GlobalLock.restype = wintypes.LPVOID

kernel32.GlobalUnlock.argtypes = [wintypes.HGLOBAL]
kernel32.GlobalUnlock.restype = wintypes.BOOL

user32.OpenClipboard.argtypes = [wintypes.HWND]
user32.OpenClipboard.restype = wintypes.BOOL

user32.EmptyClipboard.argtypes = []
user32.EmptyClipboard.restype = wintypes.BOOL

user32.SetClipboardData.argtypes = [wintypes.UINT, wintypes.HANDLE]
user32.SetClipboardData.restype = wintypes.HANDLE

user32.CloseClipboard.argtypes = []
user32.CloseClipboard.restype = wintypes.BOOL

CF_UNICODETEXT = 13
GMEM_MOVEABLE = 0x0002

def set_windows_clipboard(text: str) -> bool:
    """Sets text directly into the Windows OS clipboard (no browser user-gesture needed)."""
    try:
        data = (text + '\0').encode('utf-16le')
        h_mem = kernel32.GlobalAlloc(GMEM_MOVEABLE, len(data))
        if not h_mem:
            return False
        ptr = kernel32.GlobalLock(h_mem)
        if not ptr:
            return False
        ctypes.memmove(ptr, data, len(data))
        kernel32.GlobalUnlock(h_mem)

        if not user32.OpenClipboard(None):
            return False
        user32.EmptyClipboard()
        user32.SetClipboardData(CF_UNICODETEXT, h_mem)
        user32.CloseClipboard()
        return True
    except Exception as e:
        print(f"Clipboard error: {e}")
        return False

# ----------------- PROGRAM CODES FROM python_lab_programs.pdf ----------------- #
PROGRAMS = {
    1: """#4. Write a Python Program to Find the Real & Complex Eigen Values and Eigen Vectors of a
#User-defined Matrix with Visualization
import numpy as np
import cmath
import matplotlib.pyplot as plt

n = int(input("Enter the order of the matrix"))
A = []
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)
print("A=", A)
e, V = np.linalg.eig(A)
print("Eigen values of A: ", e)
print("Eigen vector of A(column-wise): ", V)
for i in range(n):
    v = V[:, i]
    Av = A @ v
    print("Av=", Av)
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, label="x", color='blue')
    plt.quiver(0, 0, -v[0], -v[1], angles='xy', scale_units='xy', scale=1, label="x", color='blue')
    plt.quiver(0, 0, Av[0], Av[1], angles='xy', scale_units='xy', scale=1, label="Ax", color='red')
    plt.quiver(0, 0, -Av[0], -Av[1], angles='xy', scale_units='xy', scale=1, label="Ax", color='red')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.title("Visualization of Eigenvectors of the Given Matrix")
plt.grid(True)
plt.legend()
plt.show()""",

    2: """#2. Write a Python Program to find the root of a User-defined Transcendental Equation with
#Visualization using Newton Raphson Method
import numpy as np
import matplotlib.pyplot as plt

x = float(input("Enter the initial guess x0: "))
function = input("Enter the function (use x as the variable): ")
derivative = input("Enter the derivative of the function: ")
n = abs(int(input("Enter the number of iterations: ")))

def f(x):
    return eval(function)

def df(x):
    return eval(derivative)

print("-" * 120)
print(f"{'S.NO':<6}|{'x':<16}|{'f(x)':<20}|{'f\\'(x)':<20}|{'x_new':<16}")
print("-" * 120)

for i in range(n):
    fx = f(x)
    dfx = df(x)
    if dfx == 0:
        print("Derivative is zero. Newton-Raphson method fails.")
        break
    x_new = x - fx / dfx
    print(f"{i+1:<6}|{x:<16.6f}|{fx:<20.6f}|{dfx:<20.6f}|{x_new:<16.6f}")
    print("-" * 120)
    x = x_new

print("Approximate root =", x)

# Plot
x = np.linspace(1, 3, 400)
y = f(x)
plt.plot(x, y, label=r"$f(x)= x*\\log(x) - 1.2$")
plt.axhline(0, color="black")
plt.grid(True)
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function graph")
plt.show()""",

    3: """#1. Write a Python program to solve the following natural growth problem: The number N of
#bacteria in a culture grows at a rate proportional to N. The value of N was initially 100
#and increased to 332 in one hour. What was the value of N after 1/2 hour?
import numpy as np
import matplotlib.pyplot as plt

# User-defined function to calculate growth/decay constant
def find_constant(P0, t1, P1):
    k = (1 / t1) * np.log(P1 / P0)
    return k

# User-defined function to find quantity
def find_quantity(P0, k, t):
    P = P0 * np.exp(k * t)
    return P

# User-defined function to find time
def find_time(P0, k, P):
    t = (1 / k) * np.log(P / P0)
    return t

# Input data
P0 = float(input("Enter initial quantity P0 = "))
t1 = float(input("Enter known time t1 = "))
P1 = float(input("Enter quantity at t1 = "))

# Calculate constant
k = find_constant(P0, t1, P1)
print("Growth/Decay constant k =", k)

# Check growth or decay
if k > 0:
    print("The quantity represents Natural Growth.")
elif k < 0:
    print("The quantity represents Natural Decay.")
else:
    print("The quantity remains constant.")

# Find P2 or t2
print("For P2 and t2:")
print("1. Find P2 for a given t2")
print("2. Find t2 for a given P2")
print("3. Skip P2 and t2")
choice = int(input("Enter your choice = "))
P2 = None
t2 = None
if choice == 1:
    t2 = float(input("Enter time t2 = "))
    P2 = find_quantity(P0, k, t2)
    print("Time t2 =", t2)
    print("Quantity P2 =", P2)
elif choice == 2:
    P2 = float(input("Enter required quantity P2 = "))
    t2 = find_time(P0, k, P2)
    print("Quantity P2 =", P2)
    print("Time t2 =", t2)
elif choice == 3:
    print("P2 and t2 calculation skipped.")
else:
    print("Invalid choice")

# Visualization
if choice in (1, 2):
    t = np.linspace(0, max(t1, t2) + 1, 100)
    P = P0 * np.exp(k * t)
    plt.plot(t, P)
    plt.scatter([t1, t2], [P1, P2])
    plt.xlabel("Time")
    plt.ylabel("Quantity")
    plt.title("Law of Natural Growth and Decay")
    plt.grid(True)
    plt.show()""",

    4: """#4. (D^3 - 6D^2 + 11D - 6)y = 0 with Visualization
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')
y = Function('y')
ode = Eq(diff(y(x), x, 3) - 6*diff(y(x), x, 2) + 11*diff(y(x), x) - 6*y(x), 0)
sol = dsolve(ode)
print("Solution of the differential equation:")
print(sol)

# Visualization for C1 = C2 = C3 = 1
y1 = (1 + exp(x) + exp(2*x))*exp(x)
f = lambdify(x, y1, 'numpy')
X = np.linspace(0, 5, 200)
Y = f(X)
plt.plot(X, Y, label='C1 = C2 = C3 = 1')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Visualization of CF')
plt.grid(True)
plt.legend()
plt.show()"""
}

class JupyterMockHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        # Determine which program is requested (default is Program 1)
        p_num = 1
        if 'p' in params:
            try:
                val = int(params['p'][0])
                if val in PROGRAMS:
                    p_num = val
            except ValueError:
                pass

        # API endpoint for background clipboard sync
        if parsed.path == '/api/copy':
            code = PROGRAMS.get(p_num, PROGRAMS[1])
            success = set_windows_clipboard(code)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(b'{"status": "copied", "program": %d}' % p_num)
            print(f"[✓ Copied to Windows Clipboard: Program {p_num}]")
            return

        # Main page visit: IMMEDIATELY copy code to Windows clipboard upon entering the page!
        if parsed.path in ('/', '/index.html') or '/notebooks/' in parsed.path or parsed.path.endswith('.ipynb'):
            code = PROGRAMS.get(p_num, PROGRAMS[1])
            set_windows_clipboard(code)
            print(f"[✓ Instant Copy on Enter: Program {p_num} set to Windows Clipboard!]")
            self.path = '/index.html'

        return super().do_GET()

def run():
    # Allow port reuse immediately
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), JupyterMockHandler) as httpd:
        url = f"http://localhost:{PORT}/notebooks/Python_Computational_Lab_Manual.ipynb"
        print("=" * 65)
        print(" Jupyter Notebook Mock Server Started")
        print(f" URL: {url}")
        print(" Features:")
        print("  - Instant copy to Windows clipboard when you enter/navigate to the URL")
        print("  - Use ?p=1, ?p=2, ?p=3, ?p=4 in the URL to select which program auto-copies")
        print("  - Program 1: Eigenvalues & Eigenvectors with Visualization")
        print("  - Program 2: Newton-Raphson Method Root Finding")
        print("  - Program 3: Natural Growth & Decay Law")
        print("  - Program 4: Higher Order Differential Equation (CF Plot)")
        print("=" * 65)
        
        # Pre-load program 1 into clipboard before opening browser
        set_windows_clipboard(PROGRAMS[1])
        print("[✓ Initialized Windows Clipboard with Program 1]")

        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    run()
