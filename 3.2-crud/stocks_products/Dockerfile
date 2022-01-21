FROM python
ENV PROJPATH=/crud
WORKDIR /stocks_products
EXPOSE 8000
COPY manage.py .
COPY requirements.txt .
COPY ./stocks_products ./stocks_products
COPY ./logistic ./logistic
RUN pip install -r ./requirements.txt
RUN python ./manage.py migrate
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]