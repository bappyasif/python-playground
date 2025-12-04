from db import get_session
from db.models import User

def get_user_by_email(email: str):
    session = get_session()
    return session.query(User).filter(User.email == email).first()

def confirm_action(prompt: str) -> bool:
    response = input(f"{prompt} (y/n): ").strip().lower()
    return response == 'yes'