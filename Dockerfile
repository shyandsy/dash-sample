# docker build -t tiny_home .
# docker image ls
#   show up: =====> tiny_home      latest       6f8cfef20b29   About a minute ago   479MB
# docker run -p 8080:80 tiny_home

# FROM python:3.9-slim
FROM china-devops-docker-local.arf.tesla.cn/base-images/python:3.8
#FROM china-dots-system-docker-local.arf.tesla.cn/share/dots:builder as compiler

COPY requirements.txt ./requirements.txt

#COPY . ./
RUN GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/shyandsy/dash-sample dash-sample
WORKDIR dash-sample

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD gunicorn -b 0.0.0.0:80 app.app:server