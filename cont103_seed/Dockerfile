FROM ruby:2.6

ENV APP_ROOT /myapp

# ユーザ追加
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID devel
RUN useradd -u $UID -g devel -m devel
RUN echo "devel ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# USER
USER devel

# WORKDIR
WORKDIR $APP_ROOT
