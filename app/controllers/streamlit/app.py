from app.repositories import StreamlitSessionRepository
from app.services import ChatService


def build_streamlit_service():
    repo = StreamlitSessionRepository()
    return ChatService(repo)


def setup_streamlit_app(chat_service: ChatService, debug: bool = False):
    from app.controllers.streamlit import init_session
    from app.controllers.streamlit.views import run_main_ui, run_api_key_ui

    if debug:
        from dotenv import load_dotenv

        load_dotenv()
    else:
        run_api_key_ui()

    init_session(chat_service)
    run_main_ui(chat_service)


def run_streamlit_app(debug: bool = False):
    chat_service = build_streamlit_service()
    setup_streamlit_app(chat_service, debug)
