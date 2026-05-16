
from typing import Callable

async def app(
    scope: dict,
    receive: Callable,
    send: Callable,
) -> None:
    # env에 있는 입력 정보를 처리하여 출력 데이터 생성
    data = b"Hello, world!"

    # 상태 코드와 헤더 전송
    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [(b"content-type", b"text/plain")],
    })

    # 응답 본문 전송
    await send({
        "type": "http.response.body",
        "body": data,
    })
