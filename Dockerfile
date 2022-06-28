FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3-minimal python3-pip pandoc
RUN pip3 install Markupsafe==1.1.1 flask==1.1.1

COPY main.py /main.py

ENTRYPOINT ["python3"]
CMD ["main.py"]
