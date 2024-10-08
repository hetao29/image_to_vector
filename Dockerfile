FROM ubuntu:24.04
LABEL maintainer="hetal<hetao@hetao.name>"
LABEL version="1.0"

RUN apt-get update
RUN apt-get install -y libgl1 git
RUN apt-get install -y python3 python3-opencv
RUN apt-get install -y python3-venv

WORKDIR /app
ENV PATH="$PATH:/app/local/bin"

RUN python3 -m venv /app/local
RUN sh /app/local/bin/activate
RUN pip config --user set global.index-url http://mirrors.aliyun.com/pypi/simple/
RUN pip config --user set global.trusted-host mirrors.aliyun.com
RUN pip install uvicorn 
RUN pip install fastapi 
RUN pip install pymysql 
RUN pip install rembg
RUN pip install towhee==0.8.0
RUN pip install pymilvus
RUN pip install librosa
RUN pip install opencv-python
RUN pip install matplotlib
RUN pip install cryptography
RUN pip install requests
RUN pip install numpy
RUN pip install timm
RUN pip install torch
RUN pip install torchvision
RUN pip cache purge

ENV HF_ENDPOINT=https://hf-mirror.com
COPY server /app

HEALTHCHECK --interval=5s --timeout=5s --retries=3 \
    CMD ps aux | grep "python" | grep -v "grep" > /dev/null; if [ 0 != $? ]; then exit 1; fi

EXPOSE 5000
CMD ["python", "server/image_to_vector.py"]
