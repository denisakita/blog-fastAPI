import webbrowser

import uvicorn


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:8000")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
