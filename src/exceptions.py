class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class NotResponseException(Exception):
    """Вызывается, когда от url нет ответа."""
    pass
