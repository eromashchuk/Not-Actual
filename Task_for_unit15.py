# ''' 1. Напишите программу, которая получает от пользователя имя файла,
#    открывает этот файл в текущем каталоге,
#    читает его
#    и выводит два слова:
#       - наиболее часто встречающееся из тех, что имеют размер более трех символов,
#       - и наиболее длинное слово на английском языке.'''
#
# def changeText(text):
#     for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
#         text = text.replace(i, '')
#
#     return text.split()
#
# def mostCommon(text, length = 0):
#     most_common = []
#     qty_most_common = 0
#
#     for item in text:
#         if len(item) > length:
#             qty = text.count(item)
#             if qty > qty_most_common and qty > 2:
#                 qty_most_common = qty
#                 most_common = [item]
#             elif qty == qty_most_common:
#                 most_common.append(item)
#
#     return list(set(most_common))
#
# def mostLength(text):
#     most_length = []
#     qty_most_length = 0
#     alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for item in text:
#         for char in item:
#             if char not in alphabet:
#                 charEn = False
#             else:
#                 charEn = True
#
#         if charEn:
#             qty = len(item)
#             if qty > qty_most_length:
#                 qty_most_length = qty
#                 most_length = [item]
#             elif qty == qty_most_length:
#                 most_length.append(item)
#
#     return list(set(most_length))
#
#
# nameFile = input('Название файла: ')
#
# with open(nameFile, encoding='utf8') as f:
#     fileText = f.read()
#
# fileText = changeText(fileText)
# print(f'Список самых частых слов длинной более трёх символов: {mostCommon(fileText, 3)}')
# print(f'Список самых длинных английских слов: {mostLength(fileText)}')

''' '''

class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]

for event in events:
    event_obj = Event(timestamp=event.get('timestamp'),
                      event_type=event.get('type'),
                      session_id=event.get('session_id'))
    print(event_obj.timestamp)