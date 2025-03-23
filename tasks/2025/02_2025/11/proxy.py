import re

from aiohttp import ClientSession
from aiohttp.web import Application, run_app
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from bs4 import BeautifulSoup

BASE_URL = "https://news.ycombinator.com"
PORT = 8232


async def handle_request(request: Request) -> Response:
    async with ClientSession() as session:
        async with session.get(f"{BASE_URL}{request.rel_url}") as response:
            headers = {
                key: value
                for key, value in response.headers.items()
                if key.lower() not in ["content-encoding", "transfer-encoding", "content-length"]
            }
            body = await response.text()
            body = modify_content(content=body)
            return Response(body=body, headers=headers, status=response.status)


def modify_content(content: str) -> str:
    soup = BeautifulSoup(content, "html.parser")

    text_parts = soup.find_all(text=True)

    for text in text_parts:
        if text.strip():
            text.replace_with(re.sub(r"\b\w{6}\b", lambda m: f"{m.group(0)}™", text))

    return str(soup)


async def init_app() -> Application:
    app = Application()
    app.router.add_get("/{suffix:.*}", handle_request)
    return app


if __name__ == "__main__":
    run_app(init_app(), port=PORT)
