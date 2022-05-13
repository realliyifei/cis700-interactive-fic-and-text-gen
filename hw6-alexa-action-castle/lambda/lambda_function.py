# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

from utils import *
from game_utils import * 
from constants import *
from game_classes import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

game_state = None
END = False

def camel_case_split(s):
    words = [[s[0]]]
    for c in s[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)

    return ' '.join([''.join(word.lower()) for word in words])



class DirectionRequestHandler(AbstractRequestHandler):
    """Handler for Intent Direction."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        if ask_utils.get_intent_name(handler_input) in ["north", "south", "east", "west", "up", "down", "in", "out", "getIntoTimeMachine", "travelAugust", "travelJuly"]:
            return True
        else:
            return False 

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        """ The user wants to go in some direction """
        global game_state
        global END
        direction_dict = {"north": "north", 
                          "south": "south", 
                          "east": "east", 
                          "west": "west", 
                          "up": "up", 
                          "down": "down", 
                          "in": "in", 
                          "out": "out", 
                          "getIntoTimeMachine": "get into time machine", 
                          "travelAugust": "time travel to august", 
                          "travelJuly": "time travel to july"}
        direction =  direction_dict[ask_utils.get_intent_name(handler_input)]

        speak_output = direction
        if direction in game_state.curr_location.connections:
            if game_state.curr_location.is_blocked(direction, game_state):
                # check to see whether that direction is blocked.
                speak_output = game_state.curr_location.get_block_description(direction)
            else:
                # if it's not blocked, then move there 
                game_state.curr_location = game_state.curr_location.connections[direction]
                
                # If moving to this location ends the game, only describe the location
                # and not the available items or actions.
                if game_state.curr_location.get_property('end_game'):
                    speak_output = game_state.describe_current_location()
                else:
                    speak_output = game_state.describe()
        else:
            speak_output = "You can't go %s from here." % direction.capitalize() + ' ' + str(connections)
        
        END = game_state.curr_location.get_property('end_game')

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class InventoryRequestHandler(AbstractRequestHandler):
    """Handler for Intent Direction."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        if ask_utils.get_intent_name(handler_input) == 'inventory':
            return True
        else:
            return False 

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        """ The user wants to go in some direction """
        global game_state
        
        speak_output = 'check inventory'
        
        if len(game_state.inventory) == 0:
            speak_output = "You don't have anything."
        else:
            speak_output = ''
            descriptions = []
            for item_name in game_state.inventory:
                item = game_state.inventory[item_name]
                descriptions.append(item.description)
            speak_output += "You have: "
            speak_output += ', '.join(descriptions)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )  


class TakeRequestHandler(AbstractRequestHandler):
    """Handler for Intent Direction."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        if ask_utils.get_intent_name(handler_input).startswith('take'):
            return True
        else:
            return False 

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        """ The user wants to go in some direction """
        global game_state
        global END
        
        speak_output = 'hi'
        take_dict = {'takePhone': 'phone',
                     'takeDollar': 'dollar',
                     'takeAnotherDollar': 'another dollar',
                     'takeLightsaber': 'lightsaber',
                     'takeEmptyLightsaber': 'empty lightsaber',
                     'takeStunGun': 'stun gun',
                     'takeKey': 'key',
                     'takeKnife': 'knife'
        }
        try:
            # slot_item = camel_case_split(ask_utils.get_intent_name(handler_input).replace('take', ''))
            slot_item = take_dict[ask_utils.get_intent_name(handler_input)]
            # slot_item = ask_utils.request_util.get_slot_value(handler_input, 'take')
        except:
            speak_output = 'slot failed ' + ask_utils.get_intent_name(handler_input)
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )
        matched_item = False
        speak_output = slot_item
        
        # check whether any of the items at this location match the command
        for item_name in game_state.curr_location.items:
            if item_name == slot_item:
                item = game_state.curr_location.items[item_name]
                if item.get_property('gettable'):
                    game_state.add_to_inventory(item)
                    game_state.curr_location.remove_item(item)
                    speak_output = item.take_text
                    # end_game = item.end_game
                else:
                    speak_output = "You cannot take the %s." % item_name
                matched_item = True
                break
        # check whether any of the items in the inventory match the command
        if not matched_item:
            for item_name in game_state.inventory:
                if item_name in command:
                    speak_output = "You already have the %s." % item_name
                    matched_item = True
        # fail
        if not matched_item:
            speak_output = "You can't find %." % slot_item
        
        END = game_state.curr_location.get_property('end_game')

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class SpecialCommandRequestHandler(AbstractRequestHandler):
    """Handler for Intent Direction."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        if ask_utils.get_intent_name(handler_input) in ["talkSuzuha", "unlockDoor", "useGashaponMachine", 
                "hitDad", "stabDad", "scareDad", "swapUpa", "talkKurisu", "talkKurisuDad", "stunKurisu", 
                "useLightsaber", "endGame"]:
            return True
        else:
            return False 

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        """ The user wants to go in some direction """
        global game_state
        global END
        
        speak_output = 'hi'
        special_cmd_dict = {"talkSuzuha": "talk to suzuha", 
                            "unlockDoor": "unlock door", 
                            "useGashaponMachine": "use gashapon machine", 
                            "hitDad": "hit kurisu's dad", 
                            "stabDad": "stab kurisu's dad", 
                            "scareDad": "scare kurisu's dad away", 
                            "swapUpa": "swap upa", 
                            "talkKurisu": "talk to kurisu", 
                            "talkKurisuDad": "talk to kurisu's dad", 
                            "stunKurisu": "stun kurisu", 
                            "useLightsaber": "use lightsaber", 
                            "endGame": "check timeline (end game)"}
                            
        command = special_cmd_dict[ask_utils.get_intent_name(handler_input)].lower()
        speak_output = command
        for item in game_state.get_items_in_scope():
            special_commands = item.get_commands()
            for special_command in special_commands:
                if command == special_command.lower():
                    text, end = item.do_action(special_command, game_state)
                    speak_output = text
                    END = end_game
                    break
        
        # END = game_state.curr_location.get_property('end_game')

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global game_state
        global END
        
        game_state = build_game()
        # except:
        #     speak_output = "Problem in build game"
        END = False
        speak_output = "Welcome, to steins gate! " + game_state.describe()

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Add help instructions. "

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = game_state.describe()
        speech += 'intent: ' + ask_utils.get_intent_name(handler_input) + 'input: ' + handler_input

        return handler_input.response_builder.speak(speech).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input) or END==True

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.
        speak_output = 'Game has ended'

        return handler_input.response_builder.speak(speak_output).response



class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."  # + handler_input

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(DirectionRequestHandler())
sb.add_request_handler(TakeRequestHandler())
sb.add_request_handler(InventoryRequestHandler())
sb.add_request_handler(SpecialCommandRequestHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()