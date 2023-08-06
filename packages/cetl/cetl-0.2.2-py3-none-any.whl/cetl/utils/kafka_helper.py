# pip install kafka-python
# pip install avro-python3
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from kafka.admin import KafkaAdminClient, NewTopic
import json
import pandas as pd
from kafka import KafkaProducer
import io
import pandas as pd
import pickle
from cryptography.fernet import Fernet
from kafka.errors import UnknownTopicOrPartitionError

class kafkaHelper:
    """usage
    # Define Kafka connection parameters
    bootstrap_servers = ['192.168.32.1:9092']
    topic_name = 'mytopic2'
    # task_id
    task_id = b"1.filterBy"
    # Create a pandas dataframe
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})

    with kafkaHelper(   bootstrap_servers=bootstrap_servers,
                        topic=topic_name) as kh:

        # serialize the dataframe to pickle
        serialized_data = km.serialize_dataframe(df)
        # print("serialized_data: ", serialized_data)

        # create instance of encryption
        encrypted_data = kh.fernet.encrypt(serialized_data)
        # print(encrypted_data)

        # send the data to kafka topic
        km.send(key=task_id, value=encrypted_data)


        # received message
        message = kh.receive(task_id)

        # decrypt the message
        decrypted_data = kh.fernet.decrypt(message)

        # decode by pickle
        df = kh.deserialize_dataframe(decrypted_data)

        print(df)

        # delete the topic
        kh.delete_topic()
    """
    def __init__(self,
                bootstrap_servers=None,
                topic=None):

        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.producer=None
        self.consumer=None
        

    def __enter__(self,):
        
        try:
            # self.admin_client = KafkaAdminClient(bootstrap_servers=self.bootstrap_servers)
            # try:
            #     self.delete_topic()
            # except Exception as e:
            #     print("delete_topic got error")

            # Create a Kafka producer instance
            # self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)

            # create instance of KafkaConsumer
            self.consumer = KafkaConsumer(self.topic,
                                    bootstrap_servers=self.bootstrap_servers,
                                    auto_offset_reset='earliest',
                                    enable_auto_commit=True)
        except Exception as e:
            # print("####################", e)
            # print("close producer instance")
            # self.producer.close()
            # self.consumer.close()
            print("has error")
        
        return self


    def __exit__(self, exc_type, exc_value, exc_tb):
        print("test when will run exit ################################")
        self.producer.close()
        self.consumer.close()

    def topic_exists(self, admin_client, topic_name):
        """
        [{'error_code': 3, 'topic': 'c', 'is_internal': False, 'partitions': []}, 
        {'error_code': 3, 'topic': 'o', 'is_internal': False, 'partitions': []}, 
        {'error_code': 3, 'topic': '3', 'is_internal': False, 'partitions': []}, 
        {'error_code': 3, 'topic': 'm', 'is_internal': False, 'partitions': []}, 
        {'error_code': 3, 'topic': 't', 'is_internal': False, 'partitions': []}, 
        {'error_code': 3, 'topic': 'p', 'is_internal': False, 'partitions': []}, 
        {'error_code': 3, 'topic': 'y', 'is_internal': False, 'partitions': []}, 
        {'error_code': 3, 'topic': 'i', 'is_internal': False, 'partitions': []}]
        """
        try:
            topic_metadata = admin_client.describe_topics([topic_name])
            print(topic_metadata)
            # for partition_data in topic_metadata:
            #     if "error_code" in partition_data:

            # print("show topic_metadata", topic_metadata)
            if "error_code" in topic_metadata[0]:
                if topic_metadata[0]["error_code"]==3:
                    return False
            
            return True
        except UnknownTopicOrPartitionError:
            return False


    def delete_topic(self):   
        if not self.admin_client:
            # call back
            print("call back #####")
            self.__enter__()
        

        if self.topic_exists(self.admin_client, self.topic):
            print("deleting###########################", self.topic)
            self.admin_client.delete_topics([self.topic])


    def send(self, key=None, value=None):
        # if not self.producer:
            # print("self.producer is none ##############")
            # self.__enter__()

        print(f"open topic: {self.topic}")
        print(f"key: {key}")
        print(f"value: {value}")
        print("self.producer", self.producer)
        print("bootstrap_servers", self.bootstrap_servers)
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)
        self.producer.send(self.topic, key="1.dummyStart", value=value)
        # try:
        #     self.producer.send(self.topic, key=b'1.dummyStart', value=value)
        # except Exception as e:
        #     print("self.producer.send() got error")
        #     print(str(e))
        # producer.flush()


    def receive(self, key):
        if not self.consumer:
            self.__enter__()

        for message in self.consumer:
            print("message.key", message.key)
            print("message.value", message.value)
            if message.key == key:
                received_message = message.value
                self.consumer.close()
                return received_message


    def close(self):
        self.producer.close()
        self.consumer.close()


    def serialize_dataframe(self, df):
        return pickle.dumps(df)

    
    def deserialize_dataframe(self, serialized_data):
        # deserialize the data
        file_obj = io.BytesIO(serialized_data)
        df = pickle.load(file_obj)
        return df

    
# class kafkaMedia(kafkaHelper):
#     def __init__(self, 
#                 bootstrap_servers=None,
#                 topic=None):
#         super().__init__(bootstrap_servers=bootstrap_servers,
#                         topic=topic)


#     def python2kafka(self, key=None, value=None):

#         if isinstance(value, pd.DataFrame):
#             df = value

#             # serialize the dataframe to pickle
#             serialized_data = self.serialize_dataframe(df)
#             # print("serialized_data: ", serialized_data)

#             # create instance of encryption
#             encrypted_data = self.fernet.encrypt(serialized_data)
#             # print(encrypted_data)

#             # send the data to kafka topic
#             self.send(key=key, value=encrypted_data)

#     def kafka2python(self, key=None):

        
#         # received message
#         message = self.receive(key)

#         # decrypt the message
#         decrypted_data = self.fernet.decrypt(message)

#         # decode by pickle
#         df = self.deserialize_dataframe(decrypted_data)

#         # delete the topic
#         # kh.delete_topic()

#         return df


