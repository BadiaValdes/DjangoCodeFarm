# # creating the consummer
#
# from channels.generic.websocket import AsyncWebsocketConsumer
# from economia.models import Salario
# from channels.db import database_sync_to_async
# import json
#
#
# class DashConsumer(AsyncWebsocketConsumer):
#
#     async def connect(self):
#         # we need to create a group for subscription
#         self.groupname = 'dashboard'
#         # connection is on
#         await self.channel_layer.group_add(
#             self.groupname,
#             self.channel_name
#         )
#
#         await self.accept()
#
#     async def disconnect(self, code):
#         await self.channel_layer.group_discard(
#             self.groupname,
#             self.channel_name
#         )
#
#     async def receive(self, text_data):
#         datapoint = json.loads(text_data)
#         val = datapoint['value']
#         #print(val)
#
#         await self.channel_layer.group_send(
#             # the name of the group that is subscribed
#             self.groupname,
#             # the data that will be send
#             {
#                 'type': 'deprocessing',
#                 'value': val
#             }
#
#         )
#         print('>>>>>', val)
#
#         # pass
#
#     # @database_sync_to_async
#     # def get_salario(self):
#     #     return Salario.objects.all()[0].amount
#     #
#     async def deprocessing(self, event):
#         valueOther = event['value']
#         self.send(text_data=json.dumps({'value': valueOther}))

# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from economia.models import Salario
from channels.db import database_sync_to_async
from django.core import serializers


class DashConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'dashboard'

        # Join room group
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name  # reference of the channel that is in use
            # self.channel_layer is the other method which reference the layer
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        value = text_data_json['value']
        #salario = await self.get_salario() //OLD


        # Send message to room group
        # this send the values to type method that were declare below
        # that method is the one who is going to process the info and send it to the view
        # here is only for the values that comes for the view
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'value': value,
                #'sal': salario, //OLD

            }
        )

    # Receive message from room group
    # and send it to the view
    async def chat_message(self, event):
        #message = event['value']
        #salario = json.loads(event['sal'])
        # I can do it by this way because the salario does not depends of
        # any value apart of the one which is in the database
        salario = await self.get_salario()
        fecha = await self.get_fecha()
        text_data = json.dumps({
            'sal': salario,
            'fech': fecha,
        })
        #print(self.channel_name)

        #print(salario)
        # Send message to WebSocket
        await self.send(text_data)

    # solo el salario de los ususarios
    @database_sync_to_async
    def get_salario(self):
        data = {}
        print(self.scope['session']['hola'])
        sal = Salario.objects.all()
        for idx, s in enumerate(sal):
            data['val' + idx.__str__()] = s.amount

        #salario = serializers.serialize('json', Salario.objects.all())
        #ss = json.dumps(data)
        return data
    # this is weird but, I have to turn into json to pass the salari form
    # get_salario al reciver.
    # when the chat_message enters in the process, I have to turn into python and turn that into json again
    # for more than one value

    @database_sync_to_async
    def get_fecha(self):
        data = {}
        sal = Salario.objects.all()
        for idx, s in enumerate(sal):
            data['fecha' + idx.__str__()] = s.fecha_deposito.year.__str__() + ' / ' + s.fecha_deposito.month.__str__()

        #print(data)
        #salario = serializers.serialize('json', Salario.objects.all())
        #ss = json.dumps(data)
        return data