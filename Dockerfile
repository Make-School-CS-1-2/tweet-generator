FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/
CMD [ "gunicorn", "-w", "4", "app:app"]