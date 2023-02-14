FROM alpine:latest
RUN apk add mosquitto
RUN apk add gcc g++ zlib-dev make python3-dev py3-pip py3-numpy jpeg-dev
RUN pip3 install wheel
RUN pip3 install paho-mqtt
RUN pip3 install numpy
RUN pip3 install boto3
RUN pip3 install matplotlib 
# Configure to allow remote access
RUN echo "allow_anonymous true" > /etc/mosquitto/mosquitto.conf
RUN echo "listener 1883 0.0.0.0" >> /etc/mosquitto/mosquitto.conf
CMD ["mosquitto","-c","/etc/mosquitto/mosquitto.conf"]
# copy python to this stupid thing and run
COPY cloud-broker.py cloud-broker.py
CMD python3 cloud-broker.py
