from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="hsraAI")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>hsraAI</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                }
                .container {
                    text-align: center;
                    background: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #667eea;
                    margin: 0;
                }
                p {
                    color: #666;
                    margin-top: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to hsraAI</h1>
                <p>Your FastAPI application is running!</p>
            </div>
        </body>
    </html>
    """

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "app": "hsraAI"}
