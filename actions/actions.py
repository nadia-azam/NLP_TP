# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions







from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from datetime import datetime
import re

class ActionSaveName(Action):

    def name(self) -> Text:
        return "action_save_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Récupérer le nom fourni par l'utilisateur depuis l'entité détectée
        name = tracker.latest_message.get('entities')[0]['value']

        # Sauvegarder le nom dans le slot "name"
        return [SlotSet("name", name)]
# This is a simple example for a custom action which utters "Hello World!"



class ActionConfirmerRendezvous(Action):

    def name(self) -> Text:
        return "action_save_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Récupérer le message de l'utilisateur
        message = tracker.latest_message.get('text')

        # Utiliser une expression régulière pour rechercher les dates dans le message
        dates = re.findall(r'\b\d{1,2}/\d{1,2}/\d{4}\b', message)

        if dates:
            # Prendre la première date trouvée (vous pouvez adapter cette logique selon vos besoins)
            disponibilite_date = datetime.strptime(dates[0], "%d/%m/%Y")

            # Construire la réponse de confirmation
            confirmation_message = f"Votre rendez-vous le {disponibilite_date.strftime('%d/%m/%Y')} a été confirmé."
        else:
            confirmation_message = "Je suis désolé, je n'ai pas réussi à extraire la date de votre message."

        dispatcher.utter_message(text=confirmation_message)

        return []


# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
