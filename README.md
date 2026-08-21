- name: Checkout repository
  uses: actions/checkout@v4

- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.10'

- name: Install dependencies & Buildozer
  run: |
    sudo apt-get update
    sudo apt-get install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libssl-dev libffi-dev libsqlite3-dev build-essential
    pip install --upgrade buildozer cython

- name: Build APK
  run: buildozer android debug
