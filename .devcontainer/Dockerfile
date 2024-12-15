# ベースイメージ
FROM python:3.11-slim

# 必要な環境を更新・インストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-venv \
    build-essential \
    curl \
    wget \
    git \
    zip \
    unzip \
    vim \
    iputils-ping \
    net-tools \
    software-properties-common \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# pip インストール
RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel