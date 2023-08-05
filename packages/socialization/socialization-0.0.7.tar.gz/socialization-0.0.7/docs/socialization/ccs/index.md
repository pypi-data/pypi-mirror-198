Module socialization.ccs
========================

Sub-modules
-----------
* socialization.ccs.base_god_service
* socialization.ccs.base_goddess_service
* socialization.ccs.json_ws_active_service
* socialization.ccs.json_ws_passive_service
* socialization.ccs.wrapped_god_service
* socialization.ccs.wrapped_goddess_db_agent
* socialization.ccs.wrapped_goddess_service

Classes
-------

`BaseGodService()`
:   

    ### Ancestors (in MRO)

    * socialization.ccs.json_ws_active_service.JSONWebsocketActiveService

    ### Descendants

    * socialization.ccs.wrapped_god_service.WrappedGodService

    ### Methods

    `on_open(self, ws)`
    :

`BaseGoddessService(port=9000)`
:   

    ### Ancestors (in MRO)

    * socialization.ccs.json_ws_passive_service.JSONWebsocketPassiveService

    ### Descendants

    * socialization.ccs.wrapped_goddess_service.WrappedGoddessService

`JSONWebsocketActiveService()`
:   

    ### Descendants

    * socialization.ccs.base_god_service.BaseGodService

    ### Methods

    `create_connection(self, uri, on_open=None, on_message=None, on_error=None, on_close=None)`
    :

    `create_websocket(self, uri, on_open=None, on_message=None, on_error=None, on_close=None)`
    :

    `echo(self, ws, message)`
    :

    `on_close(self, ws, close_status_code, close_msg)`
    :

    `on_error(self, ws, error)`
    :

    `on_message(self, ws, message)`
    :

    `on_open(self, ws)`
    :

    `run(self)`
    :

`JSONWebsocketPassiveService(port=7654)`
:   

    ### Descendants

    * socialization.ccs.base_goddess_service.BaseGoddessService

    ### Methods

    `echo(self, ws, message)`
    :

    `get_server_coroutine(self)`
    :

`WrappedGodService(name='WrappedGodService')`
:   This is the wrapped God service.
    CCS provides a various of features for users in corresponding channels to use.

    ### Ancestors (in MRO)

    * socialization.ccs.base_god_service.BaseGodService
    * socialization.ccs.json_ws_active_service.JSONWebsocketActiveService

    ### Methods

    `add_feature(self, name, code, prompts, func=None)`
    :   Add a feature to the service.
        Every feature contains a name, a code and a prompt.
        The code is always a five-digited int, and the first number must be 9, like 90001.
        The prompt here will be replaced by "params" in the future.
        Now it's the string that shows to the user in the input bar.
        You do not need to specify a handler func to the feature, but it's recommended to do so.
        If one feature with no handler is triggered, an exception will be raised.
        You can use set_feature_handle to set a handler for a feature.

    `broadcast_command_image(self, data, ws, url)`
    :   Broadcast an image to all users in a channel.

    `broadcast_command_text(self, data, ws, text, clear=False)`
    :   Broadcast a text to all users in a channel.

    `on_open(self, ws)`
    :   Default behavior "on_open" for websocket.
        You can override this method to customize your own behavior.
        Also applies to "on_message", "on_error" and "on_close".

    `remove_feature(self, code)`
    :   Remove a feature from the service.
        The feature is specified by its code.

    `reply_command_image(self, data, ws, url)`
    :   Reply an image to a single user.

    `reply_command_text(self, data, ws, text, clear=False)`
    :   Reply a text to a single user.

    `run(self)`
    :   Run the service.

    `set_account(self, user_id, password)`
    :   Set the account for the service.
        Fetch these in CH0000.

    `set_basic_command_handle(self, code, func)`
    :   Set a handler for a basic command.
        The command is specified by its code.
        Some commands will be like "help", "quit".

    `set_feature_handle(self, code, func)`
    :   Set a handler for a feature.
        The feature is specified by its code.

    `set_message_handle(self, code, func)`
    :   Set a handler for a message.
        This code is always MESSAGE_TO_CCS.

    `set_notice_handle(self, code, func)`
    :   Set a handler for a notice.
        The notice is specified by its code.
        Some notices will be like "user joined the channel", "user left the channel".

    `whistle_sender_command_text(self, data, ws, *, text_to_sender, text_to_others, clear_sender=False, clear_others=False)`
    :   Dog whistle.

`WrappedGoddessDBAgent(path)`
:   

    ### Methods

    `add_whistle_msg(self, channel_id, msg, recipients)`
    :

    `get_channel_user_list(self, channel_id)`
    :

    `get_whistle_recipients(self, channel_id, msg)`
    :

    `init_dog_whistle(self, channel_id)`
    :

    `init_user_id_list(self, channel_id, user_ids)`
    :

    `join_channel(self, channel_id, user_id)`
    :

    `leave_channel(self, channel_id, user_id)`
    :

`WrappedGoddessService(port, uri, token, name='WrappedGoddessService')`
:   

    ### Ancestors (in MRO)

    * socialization.ccs.base_goddess_service.BaseGoddessService
    * socialization.ccs.json_ws_passive_service.JSONWebsocketPassiveService

    ### Methods

    `add_feature(self, name, code, prompts, func=None)`
    :

    `broadcast_command_image(self, channel_id, ws, url, clear=False)`
    :

    `broadcast_command_text(self, channel_id, ws, text, clear=False)`
    :

    `reply_command_text(self, data, ws, text, clear=False)`
    :

    `set_basic_command_handle(self, code, func)`
    :

    `set_feature_handle(self, code, func)`
    :

    `set_message_handle(self, code, func)`
    :

    `set_notice_handle(self, code, func)`
    :

    `whistle_sender_command_text(self, data, ws, *, text_to_sender, text_to_others, clear_sender=False, clear_others=False)`
    :