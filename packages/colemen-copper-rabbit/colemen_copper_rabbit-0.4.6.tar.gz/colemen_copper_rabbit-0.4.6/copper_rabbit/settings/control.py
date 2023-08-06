



# ---------------------------------------------------------------------------- #
#                                 SERVER MODES                                 #
# ---------------------------------------------------------------------------- #

maintenance_mode:bool = False
'''If True, all API end points are blocked with a 503 (Service Unavailable) status code unless a bypass is provided.'''
coming_soon_mode:bool = False
'''If True, all API end points are blocked with a 503 (Service Unavailable) status code unless a bypass is provided.'''

retry_after_duration:int = 3600

bypass_name:str = "susurrus"
'''The name of the cookie/token that is used to bypass maintenance and coming_soon mode.'''


# ---------------------------------------------------------------------------- #
#                                    TOKENS                                    #
# ---------------------------------------------------------------------------- #

token_types = ["access","invitation"]
'''The token type names.'''

token_expiration = 3600
'''The time in seconds until a token will expire'''

token_secret = "N6SZxB3ORyrX?!&x34ODhud?$#V56o_T5mWDdZj3irx"
'''The token secret used for generating the signature'''

token_algorithm = "HS256"
'''The algorithm used for generating the token signature'''

token_issuer = "apricity"
'''The token issuer claim value.'''



test_mode:bool = True
log_to_console:bool = True


session_cookie_name = "aesopian"
session_header_name = "aesopian"


