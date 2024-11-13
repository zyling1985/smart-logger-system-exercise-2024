# Import necessary libraries
import adafruit_minimqtt.adafruit_minimqtt as mqtt
import adafruit_connection_manager
import socketpool
import wifi


# Define a Communication class
class Communication:
    def __init__(self,message=None):
        # Create a socket pool using the Wi-Fi radio
        pool = adafruit_connection_manager.get_radio_socketpool(wifi.radio)
        # Create an MQTT client with the specified broker and port
        self.mqtt_client = mqtt.MQTT(broker='10.247.10.18',port=1883,socket_pool=pool)
        # Set the on_connect callback function
        self.mqtt_client.on_connect = self.on_connect        
        # Connect to the MQTT broker
        self.mqtt_client.connect()

    # Callback function called when the MQTT client successfully connects
    def on_connect(self,client,userdata,flags,rc):
        if rc == 0:
            print("Connected to broker")
        else:
            print("Connection failed")

     # Publish a message to a specified topic
    def publish(self,topic):       
        self.mqtt_client.publish('service/topic',topic)