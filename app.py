from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "v1")
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TravelX - Explore The World</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Poppins',sans-serif;}}
body{{background:#f4f7fa;scroll-behavior:smooth;}}

header{{
position:fixed;width:100%;top:0;left:0;
display:flex;justify-content:space-between;align-items:center;
padding:15px 70px;
background:linear-gradient(135deg,#0d6efd,#6610f2);
color:white;z-index:1000;transition:0.3s;
}}

.logo{{font-size:22px;font-weight:700;}}

.hero{{
height:100vh;
background:url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e') no-repeat center/cover;
display:flex;justify-content:center;align-items:center;
text-align:center;color:white;position:relative;overflow:hidden;
}}

.hero h1{{font-size:55px;}}

section{{padding:120px 80px;}}

.section-title{{
text-align:center;margin-bottom:60px;font-size:38px;font-weight:700;
background:linear-gradient(45deg,#0d6efd,#6610f2);
-webkit-background-clip:text;color:transparent;
}}

footer{{background:#111;color:white;text-align:center;padding:20px;}}
</style>
</head>

<body>

<header>
<div class="logo">✈️ TravelX | {version}</div>
</header>

<section class="hero">
<h1>Experience The Beauty of The Ocean 🌊</h1>
</section>

<section>
<h2 class="section-title">Welcome to Secure CI/CD Travel Dashboard</h2>
<p style="text-align:center;font-size:18px;">
Deployed via Docker → Artifact Registry → GKE 🚀
</p>
</section>

<footer>
© 2026 TravelX | Designed with ❤️ @cloudambassadorsteam
</footer>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
