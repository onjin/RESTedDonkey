from StringIO import StringIO

from twisted.web import server
from twisted.web.test.test_web import DummyChannel
from twisted.web.http_headers import Headers
from twisted.internet.defer import succeed

from mock import Mock


def requestMock(path, method="GET", host="localhost", port=8080,
                isSecure=False, body=None, headers=None):
    if not headers:
        headers = {}

    if not body:
        body = ''

    request = server.Request(DummyChannel(), False)
    request.gotLength(len(body))
    request.content = StringIO()
    request.content.write(body)
    request.requestHeaders = Headers(headers)
    request.setHost(host, port, isSecure)
    request.uri = path
    request.prepath = []
    request.postpath = path.split('/')[1:]
    request.method = method
    request.clientproto = 'HTTP/1.1'

    request.setHeader = Mock(wraps=request.setHeader)
    request.setResponseCode = Mock(wraps=request.setResponseCode)

    request.finish = Mock(wraps=request.finish)
    request.write = Mock(wraps=request.write)

    def registerProducer(producer, streaming):
        # This is a terrible terrible hack.
        producer.resumeProducing()
        producer.resumeProducing()

    request.registerProducer = registerProducer
    request.unregisterProducer = Mock()

    return request


def _render(resource, request):
    result = resource.render(request)
    if isinstance(result, str):
        request.write(result)
        request.finish()
        return succeed(None)
    elif result is server.NOT_DONE_YET:
        if request.finished:
            return succeed(request)
        else:
            return request.notifyFinish().addCallback(lambda _: request)
    else:
        raise ValueError("Unexpected return value: %r" % (result,))
