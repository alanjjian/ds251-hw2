This homework was completed jointly by Alan Jian and Silas Gifford. 

MQTT Topics: 
- test_topic: we never got around to changing the topic names. This is OK but was a little annoying to debug. All messages are passed on this topic.
- We decided to use a QoS of 0 for all topics because we don't mind if a few messages containing the detected faces get lost. Additionally, QoS is the fastest and has the lowest overhead. 

Storing your faces in publicly reachable object storage or submitting them with your HW.

We had some issues getting a link to S3 so see the screenshot in `hw2-s3-screenshot.jpg` to see that images are in S3. An example image can be found in the repo. 

The instructions for this homework submission were confusing. We hope this readme is sufficient. Please let us know if it is not.
