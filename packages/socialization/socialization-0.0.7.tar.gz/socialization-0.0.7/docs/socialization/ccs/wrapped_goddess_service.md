Module socialization.ccs.wrapped_goddess_service
================================================

Functions
---------

    
`handle_command_fetch_cmd_list(self, data, ws, path)`
:   

    
`handle_command_fetch_recipient_list(self, data, ws, path)`
:   

    
`handle_command_fetch_user_list(self, data, ws, path)`
:   

    
`handle_fetch_command(self, data, ws, path)`
:   

    
`handle_join(self, data, ws, path)`
:   

    
`handle_notice_auth_token(self, data, ws, path)`
:   

    
`handle_notice_release(self, data, ws, path)`
:   

    
`handle_notice_take_over(self, data, ws, path)`
:   

    
`handle_notice_user_joined(self, data, ws, path)`
:   

Classes
-------

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