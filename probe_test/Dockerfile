FROM python
RUN apt-get update && apt-get  install vim git -y
RUN pip install Flask requests
RUN mkdir /app
RUN chown 1001 /app
COPY --chown=1001 app.py /app/flaskapp/app.py
USER 1001
WORKDIR /app/flaskapp
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
EXPOSE 5000
RUN chmod 777 /app/
CMD ["python","-m","flask","run","--host=0.0.0.0"]
