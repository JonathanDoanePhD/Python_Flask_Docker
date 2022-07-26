FROM python:3

COPY . /Fetch_Rewards

WORKDIR /Fetch_Rewards

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "api.py"]