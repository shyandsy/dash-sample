# docker build -t tiny_home .
# docker image ls
#   show up: =====> tiny_home      latest       6f8cfef20b29   About a minute ago   479MB
# docker run -p 8080:80 tiny_home
FROM python:3.9-slim
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . ./
CMD gunicorn -b 0.0.0.0:80 app.app:server