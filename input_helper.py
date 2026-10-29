def is_valid_question(question: str)->bool:
    if not question.strip():
        return False
    elif len(question) > 500:
        return False
    return True