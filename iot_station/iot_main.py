# importing pubnub libraries
from pubnub.pubnub import PubNub, SubscribeListener, SubscribeCallback, PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.exceptions import PubNubException
from plantower import pt_pms5003
from ds18b20   import ds18b20_read
import pubnub

pnconf = PNConfiguration()
pnconf.publish_key = ''
pnconf.subscribe_key = ''
pubnub = PubNub(pnconf)

channel  ='jinz_station'

pmx_str  ='jinz_getpmx'
temp_str ='jinz_gettemp'

data = {                                    # data to be published
    'username': 'Rasberry Jin',
    'message' : 'Test Publish'
}

class MyListener(SubscribeCallback):        # Not need for working of this program
    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNConnectedCategory:
            pubnub.publish().channel(channel).message({'fieldA': 'awesome', 'fieldB': 10}).sync()

    def message(self, pubnub, message):
        print(message)

    def presence(self, pubnub, presence):
        pass

my_listener = SubscribeListener()                   # create listner_object to read the msg from the Broker/Server
pubnub.add_listener(my_listener)                    # add listner_object to pubnub_object to subscribe it
pubnub.subscribe().channels(channel).execute()      # subscribe the channel (Runs in background)

my_listener.wait_for_connect()                      # wait for the listner_obj to connect to the Broker.Channel
print('connected')                                  # print confirmation msg

pubnub.publish().channel(channel).message(data).sync()      # publish the data to the mentioned channel

while True:                                                 # Infinite loop
    result = my_listener.wait_for_message_on(channel)       # Read the new msg on the channel
    print(result.message)                                   # print the new msg
    for command in result.message.values():
        # Check for PM command.
        if command == pmx_str:
          pm_instance = pt_pms5003('/dev/ttyAMA0')
          pma,pmb,pmc = pm_instance.pt_pms5003_read()
          data['message']="PM 1.0="+str(pma)+" PM 2.5="+str(pmb)+" PM 10.0="+str(pmc)
          pubnub.publish().channel(channel).message(data).sync()
        # Check for Temperature command.
        elif command == temp_str:
          data['message'] = "Temperature(Celcuis) = "+ds18b20_read()
          pubnub.publish().channel(channel).message(data).sync()
