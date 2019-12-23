#FROM ubuntu
FROM 480377481292.dkr.ecr.cn-north-1.amazonaws.com.cn/yuantestrepo:basecn
WORKDIR /usr/local/src/test1
RUN apt-get update -qq
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y unzip 
#RUN sudo apt-get install  python3
#RUN sudo apt-get install  python3-pip
RUN apt-get install -y python-dev build-essential
RUN apt-get install -y python3-pip
RUN pip3 install boto3
RUN pip3 install configparser
RUN pip3 install oss2
COPY test1.zip ./
RUN unzip test1.zip
#CMD ["python3","/usr/local/src/test1/test.py"]

