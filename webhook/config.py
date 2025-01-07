from djchoices import ChoiceItem, DjangoChoices

class HttpMethodChoices(DjangoChoices):
    """Holds the HttpMethod types available for destination apis."""

    GET = ChoiceItem('GET', 'GET Method')
    POST = ChoiceItem('POST', 'POST Method')
    PUT = ChoiceItem('PUT', 'PUT Method')
