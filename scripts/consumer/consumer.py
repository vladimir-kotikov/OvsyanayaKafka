import json
import time
from kafka import KafkaConsumer
from kafka_common import AKafkaCommon

class AConsumer(AKafkaCommon):
    """
    Kafka consumer
    """
    def __init__(self, host = 'localhost', port = '9092', *args, **kwargs):
        super(AConsumer, self).__init__(host, port, *args, **kwargs)

    def __connect(self, cb, topic):
        try:
            self.consumer = KafkaConsumer(bootstrap_servers = self.server())
            cb(topic)
        except:
            time.sleep(1000)
            self.__connect(cb, topic)

    def listen(self, topic):
        """
        Listen data topic
        """
        if hasattr(self, 'consumer'):
            self.consumer.subscribe(topic)
            for msg in self.consumer:
                try:
                    print json.loads(msg.value)
                except:
                    print msg.value
        else:
            self.__connect(self.listen, topic)
