## docker run 명령어
> docker run -d --name youtube_download -p 7000:8501 youtube_download:1.1

## docker 내부 접속
> docker exec -it RL_cartpole /bin/bash

|  설명 |
|---|
| -d : 컨테이너를 백그라운드 모드로 실행|
| -p : 호스트의 7000번 포트를 컨테이너의 8501 포트에 매핑|

