Module socialization.ccs.wrapped_god_service
============================================

Functions
---------

    
`handle_fetch_command(self, data, ws, path)`
:   A function that handles the "fetch command" notice.
    This can be the default behavior.

    
`handle_fetch_recipient_list(self, data, ws, path)`
:   

    
`handle_fetch_user_list(self, data, ws, path)`
:   A function that handles the "fetch user list" notice.
    This can be the default behavior.

    
`handle_join(self, data, ws, path)`
:   A function that handles the "user join" notice.
    This can be the default behavior.

    
`handle_left(self, data, ws, path)`
:   A function that handles the "user leave" notice.
    This can be the default behavior.

    
`handle_message(self, data, ws, path)`
:   A function that handles message to ccs.
    This can be the default behavior.
    When a message is sent, CCS will receive a response
    //TODO: describe later things, like what response and whistle parts
    def _send_message_down(self, ws, type_code, channel_id, to_user_ids, origin, **kwargs):

    
`handle_notice_release(self, data, ws, path)`
:   A function that handles the "release channel" notice.
    This can be the default behavior.

    
`handle_notice_take_over(self, data, ws, path)`
:   A function that handles the "take over channel" notice.
    This can be the default behavior.

    
`handle_receive_user_list(self, data, ws, path)`
:   A function that handles the "get user list" notice.
    This can be the default behavior.

Classes
-------

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