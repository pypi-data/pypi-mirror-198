Module socialization.bot.json_socket_user
=========================================

Classes
-------

`JSONSocketUser(path: str = None, reconnect: int = None, pre_analyse: bool = True)`
:   This is basic class of socket client user, which 
    implements fundamental interfaces that you can 
    reach as a user.
    We wraps the message data into a Message object.
    For better performance(not indeed), you could set
    `pre_analyse` to be `False` to get raw data of message(dict).

    ### Descendants

    * socialization.bot.base_bot.BaseBot

    ### Methods

    `create_connection(self, uri: str, on_open=None, on_message=None, on_error=None, on_close=None)`
    :   Initialize websocket connection between this user object itself and given server
        
        Args:
            Args:
            uri : str
                Location of server this user connects.
        
            on_open : function : optional
                Callback function execute when websocket connection is created.
                
            on_message : function : optional
                Callback function execute when receive message from websocket connection.
            
            on_error : function : optional
                Callback function execute when error occurs on websocket connection.
        
            on_close : function : optional
                Callback function execute when websocket connectoin breaks or closes.

    `on_close(self, ws, close_status_code, close_msg)`
    :   Default callback execute when connection is closed.
        As default, it would only print closure information.
        
        Args:
            ws : websocket.WebSocketApp
                Connection object
        
            close_status_code : str
                Status code of closure, more details refer to `https://websocket-client.readthedocs.io/en/latest`
        
            close_msg : str
                Information of closure.

    `on_error(self, ws, error)`
    :   Default callback execute when error occurs on connection.
        As default, it would only print error instead of raise an
        exception.
        Args:
            ws : websocket.WebSocketApp
                Connection object.
            
            error : exception object
                Object contains full information of the error.

    `on_message(self, ws, message)`
    :   Default callback when receive message from websocket connectoin.
        Don't override this function if you can't figure out what you would
        face to do so!
        
        Args:
            ws : websocket.WebSocketApp
                Connection object.
            
            message : str
                Message Object in utf-8 received from websocket connection.

    `on_open(self, ws)`
    :   Callback that is called when connection is open.
        As default it will only print message that bot opens.
        Args:
            ws : websocket.WebSocketApp
                Connection object.

    `on_receive_command(self, data)`
    :   Default callback that is called when receive command from connection.
        
        Args:
            data : dict
                Object of command.

    `on_receive_message(self, data)`
    :   Default callback that is called when receive message from connection.
        
        Args:
            data : Message
                Object of message.

    `on_receive_other(self, data)`
    :   Default callback that is called when receive something that is not command,
        message or status from connection.
        It always indicates error occurs on server end. As default, it will raise an 
        exception when called.
        Args:
            data : dict
                Object of received thing.

    `on_receive_status(self, data)`
    :   Default callback that is called when receive status from connection.
        
        Args:
            data : dict
                Object of status.

    `run(self)`
    :   Default function to startup a bot.
        Basically it will bind an rel to reconnect when stalled too long.
        Override this if you want to make some change before connection is
        created!