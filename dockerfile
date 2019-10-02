FROM python:3.7.4-stretch

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY webService.py ./
COPY config.py ./
COPY Summaries.py ./
COPY InterdaySummaries.csv ./

CMD [ "python", "./webService.py" ]