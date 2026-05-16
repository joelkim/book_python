
from collections.abc import Callable, Iterable

def app(env: dict, start_response:  Callable) -> Iterable[bytes]:
  # env에 있는 입력 정보를 처리하여 결과 데이터 생성
  data = b"Hello, World!"
  # start_response 함수를 호출하여 상태, 헤더, 예외 전송
  start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data))),
    ])
  # 결과를 이터러블 객체로 반환
  return [data]
```
