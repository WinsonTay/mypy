# Stubs for http.client (Python 3.4)

from typing import Any, Dict
import email.message
import io

responses = ...  # type: Dict[int, str]

class HTTPMessage(email.message.Message):
    def getallmatchingheaders(self, name): ...

class HTTPResponse(io.RawIOBase):
    fp = ...  # type: Any
    debuglevel = ...  # type: Any
    headers = ...  # type: Any
    version = ...  # type: Any
    status = ...  # type: Any
    reason = ...  # type: Any
    chunked = ...  # type: Any
    chunk_left = ...  # type: Any
    length = ...  # type: Any
    will_close = ...  # type: Any
    def __init__(self, sock, debuglevel=0, method=None, url=None): ...
    code = ...  # type: Any
    def begin(self): ...
    def close(self): ...
    def flush(self): ...
    def readable(self): ...
    def isclosed(self): ...
    def read(self, amt=None): ...
    def readinto(self, b): ...
    def fileno(self): ...
    def getheader(self, name, default=None): ...
    def getheaders(self): ...
    def __iter__(self): ...
    def info(self): ...
    def geturl(self): ...
    def getcode(self): ...

class HTTPConnection:
    response_class = ...  # type: Any
    default_port = ...  # type: Any
    auto_open = ...  # type: Any
    debuglevel = ...  # type: Any
    mss = ...  # type: Any
    timeout = ...  # type: Any
    source_address = ...  # type: Any
    sock = ...  # type: Any
    def __init__(self, host, port=None, timeout=..., source_address=None): ...
    def set_tunnel(self, host, port=None, headers=None): ...
    def set_debuglevel(self, level): ...
    def connect(self): ...
    def close(self): ...
    def send(self, data): ...
    def putrequest(self, method, url, skip_host=0, skip_accept_encoding=0): ...
    def putheader(self, header, *values): ...
    def endheaders(self, message_body=None): ...
    def request(self, method, url, body=None, headers=...): ...
    def getresponse(self): ...

class HTTPSConnection(HTTPConnection):
    default_port = ...  # type: Any
    key_file = ...  # type: Any
    cert_file = ...  # type: Any
    def __init__(self, host, port=None, key_file=None, cert_file=None, timeout=...,
                 source_address=None, *, context=None, check_hostname=None): ...
    sock = ...  # type: Any
    def connect(self): ...

class HTTPException(Exception): ...
class NotConnected(HTTPException): ...
class InvalidURL(HTTPException): ...

class UnknownProtocol(HTTPException):
    args = ...  # type: Any
    version = ...  # type: Any
    def __init__(self, version): ...

class UnknownTransferEncoding(HTTPException): ...
class UnimplementedFileMode(HTTPException): ...

class IncompleteRead(HTTPException):
    args = ...  # type: Any
    partial = ...  # type: Any
    expected = ...  # type: Any
    def __init__(self, partial, expected=None): ...

class ImproperConnectionState(HTTPException): ...
class CannotSendRequest(ImproperConnectionState): ...
class CannotSendHeader(ImproperConnectionState): ...
class ResponseNotReady(ImproperConnectionState): ...

class BadStatusLine(HTTPException):
    args = ...  # type: Any
    line = ...  # type: Any
    def __init__(self, line): ...

class LineTooLong(HTTPException):
    def __init__(self, line_type): ...

error = HTTPException
