FROM python:3.8
ENV PYTHONWRITECODE=1
ENV PYTHONBUFFERED=1
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
RUN apt update && apt install -y default-mysql-client && apt install -y netcat
RUN useradd app
RUN mkdir /code/staticfiles
RUN chown -R app:app /code
USER app
RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]

