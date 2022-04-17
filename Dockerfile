FROM python
WORKDIR /root/doc_demo
ADD . /root/doc_demo

RUN pip install pandas
RUN pip install sklearn
RUN pip install flask
RUN pip install flask-restful

CMD ["python3","/root/doc_demo/app.py"]


