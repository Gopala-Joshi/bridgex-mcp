from fastapi import FastAPI

app = FastAPI(
    title="BridgeX MCP",
    description="Universal Model Context Protocol Server",
    version="0.1"
)

@app.get("/")
def root():
    return {
        "project": "BridgeX MCP",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/tools")
def tools():
    return {
        "available_tools": [
            "system_metrics",
            "service_dependencies",
            "log_search"
        ]
    }