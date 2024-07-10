import webbrowser
import uvicorn

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:8001")
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
