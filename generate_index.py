import base64
import json
import pygments
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# Read extracted images as base64
images_b64 = {}
for i in [1, 2, 3, 4]:
    with open(f"c:/Users/Akshaya/Downloads/scam2/fig_{i}.png", "rb") as f:
        images_b64[i] = base64.b64encode(f.read()).decode("utf-8")

# Program pure raw python codes from python_lab_programs.pdf
p1_code = """#4. Write a Python Program to Find the Real & Complex Eigen Values and Eigen Vectors of a
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
plt.show()"""

p2_code = """#2. Write a Python Program to find the root of a User-defined Transcendental Equation with
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
plt.show()"""

p3_code = """#1. Write a Python program to solve the following natural growth problem: The number N of
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
    plt.show()"""

p4_code = """#4. (D^3 - 6D^2 + 11D - 6)y = 0 with Visualization
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

# Console execution outputs matching PDF exactly
out1_text = """Enter the order of the matrix2
4 2
1 3
A= [[4.0, 2.0], [1.0, 3.0]]
Eigen values of A:  [5. 2.]
Eigen vector of A(column-wise):  [[ 0.89442719 -0.70710678]
 [ 0.4472136   0.70710678]]
Av= [4.47213595 2.23606798]
Av= [-1.41421356  1.41421356]
<Figure size 640x480 with 1 Axes>"""

out2_text = """Enter the initial guess x0: 1.5
Enter the function (use x as the variable): x*np.log(x)-1.2
Enter the derivative of the function: 1+np.log(x)
Enter the number of iterations: 5
------------------------------------------------------------------------------------------------------------------------
S.NO  |x               |f(x)                |f'(x)               |x_new           
------------------------------------------------------------------------------------------------------------------------
1     |1.500000        |-0.591982           |1.405465            |1.921072        
------------------------------------------------------------------------------------------------------------------------
2     |1.921072        |0.054236            |1.652883            |1.888259        
------------------------------------------------------------------------------------------------------------------------
3     |1.888259        |0.000282            |1.635655            |1.888087        
------------------------------------------------------------------------------------------------------------------------
4     |1.888087        |0.000000            |1.635564            |1.888087        
------------------------------------------------------------------------------------------------------------------------
5     |1.888087        |-0.000000           |1.635564            |1.888087        
------------------------------------------------------------------------------------------------------------------------
Approximate root = 1.8880867530283436
<Figure size 640x480 with 1 Axes>"""

out3_text = """Enter initial quantity P0 = 100
Enter known time t1 = 1
Enter quantity at t1 = 332
Growth/Decay constant k = 1.199964782418397
The quantity represents Natural Growth.
For P2 and t2:
1. Find P2 for a given t2
2. Find t2 for a given P2
3. Skip P2 and t2
Enter your choice = 1
Enter time t2 = 1.5
Time t2 = 1.5
Quantity P2 = 604.9127096551812
<Figure size 640x480 with 1 Axes>"""

out4_text = """Solution of the differential equation:
Eq(y(x), (C1 + C2*exp(x) + C3*exp(2*x))*exp(x))
<Figure size 640x480 with 1 Axes>"""

lexer = PythonLexer()
formatter = HtmlFormatter(nowrap=True)

html1 = pygments.highlight(p1_code, lexer, formatter)
html2 = pygments.highlight(p2_code, lexer, formatter)
html3 = pygments.highlight(p3_code, lexer, formatter)
html4 = pygments.highlight(p4_code, lexer, formatter)

pygments_css = HtmlFormatter().get_style_defs('.highlight')

raw_json = json.dumps({
    1: p1_code,
    2: p2_code,
    3: p3_code,
    4: p4_code
})

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Python_Computational_Lab_Manual - Jupyter Notebook</title>
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 448 512'%3E%3Cpath fill='%23F37626' d='M224 0C100.3 0 0 100.3 0 224s100.3 224 224 224 224-100.3 224-224S347.7 0 224 0zm0 405.3c-100 0-181.3-81.3-181.3-181.3S124 42.7 224 42.7 405.3 124 405.3 224 324 405.3 224 405.3z'/%3E%3C/svg%3E">
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      font-size: 14px;
      line-height: 1.42857143;
      color: #333;
      background-color: #eee;
    }}

    /* Jupyter Header */
    #header {{
      background-color: #fff;
      border-bottom: 1px solid #e7e7e7;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }}
    .header-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 6px 16px;
      border-bottom: 1px solid #f0f0f0;
    }}
    .brand-section {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .jupyter-logo {{
      width: 26px;
      height: 28px;
    }}
    .title-area {{
      display: flex;
      flex-direction: column;
    }}
    .doc-title {{
      font-size: 16px;
      font-weight: 600;
      color: #333;
      cursor: pointer;
    }}
    .doc-title:hover {{
      text-decoration: underline;
    }}
    .checkpoint-status {{
      font-size: 11px;
      color: #777;
    }}
    .header-right {{
      display: flex;
      align-items: center;
      gap: 15px;
    }}
    .kernel-status {{
      display: flex;
      align-items: center;
      gap: 7px;
      font-size: 12px;
      color: #555;
      background: #f8f9fa;
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
    }}
    .kernel-indicator {{
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background-color: #28a745;
      display: inline-block;
      box-shadow: 0 0 0 2px rgba(40,167,69,0.2);
    }}
    .copy-banner {{
      font-size: 11px;
      padding: 3px 8px;
      border-radius: 3px;
      font-weight: 500;
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .copy-banner.copied {{
      background-color: #d4edda;
      color: #155724;
      border: 1px solid #c3e6cb;
    }}

    /* Menu Bar */
    .menubar {{
      display: flex;
      padding: 2px 16px;
      background-color: #fff;
      font-size: 13px;
      border-bottom: 1px solid #e7e7e7;
    }}
    .menu-item {{
      padding: 4px 8px;
      color: #222;
      cursor: pointer;
      border-radius: 3px;
      user-select: none;
    }}
    .menu-item:hover {{
      background-color: #e6e6e6;
    }}

    /* Toolbar */
    .toolbar {{
      display: flex;
      align-items: center;
      gap: 5px;
      padding: 4px 16px;
      background-color: #f7f7f7;
      border-bottom: 1px solid #ddd;
    }}
    .btn-group {{
      display: inline-flex;
      border: 1px solid #ccc;
      border-radius: 3px;
      background: #fff;
    }}
    .tb-btn {{
      background: #fff;
      border: none;
      border-right: 1px solid #ccc;
      padding: 5px 9px;
      font-size: 12px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: #444;
      line-height: 1;
    }}
    .tb-btn:last-child {{
      border-right: none;
    }}
    .tb-btn:hover {{
      background: #f0f0f0;
      color: #000;
    }}
    .tb-select {{
      font-size: 12px;
      padding: 3px 7px;
      border: 1px solid #ccc;
      border-radius: 3px;
      background: #fff;
      margin-left: 6px;
    }}
    .shortcut-badge {{
      font-size: 11px;
      color: #666;
      margin-left: auto;
      display: flex;
      gap: 8px;
    }}
    .key-badge {{
      background: #e2e8f0;
      padding: 2px 7px;
      border-radius: 3px;
      font-family: monospace;
      font-size: 11px;
      cursor: pointer;
      border: 1px solid #cbd5e0;
      font-weight: 500;
    }}
    .key-badge:hover {{
      background: #cbd5e0;
      color: #000;
    }}

    /* Notebook Main Area */
    #notebook-container {{
      max-width: 1180px;
      margin: 20px auto 60px auto;
      background-color: #fff;
      box-shadow: 0 0 12px rgba(0,0,0,0.07);
      padding: 30px 35px;
      min-height: 800px;
    }}

    /* Cells */
    .cell {{
      position: relative;
      margin-bottom: 24px;
      border: 1px solid transparent;
      border-radius: 2px;
      transition: border-color 0.15s ease;
    }}
    .cell.selected {{
      border-left: 5px solid #28a745;
      padding-left: 5px;
    }}
    .cell.code-cell {{
      display: flex;
      flex-direction: column;
    }}

    /* Markdown Cell */
    .markdown-cell {{
      padding: 10px 14px;
      margin-bottom: 24px;
      border-bottom: 2px solid #eaeaea;
    }}
    .markdown-cell h1 {{
      font-size: 26px;
      margin-bottom: 8px;
      color: #2b2b2b;
      font-weight: 600;
    }}
    .markdown-cell p {{
      color: #666;
      font-size: 14px;
    }}

    /* Section Subheadings inside cells */
    .exp-heading {{
      font-size: 13px;
      font-weight: 600;
      color: #4a5568;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
      padding-left: 80px;
    }}

    /* Cell Input Area */
    .cell-input-row {{
      display: flex;
      align-items: flex-start;
      margin-top: 4px;
    }}
    .prompt {{
      min-width: 80px;
      padding: 8px 10px 0 0;
      font-family: "Lucida Console", Monaco, Consolas, "Courier New", monospace;
      font-size: 12.5px;
      text-align: right;
      color: #303ea0;
      user-select: none;
      font-weight: 500;
    }}
    .cell-wrapper {{
      flex: 1;
      position: relative;
    }}
    .code-container {{
      background-color: #f7f7f7;
      border: 1px solid #cfcfcf;
      border-radius: 2px;
      padding: 10px 14px;
      font-family: Consolas, Monaco, "Andale Mono", "Ubuntu Mono", monospace;
      font-size: 13px;
      line-height: 1.5;
      overflow-x: auto;
      white-space: pre;
      position: relative;
      cursor: pointer;
    }}
    .code-container:hover {{
      background-color: #fbfbfb;
      border-color: #a0aec0;
    }}
    .cell.selected .code-container {{
      background-color: #fff;
      border-color: #4299e1;
      box-shadow: 0 0 0 1px #4299e1;
    }}

    /* Quick Copy Overlay Button */
    .cell-actions {{
      position: absolute;
      top: 6px;
      right: 8px;
      display: flex;
      gap: 6px;
      opacity: 0.7;
      transition: opacity 0.15s ease;
      z-index: 5;
    }}
    .cell-wrapper:hover .cell-actions {{
      opacity: 1;
    }}
    .copy-btn {{
      background: #ffffff;
      border: 1px solid #cbd5e0;
      border-radius: 3px;
      font-size: 11px;
      padding: 3px 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      color: #4a5568;
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }}
    .copy-btn:hover {{
      background: #edf2f7;
      color: #1a202c;
    }}
    .copy-btn.copied {{
      background: #28a745;
      color: #fff;
      border-color: #28a745;
    }}

    /* Cell Output Area */
    .cell-output-row {{
      display: flex;
      align-items: flex-start;
      margin-top: 4px;
    }}
    .output-prompt {{
      min-width: 80px;
      padding: 8px 10px 0 0;
      font-family: "Lucida Console", Monaco, Consolas, "Courier New", monospace;
      font-size: 12.5px;
      text-align: right;
      color: #d42a2a;
      user-select: none;
    }}
    .output-container {{
      flex: 1;
      padding: 6px 14px 14px 14px;
      font-family: Consolas, Monaco, monospace;
      font-size: 12.5px;
      color: #222;
      overflow-x: auto;
    }}
    .output-subtext {{
      color: #333;
      line-height: 1.45;
      white-space: pre-wrap;
      margin-bottom: 12px;
    }}

    /* Plot Graph Presentation */
    .output-figure {{
      margin-top: 8px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
    }}
    .output-figure img {{
      max-width: 620px;
      width: 100%;
      height: auto;
      border: 1px solid #ddd;
      border-radius: 3px;
      background: #fff;
      box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    }}
    .figure-caption {{
      margin-top: 6px;
      font-size: 12px;
      color: #666;
      font-style: italic;
    }}

    /* Pygments Syntax Highlighting CSS */
    {pygments_css}
    .highlight .c, .highlight .c1, .highlight .cm {{ color: #408080; font-style: italic; }}
    .highlight .k, .highlight .kn, .highlight .kp {{ color: #008000; font-weight: bold; }}
    .highlight .s, .highlight .s1, .highlight .s2, .highlight .sa, .highlight .sb, .highlight .sc, .highlight .sd, .highlight .se, .highlight .sh, .highlight .si, .highlight .sx, .highlight .sr, .highlight .ss {{ color: #ba2121; }}
    .highlight .nf, .highlight .fm {{ color: #0086b3; }}
    .highlight .nb, .highlight .bp {{ color: #008000; }}
    .highlight .m, .highlight .mi, .highlight .mf, .highlight .mh, .highlight .mo, .highlight .il {{ color: #080; }}
    .highlight .o, .highlight .ow {{ color: #666666; }}
    .highlight .n, .highlight .nn, .highlight .nc {{ color: #111; }}

    /* Floating Toast Notification */
    #copy-toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #2d3748;
      color: #fff;
      padding: 10px 18px;
      border-radius: 6px;
      font-size: 13px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.25);
      display: flex;
      align-items: center;
      gap: 10px;
      opacity: 0;
      transform: translateY(12px);
      transition: opacity 0.25s ease, transform 0.25s ease;
      pointer-events: none;
      z-index: 9999;
    }}
    #copy-toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}
    #copy-toast .toast-icon {{
      color: #48bb78;
      font-size: 16px;
    }}
  </style>
</head>
<body>

  <!-- Jupyter Header -->
  <div id="header">
    <div class="header-top">
      <div class="brand-section">
        <!-- SVG Jupyter Classic Logo -->
        <svg class="jupyter-logo" viewBox="0 0 448 512" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="224" cy="256" r="160" stroke="#767676" stroke-width="38"/>
          <circle cx="90" cy="130" r="48" fill="#F37626"/>
          <circle cx="358" cy="382" r="48" fill="#F37626"/>
          <circle cx="358" cy="130" r="22" fill="#767676"/>
          <circle cx="90" cy="382" r="22" fill="#767676"/>
        </svg>
        <div class="title-area">
          <span class="doc-title" id="notebook-title">Python_Computational_Lab_Manual</span>
          <span class="checkpoint-status">Last Checkpoint: a few seconds ago (autosaved)</span>
        </div>
      </div>
      <div class="header-right">
        <div class="copy-banner copied" id="status-pill">
          <span>&#10003; Ready (Press 1-4 to switch/copy)</span>
        </div>
        <div class="kernel-status">
          <span class="kernel-indicator"></span>
          <span>Python 3 (ipykernel)</span>
        </div>
      </div>
    </div>

    <!-- Menubar -->
    <div class="menubar">
      <div class="menu-item">File</div>
      <div class="menu-item">Edit</div>
      <div class="menu-item">View</div>
      <div class="menu-item">Insert</div>
      <div class="menu-item">Cell</div>
      <div class="menu-item">Kernel</div>
      <div class="menu-item">Widgets</div>
      <div class="menu-item">Help</div>
    </div>

    <!-- Toolbar -->
    <div class="toolbar">
      <div class="btn-group">
        <button class="tb-btn" title="Save and Checkpoint">&#128190;</button>
      </div>
      <div class="btn-group">
        <button class="tb-btn" title="Insert Cell Below">&#10133;</button>
        <button class="tb-btn" title="Cut Selected Cells">&#9986;</button>
        <button class="tb-btn" title="Copy Selected Cells" onclick="copyCurrentCell()">&#128203;</button>
        <button class="tb-btn" title="Paste Cells Below">&#128196;</button>
      </div>
      <div class="btn-group">
        <button class="tb-btn" title="Move Selected Cells Up">&#9650;</button>
        <button class="tb-btn" title="Move Selected Cells Down">&#9660;</button>
      </div>
      <div class="btn-group">
        <button class="tb-btn" title="Run Cell" style="color: #2b7a0b; font-weight: bold;" onclick="copyCurrentCell()">&#9654; Run</button>
        <button class="tb-btn" title="Interrupt Kernel">&#9209;</button>
        <button class="tb-btn" title="Restart Kernel">&#128260;</button>
        <button class="tb-btn" title="Restart & Run All">&#9193;</button>
      </div>
      <select class="tb-select">
        <option>Code</option>
        <option>Markdown</option>
        <option>Raw NBConvert</option>
        <option>Heading</option>
      </select>
      <div class="shortcut-badge">
        <span>Click any cell to copy | Keys:</span>
        <span class="key-badge" onclick="copyProgram(1)">[1] Eigenvalues</span>
        <span class="key-badge" onclick="copyProgram(2)">[2] Newton-Raphson</span>
        <span class="key-badge" onclick="copyProgram(3)">[3] Growth &amp; Decay</span>
        <span class="key-badge" onclick="copyProgram(4)">[4] Diff Eq (CF)</span>
      </div>
    </div>
  </div>

  <!-- Notebook Body -->
  <div id="notebook-container">

    <!-- Markdown Overview -->
    <div class="markdown-cell">
      <h1>Python Computational Lab Manual</h1>
      <p>Complete Exact Implementation: Source Code, Console Execution Output &amp; Graphical Visualizations</p>
    </div>

    <!-- Cell 1: Program 1 -->
    <div class="exp-heading">EXPERIMENT 01 &bull; UNIT-I: EIGEN VALUES &amp; EIGEN VECTORS</div>
    <div class="cell code-cell selected" id="cell-1" onclick="selectAndCopy(1)">
      <div class="cell-input-row">
        <div class="prompt">In&nbsp;[1]:</div>
        <div class="cell-wrapper">
          <div class="cell-actions">
            <button class="copy-btn" id="copy-btn-1" onclick="event.stopPropagation(); copyProgram(1);">&#128203; Copy Code</button>
          </div>
          <div class="code-container highlight" id="code-1">{html1}</div>
        </div>
      </div>
      <div class="cell-output-row">
        <div class="output-prompt">Out&nbsp;[1]:</div>
        <div class="output-container">
          <div class="output-subtext">{out1_text}</div>
          <div class="output-figure">
            <img src="data:image/png;base64,{images_b64[1]}" alt="Figure 1: Quiver plot showing eigenvectors x and transformed vectors Ax">
            <span class="figure-caption">Figure 1: Quiver plot showing eigenvectors x and transformed vectors Ax</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Cell 2: Program 2 -->
    <div class="exp-heading">EXPERIMENT 02 &bull; NUMERICAL METHODS: ROOT FINDING</div>
    <div class="cell code-cell" id="cell-2" onclick="selectAndCopy(2)">
      <div class="cell-input-row">
        <div class="prompt">In&nbsp;[2]:</div>
        <div class="cell-wrapper">
          <div class="cell-actions">
            <button class="copy-btn" id="copy-btn-2" onclick="event.stopPropagation(); copyProgram(2);">&#128203; Copy Code</button>
          </div>
          <div class="code-container highlight" id="code-2">{html2}</div>
        </div>
      </div>
      <div class="cell-output-row">
        <div class="output-prompt">Out&nbsp;[2]:</div>
        <div class="output-container">
          <div class="output-subtext">{out2_text}</div>
          <div class="output-figure">
            <img src="data:image/png;base64,{images_b64[2]}" alt="Figure 2: Plot of f(x) = x·ln(x) - 1.2 intersecting the x-axis at root ≈ 1.888087">
            <span class="figure-caption">Figure 2: Plot of f(x) = x&middot;ln(x) - 1.2 intersecting the x-axis at root &asymp; 1.888087</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Cell 3: Program 3 -->
    <div class="exp-heading">EXPERIMENT 03 &bull; DIFFERENTIAL EQUATIONS: APPLICATIONS</div>
    <div class="cell code-cell" id="cell-3" onclick="selectAndCopy(3)">
      <div class="cell-input-row">
        <div class="prompt">In&nbsp;[3]:</div>
        <div class="cell-wrapper">
          <div class="cell-actions">
            <button class="copy-btn" id="copy-btn-3" onclick="event.stopPropagation(); copyProgram(3);">&#128203; Copy Code</button>
          </div>
          <div class="code-container highlight" id="code-3">{html3}</div>
        </div>
      </div>
      <div class="cell-output-row">
        <div class="output-prompt">Out&nbsp;[3]:</div>
        <div class="output-container">
          <div class="output-subtext">{out3_text}</div>
          <div class="output-figure">
            <img src="data:image/png;base64,{images_b64[3]}" alt="Figure 3: Exponential growth curve showing observed points (t1=1, P1=332) and (t2=1.5, P2=604.91)">
            <span class="figure-caption">Figure 3: Exponential growth curve showing observed points (t1=1, P1=332) and (t2=1.5, P2=604.91)</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Cell 4: Program 4 -->
    <div class="exp-heading">EXPERIMENT 04 &bull; UNIT-V: HIGHER ORDER DIFFERENTIAL EQUATIONS</div>
    <div class="cell code-cell" id="cell-4" onclick="selectAndCopy(4)">
      <div class="cell-input-row">
        <div class="prompt">In&nbsp;[4]:</div>
        <div class="cell-wrapper">
          <div class="cell-actions">
            <button class="copy-btn" id="copy-btn-4" onclick="event.stopPropagation(); copyProgram(4);">&#128203; Copy Code</button>
          </div>
          <div class="code-container highlight" id="code-4">{html4}</div>
        </div>
      </div>
      <div class="cell-output-row">
        <div class="output-prompt">Out&nbsp;[4]:</div>
        <div class="output-container">
          <div class="output-subtext">{out4_text}</div>
          <div class="output-figure">
            <img src="data:image/png;base64,{images_b64[4]}" alt="Figure 4: Complementary function (CF) trajectory for constants C1 = C2 = C3 = 1">
            <span class="figure-caption">Figure 4: Complementary function (CF) trajectory for constants C1 = C2 = C3 = 1</span>
          </div>
        </div>
      </div>
    </div>

  </div>

  <!-- Toast Notification -->
  <div id="copy-toast">
    <span class="toast-icon">&#10003;</span>
    <span id="toast-msg">Program copied to clipboard!</span>
  </div>

  <script>
    // Pure Raw Python Code for each program
    const rawPrograms = {raw_json};

    let currentSelected = 1;
    let toastTimer = null;

    // Check URL parameters (e.g. ?p=2 to auto-select Program 2)
    const urlParams = new URLSearchParams(window.location.search);
    const paramP = parseInt(urlParams.get('p'));
    if (paramP >= 1 && paramP <= 4) {{
      currentSelected = paramP;
    }}

    // Select cell UI
    function selectCell(num) {{
      currentSelected = num;
      document.querySelectorAll('.cell.code-cell').forEach(c => c.classList.remove('selected'));
      const activeCell = document.getElementById('cell-' + num);
      if (activeCell) activeCell.classList.add('selected');
    }}

    // Show toast notification
    function showToast(msg) {{
      const toast = document.getElementById('copy-toast');
      const toastMsg = document.getElementById('toast-msg');
      const statusPill = document.getElementById('status-pill');

      toastMsg.textContent = msg;
      toast.classList.add('show');
      statusPill.innerHTML = `<span>&#10003; ${{msg}}</span>`;

      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => {{
        toast.classList.remove('show');
      }}, 2200);
    }}

    // Clipboard copy with modern API & fallback
    function writeToClipboard(text) {{
      if (navigator.clipboard && window.isSecureContext) {{
        return navigator.clipboard.writeText(text);
      }} else {{
        const textarea = document.createElement('textarea');
        textarea.value = text;
        textarea.style.position = 'fixed';
        textarea.style.left = '-9999px';
        document.body.appendChild(textarea);
        textarea.focus();
        textarea.select();
        return new Promise((resolve, reject) => {{
          const success = document.execCommand('copy');
          document.body.removeChild(textarea);
          success ? resolve() : reject();
        }});
      }}
    }}

    // Copy specific program
    function copyProgram(num) {{
      selectCell(num);
      const code = rawPrograms[num];

      // Ping local server to guarantee OS-level clipboard write (100% bypasses browser restrictions)
      fetch('/api/copy?p=' + num).catch(() => {{}});

      writeToClipboard(code).then(() => {{
        showToast(`Program ${{num}} copied to clipboard!`);
        
        // Highlight button briefly
        const btn = document.getElementById('copy-btn-' + num);
        if (btn) {{
          const original = btn.innerHTML;
          btn.classList.add('copied');
          btn.innerHTML = '&#10003; Copied!';
          setTimeout(() => {{
            btn.classList.remove('copied');
            btn.innerHTML = original;
          }}, 1500);
        }}
      }}).catch(err => {{
        showToast(`Tap or click to copy Program ${{num}}`);
      }});
    }}

    // Cell click handler
    function selectAndCopy(num) {{
      copyProgram(num);
    }}

    // Toolbar copy handler
    function copyCurrentCell() {{
      copyProgram(currentSelected);
    }}

    // Hotkeys: Press 1, 2, 3, 4 anywhere on page to copy that program
    window.addEventListener('keydown', (e) => {{
      // If typing in an input, don't trigger hotkeys
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

      if (e.key === '1') {{
        copyProgram(1);
      }} else if (e.key === '2') {{
        copyProgram(2);
      }} else if (e.key === '3') {{
        copyProgram(3);
      }} else if (e.key === '4') {{
        copyProgram(4);
      }}
    }});

    // Attempt direct copy on load
    window.addEventListener('DOMContentLoaded', () => {{
      selectCell(currentSelected);
      // Try immediate auto-copy
      writeToClipboard(rawPrograms[currentSelected]).then(() => {{
        showToast(`Program ${{currentSelected}} auto-copied!`);
      }}).catch(() => {{
        // If browser blocks non-gesture clipboard, auto-copy on the first click/keypress anywhere
        const oneTimeListener = () => {{
          copyProgram(currentSelected);
          window.removeEventListener('pointerdown', oneTimeListener);
          window.removeEventListener('keydown', oneTimeListener);
        }};
        window.addEventListener('pointerdown', oneTimeListener, {{ once: true }});
        window.addEventListener('keydown', oneTimeListener, {{ once: true }});
      }});
    }});
  </script>
</body>
</html>"""

with open("c:/Users/Akshaya/Downloads/scam2/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html regenerated cleanly! Size:", len(html_content))
