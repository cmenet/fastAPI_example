# Selects Python 3.9 image
FROM python:3.9

# Uses the root/code directory
WORKDIR /code

# Copies the requirements archive to the container
COPY ./backend/requirements.txt /code/requirements.txt

# Installs the Python requirenmentes
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
