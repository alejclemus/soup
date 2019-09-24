FROM python:3-alpine
RUN pip install pipenv
COPY Pipfile* /tmp
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/myapp
RUN pip install /tmp/myapp
CMD ["python3", "soup.py"]
ENV DEVELOPER="Alejandra Lemus"