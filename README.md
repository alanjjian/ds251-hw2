Explaining the MQTT topics and the QoS that you used.
Topics: 
- test_topic: we never got around to changing the topic names. This is OK but was a little annoying to debug. All messages are passed on this topic.
- We decided to use a QoS of 0 for all topics because we don't mind if a few messages containing the detected faces get lost. Additionally, QoS is the fastest and has the lowest overhead. 

Storing your faces in publicly reachable object storage or submitting them with your HW.
