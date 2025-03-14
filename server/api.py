from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .routes import router as GitaAPIRouter

app = FastAPI()


@app.get("/", tags = ["Root"], response_class = HTMLResponse)
async def read_root() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bhagavad Gita API</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Poppins', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .header {
            text-align: center;
            padding: 40px 0;
            background: linear-gradient(135deg, #ff9966, #ff5e62);
            color: white;
            border-radius: 10px;
            margin-bottom: 40px;
        }
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        .section {
            background: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .section h2 {
            color: #ff5e62;
            margin-bottom: 20px;
        }
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .feature-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #ff5e62;
        }
        .endpoints {
            border-collapse: collapse;
            width: 100%;
        }
        .endpoints th, .endpoints td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        .endpoints th {
            background-color: #f8f9fa;
            color: #ff5e62;
        }
        .button {
            display: inline-block;
            padding: 12px 24px;
            background: #ff5e62;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            transition: background 0.3s;
        }
        .button:hover {
            background: #ff9966;
        }
        .languages {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-top: 20px;
        }
        .language-badge {
            background: #f8f9fa;
            color: #ff5e62;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: 500;
        }
        @media (max-width: 768px) {
            body {
                padding: 10px;
            }
            .header {
                padding: 30px 20px;
            }
            .section {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🕉️ Bhagavad Gita API</h1>
        <p>Access the divine wisdom of Bhagavad Gita in multiple languages</p>
        <div class="languages">
            <span class="language-badge">Telugu (tel)</span>
            <span class="language-badge">Odia (odi)</span>
        </div>
    </div>

    <div class="section">
        <h2>About</h2>
        <p>A FastAPI-based REST API service that provides Bhagavad Gita verses in multiple languages. Access all 700 verses across 18 chapters with detailed translations, transliterations, and meanings.</p>
        <div style="margin-top: 20px">
            <a href="/docs" class="button">API Documentation</a>
            <a href="https://github.com/bewithdhanu/gita-api-vercel" class="button" style="margin-left: 10px">GitHub Repository</a>
        </div>
    </div>

    <div class="section">
        <h2>Features</h2>
        <div class="features-grid">
            <div class="feature-card">
                <h3>Complete Coverage</h3>
                <p>Access all 700 verses from 18 chapters</p>
            </div>
            <div class="feature-card">
                <h3>Multiple Languages</h3>
                <p>Available in Telugu and Odia</p>
            </div>
            <div class="feature-card">
                <h3>Rich Content</h3>
                <p>Includes verse text, translation, transliteration, and meanings</p>
            </div>
            <div class="feature-card">
                <h3>Audio Support</h3>
                <p>Audio recitations available for verses</p>
            </div>
        </div>
    </div>

    <div class="section">
        <h2>API Endpoints</h2>
        <table class="endpoints">
            <tr>
                <th>Endpoint</th>
                <th>Description</th>
            </tr>
            <tr>
                <td><code>/{language}/chapters</code></td>
                <td>List all chapters with their names and verse counts</td>
            </tr>
            <tr>
                <td><code>/{language}/chapter/{chapter_no}/verses</code></td>
                <td>Get all verses from a specific chapter</td>
            </tr>
            <tr>
                <td><code>/{language}/verse/{chapter_no}/{verse_no}</code></td>
                <td>Get a specific verse by chapter and verse number</td>
            </tr>
            <tr>
                <td><code>/{language}/verse/{verse_no_serial}</code></td>
                <td>Get a verse by its serial number (1-700)</td>
            </tr>
        </table>
    </div>

    <div class="section">
        <h2>Getting Started</h2>
        <p>To get started with the API, visit our <a href="/docs" style="color: #ff5e62">interactive documentation</a> where you can explore and test all available endpoints. The API is free to use and requires no authentication.</p>
        <p style="margin-top: 15px">For more information, bug reports, or contributions, please visit our <a href="https://github.com/dhanu0001/gita-api-vercel" style="color: #ff5e62">GitHub repository</a>.</p>
    </div>
</body>
</html> """


app.include_router(GitaAPIRouter)
