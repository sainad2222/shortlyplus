from concurrent import futures

import grpc
import api_pb2
import api_pb2_grpc
import random
import string
import re


class ShortenService(api_pb2_grpc.ShortenerServicer):
    def __init__(self, *args, **kwargs):
        pass

    def shortenURL(self, request, context):
        url = request.url
        url, error = self.validateURL(url)
        if error:
            result = {"error": error}
            return api_pb2.shortenURLResponse(**result)
        slug = request.slug
        stub = self.create_stub_DB()
        if slug:
            if len(slug) < 6:
                result = {"error": "Slug should be atleast 6 characters"}
                return api_pb2.shortenURLResponse(**result)
            res = stub.checkIfPresent(api_pb2.checkIfPresentRequest(slug=slug))
            if res.error:
                return api_pb2.shortenURLResponse(**res)
            if res.isPresent:
                result = {'error': "Slug already exists"}
                return api_pb2.shortenURLResponse(**result)
        else:
            slug, error = self.generateUniqueRandomSlug(stub)
            if error != "":
                return api_pb2.checkIfPresentResponse(**error)
        res = stub.storeInDB(api_pb2.storeInDBRequest(url=url, slug=slug))
        if res.error:
            return api_pb2.shortenURLResponse(**res.error)

        result = {'shortURL': slug}
        return api_pb2.shortenURLResponse(**result)

    def create_stub_DB(self):
        channel = grpc.insecure_channel('db:50052')
        stub = api_pb2_grpc.DatabaseStub(channel)
        return stub

    def generateUniqueRandomSlug(self, stub):
        characterMask = string.ascii_letters + string.digits
        currentSlug = ''.join(random.choice(characterMask)
                              for _ in range(6))

        res = stub.checkIfPresent(
            api_pb2.checkIfPresentRequest(slug=currentSlug))
        while True:
            currentSlug = ''.join(random.choice(
                characterMask) for _ in range(6))
            res = stub.checkIfPresent(
                api_pb2.checkIfPresentRequest(slug=currentSlug))
            if res.error:
                return ("", res.error)
            if not res.isPresent:
                break
        return (currentSlug, "")

    def validateURL(self, url):
        patt = re.compile(
            r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
        if not patt.match(url):
            return "", "Invalid URL"
        if not url.startswith("http"):
            url = "http://"+url
        return url, ""


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    api_pb2_grpc.add_ShortenerServicer_to_server(ShortenService(), server)
    server.add_insecure_port('[::]:50051')
    print("[INFO] started listening on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
