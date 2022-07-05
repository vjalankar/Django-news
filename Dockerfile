FROM python
RUN mkdir /news-app
WORKDIR /news-app/newsproject
ADD . /news-app/newsproject
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0:8000
