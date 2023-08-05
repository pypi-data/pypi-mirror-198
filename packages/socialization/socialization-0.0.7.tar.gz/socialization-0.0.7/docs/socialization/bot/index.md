Module socialization.bot
========================

Sub-modules
-----------
* socialization.bot.base_bot
* socialization.bot.json_socket_user
* socialization.bot.message

Classes
-------

`BaseBot(user_id: str, password: str, path: str = None, reconnect: int = None, pre_analyse: bool = True)`
:   This is the base of bot, deriving from which you can define automation of 
        all behavior that a bot will abey. 
        For basic use, what you need to do is only overriding `on_receive_message`
        to define the behaviour when receive a message. For example, you
        are definately allowed to broadcast the message to everyone in the channel 
        where you receive it by overriding `on_receive_message` and call 
        `send_message` with message you received send it to all users in the channel.
    
        We wraps the message data into a Message object.
    For better performance(not indeed), you could set
    `pre_analyse` to be `False` to get raw data of message(dict).
        
    
    Initialize a Bot instance.
    
    Args:
            user_id : str
                    User ID of the account you wanna set as a bot.
            password : str
                    Password of that account referred above.
            path : str : optional
                    Location of server the bot will be running on.
            reconnect : int : optional
                    Max pending time for stalling. Reconnection will launch if stalls
                    outlong this time.
            pre_analyse : bool : optional
                    Trigger for pre-analysing message by wrapping it into a Message object.
                    If turned off, data param in on_receive_data() will be raw dict!

    ### Ancestors (in MRO)

    * socialization.bot.json_socket_user.JSONSocketUser

    ### Methods

    `create_channel(self, channel_id)`
    :   Wrapped create channel function. Call this to create channel.
        If you wanna customize create channel behaviour, call
        `_command_create_channel()` to send command to create channel.
        
        Args:
                channel_id : str
                        ID of the new channel.

    `fetch_bot_channels(self)`
    :   Wrapped fetch bot channels function. Call this to fetch bot channels.
        If you wanna customize fetch bot channels behaviour, call
        `_command_fetch_user_channels()` to send command to fetch bot channels.

    `fetch_channel_command_list(self, channel_id)`
    :   Wrapped fetch channel cmd list function. Call this to fetch channel cmd list.
        If you wanna customize fetch channel cmd list behaviour, call
        `_command_fetch_channel_command_list()` to send command to fetch channel cmd list.
        
        Args:
                channel_id : str
                        ID of the channel to fetch command list.

    `fetch_offline_message(self)`
    :   Wrapped fetch ofl-message function. Call this to fetch ofl-message.
        If you wanna customize fetch ofl-message behaviour, call
        `_command_fetch_offline_message()` to send command to fetch ofl-message.

    `fetch_recipients(self, message_id)`
    :   Wrapped fetch recipients function. Call this to fetch recipients of 
        a certain message. If you wanna customize fetch recipients behaviour, 
        call `_command_fetch_recipients()` to send command to fetch recipients.
        
        Args:
                message_id : str
                        ID of the message to look up for recipients.

    `join_channel(self, channel_id: str)`
    :   Wrapped join channel function. Call this to join channel.
        If you wanna customize join channel behaviour, call
        `_command_join_channel()` to send command to join channel.
        
        Args:
                channel_id : str
                        ID of channel to join.

    `leave_channel(self, channel_id: str)`
    :   Wrapped leave channel function. Call this to leave channel.
        If you wanna customize leave channel behaviour, call
        `_command_leave_channel()` to send command to leave channel.
        
        Args:
                channel_id : str
                        ID of channel to leave.

    `login(self)`
    :   Wrapped login function. Call this to login.
        If you wanna customize login behaviour, call
        `_command_login()` to send command to login.

    `logout(self)`
    :   Wrapped logout function. Call this to logout.
        If you wanna customize logout behaviour, call
        `_command_logout()` to send command to logout.

    `on_close(self, ws, close_status_code, close_msg)`
    :   Behaviour at the time websocket connection is closed.
        
        Args:
                ws : websocket.WebSocketApp
        Connection object.

    `on_error(self, ws, error)`
    :   Behaviour at the time error occur on websocket connection.
        
        Args:
                ws : websocket.WebSocketApp
        Connection object.

    `on_message(self, ws, message)`
    :   Behaviour at the time receive message from websocket connection.
        
        Warning:
                Do not re-write this if you have no idea what will happen!
        
        Args:
                ws : websocket.WebSocketApp
        Connection object.
                message : jstr
                        Raw message json string from ws connection.

    `on_open(self, ws)`
    :   Behaviour at the time websocket connection is created.
        
        Args:
                ws : websocket.WebSocketApp
        Connection object.

    `on_receive_command(self, data)`
    :   Behaviour when receives commands from server(4xxxx).
        It's crucial for keeping channel_list up to date. If
        you want to customize the behaviour, please **call**
        **super().on_receive_command** to keep those properties.
        
        Args:
                data : dict
                        WS data in the format definde by `codes.md`

    `on_receive_message(self, data)`
    :   Behaviour when receives message from server(3xxxx).
        Override this to customize what to do when receives
        a message!
        
        Args:
                data : dict || Message
                        Wrapped Message object of message received.
                        If pre-analyse is turned off, it would be 
                        raw WS data in the format definde by `codes.md`

    `on_receive_status(self, data)`
    :   Behaviour when receives status from server(6xxxx).
        
        By default, we would update channel_list and user_list
        on sereval cases. Therefore, if you want to customize
        behaviour receive status while keeping these properties
        up to date, override this function and **call**
        **super().on_receive_status** to keep them.
        
        Args:
                data : dict
                        WS data in the format definde by `codes.md`

    `register(self, email: str, password: str)`
    :   Wrapped register function. Call this to register.
        If you wanna customize register behaviour, call
        `_command_register()` to send command to register.
        
        Args:
                email : str
                        Email to register an account.
                password : str
                        Password for that new account.

    `reset_password(self, email: str, password: str)`
    :   Wrapped reset password function. Call this to reset password.
        If you wanna customize reset password behaviour, call
        `_command_reset_password()` to send command to reset password.
        
        Args:
                email : str
                        Email of the account to reset pw.
                password : str
                        New password for that account.

    `run(self)`
    :   Behaviour to run bot. 
        By default, it will login and update several properties
        of bot like channel_list .etc. Then it will hang this
        process up and reconnect when error occurs.
        
        Warning:
                Don't re-write this if you have no idea what will happen!

    `send_message(self, message: socialization.bot.message.Message)`
    :   Wrapped send message function. Call this to send message.
        If you wanna customize send message behaviour, call
        `_command_send_message()` to send command to send message.
        
        Args:
                message : Message
                        Wrapped message object contains message body, receivers,
                        target channel and sender information.

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

`Message(type: socialization.bot.message.MessageType, body=None, channel: str = '', to: list = [], sender: str = '', recipient_count: int = 0, id: str = '', origin: str = 'Bot', raw=None)`
:   

`MessageType(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   This is enumeration of message types.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `FILE`
    :

    `IMAGE`
    :

    `TEXT`
    :