FROM ruby:2.7

ENV APP_ROOT /app

# ユーザ追加
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID devel
RUN useradd -u $UID -g devel -m devel
RUN echo "devel ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# USER
USER devel

#ADD
ADD ./app $APP_ROOT

# WORKDIR
WORKDIR $APP_ROOT
