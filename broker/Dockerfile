FROM alpine:latest
RUN apk add mosquitto
RUN apk add --update py-pip
RUN pip3 install paho-mqtt 
# Configure to allow remote access
RUN echo "allow_anonymous true" > /etc/mosquitto/mosquitto.conf
RUN echo "listener 1883 0.0.0.0" >> /etc/mosquitto/mosquitto.conf
CMD ["mosquitto","-c","/etc/mosquitto/mosquitto.conf"]
# copy python to this stupid thing and run
COPY broker.py broker.py
CMD python3 broker.py
