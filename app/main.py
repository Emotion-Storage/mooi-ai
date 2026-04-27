from app.config import settings
from app.controllers.fastapi.app import run_fastapi_app
from app.controllers.streamlit.app import run_streamlit_app


def main():
    mode = settings.APP_MODE
    if mode == "debug":
        run_streamlit_app(debug=True)
    elif mode == "streamlit":
        run_streamlit_app()
    elif mode == "fastapi":
        import uvicorn
        uvicorn.run("app.main:run_fastapi_app", host="0.0.0.0", port=8000, factory=True)
    else:
        raise ValueError(f"Invalid APP_MODE: '{mode}'. Use 'streamlit' or 'fastapi'.")


if __name__ == "__main__":
    main()
