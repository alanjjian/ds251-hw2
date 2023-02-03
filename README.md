65 points for a containerized end to end application 
We created 

5 points for using a user defined network in the cloud (automatic if you decide to use k8s on the cloud side)
10 points for using Kubernetes on your Edge VM
10 points for explaining the MQTT topics and the QoS that you used.
Topics: 
-faces: from face_detector to broker
-faces2: from broker to forwarder and from broker to logger
-faces3: from forwarder to ...
We decided to use a QoS of 0 for all topics because we don't mind if a few messages containing the detected faces get lost. Additionally, QoS is the fastest and has the lowest overhead. 

10 points for storing your faces in publicly reachable object storage or submitting them with your HW.
