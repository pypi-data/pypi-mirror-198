from requests.exceptions import HTTPError
class TooManyRequests(Exception):
    pass

class ChannelDeleted(HTTPError):
    pass

class NoVideoFound(Exception):
    pass
