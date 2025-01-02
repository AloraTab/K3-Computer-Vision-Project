
FROM python:3.9


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt

# For fixing ImportError: libGL.so.1: cannot open shared object file: No such file or directory
RUN apt-get update
RUN apt install -y libgl1-mesa-glx

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
