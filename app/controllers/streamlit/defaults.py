import streamlit as st

from models import ChatSession, Gauge
from prompt.defaults import (
    DEFAULT_CHATBOT_PROMPT_MESSAGE,
    DEFAULT_TIMECAPSULE_ROLE_PROMPT_MESSAGE,
    DEFAULT_TIMECAPSULE_REFERENCE_PROMPT_MESSAGE,
    DEFAULT_TIMECAPSULE_ANALYZE_PROMPT_MESSAGE,
    DEFAULT_SENTIMENT_ROLE_PROMPT_MESSAGE,
    DEFAULT_SENTIMENT_REFERENCE_PROMPT_MESSAGE,
    DEFAULT_SENTIMENT_ANALYZE_PROMPT_MESSAGE,
    DEFAULT_GAUGE_ANALYZE_PROMPT_MESSAGE,
    DEFAULT_GAUGE_REFERENCE_PROMPT_MESSAGE,
)
from services import ChatService


def init_session(chat_service: ChatService):

    defaults = {
        "current_session": "대화 1",
        "gauge": None,
        "sentiment_output": None,
        "timecapsule": None,
        "chat_prompt_message": DEFAULT_CHATBOT_PROMPT_MESSAGE,
        "gauge_reference_prompt_message": DEFAULT_GAUGE_REFERENCE_PROMPT_MESSAGE,
        "gauge_content_prompt_message": DEFAULT_GAUGE_ANALYZE_PROMPT_MESSAGE,
        "capsule_role_prompt_message": DEFAULT_TIMECAPSULE_ROLE_PROMPT_MESSAGE,
        "capsule_reference_prompt_message": DEFAULT_TIMECAPSULE_REFERENCE_PROMPT_MESSAGE,
        "capsule_content_prompt_message": DEFAULT_TIMECAPSULE_ANALYZE_PROMPT_MESSAGE,
        "analyze_role_prompt_message": DEFAULT_SENTIMENT_ROLE_PROMPT_MESSAGE,
        "analyze_reference_prompt_message": DEFAULT_SENTIMENT_REFERENCE_PROMPT_MESSAGE,
        "analyze_content_prompt_message": DEFAULT_SENTIMENT_ANALYZE_PROMPT_MESSAGE,
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)

    if chat_service.repo.get("대화 1") is None:
        chat_service.repo.save(ChatSession(session_id="대화 1"))
