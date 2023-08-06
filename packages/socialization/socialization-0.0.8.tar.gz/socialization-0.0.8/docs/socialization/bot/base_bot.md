Module socialization.bot.base_bot
=================================

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