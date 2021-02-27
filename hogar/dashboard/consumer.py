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
