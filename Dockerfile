FROM python
RUN apt-get update && apt-get  install vim -y
RUN pip install Flask requests
RUN mkdir /app
RUN chown 1001 /app
USER 1001
RUN cd /app; git clone https://github.com/kisshore/flaskapp.git
WORKDIR /app/flaskapp
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
EXPOSE 5000
CMD ["python","-m","flask","run","--host=0.0.0.0"]
