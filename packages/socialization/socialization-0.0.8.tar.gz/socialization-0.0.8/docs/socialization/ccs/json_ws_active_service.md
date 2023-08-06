Module socialization.ccs.json_ws_active_service
===============================================

Classes
-------

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