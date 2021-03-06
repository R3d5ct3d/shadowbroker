# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: types.py
from types import *
SOCKET_TYPE_UNKNOWN = 0
SOCKET_TYPE_TCP = 1
SOCKET_TYPE_UDP = 2
RAW_TYPE_DATA = 0
RAW_TYPE_COMMAND = 1
RAW_COMMAND_DISCONNECT = 1
NOTIFY_CONNECT_SUCCESS = 0
NOTIFY_CONNECT_REFUSED = 1
NOTIFY_CONNECT_UNREACH = 2
NOTIFY_CONNECT_TIMEOUT = 3
NOTIFY_CONNECT_FAILED = 4
MSG_KEY_PARAMS_COMMON = 65536
MSG_KEY_PARAMS_COMMON_CMD_ID = 65537
MSG_KEY_PARAMS_COMMON_STATUS_ADDRESS = 65538
MSG_KEY_PARAMS_STANDARD = 131072
MSG_KEY_PARAMS_STANDARD_SOCKET_TYPE = 131073
MSG_KEY_PARAMS_STANDARD_FLAGS = 131074
MSG_KEY_PARAMS_STANDARD_MAX_RECV_SIZE = 131075
MSG_KEY_PARAMS_LISTEN = 196608
MSG_KEY_PARAMS_LISTEN_COMMON = 196609
MSG_KEY_PARAMS_LISTEN_STANDARD = 196610
MSG_KEY_PARAMS_LISTEN_CONNECT_ADDRESS = 196611
MSG_KEY_PARAMS_LISTEN_CONNECT_SOCKET_TYPE = 196612
MSG_KEY_PARAMS_LISTEN_LISTEN_PORT = 196613
MSG_KEY_PARAMS_LISTEN_MAX_CONNECTIONS = 196614
MSG_KEY_PARAMS_LISTEN_TARGET_DST_PORT = 196615
MSG_KEY_PARAMS_LISTEN_TARGET_SRC_PORT = 196616
MSG_KEY_PARAMS_LISTEN_LISTEN_BIND_ADDR = 196617
MSG_KEY_PARAMS_LISTEN_TARGET_ADDR = 196618
MSG_KEY_PARAMS_LISTEN_TARGET_SRC_ADDR = 196619
MSG_KEY_PARAMS_LISTEN_LIMIT_ADDR = 196620
MSG_KEY_PARAMS_LISTEN_LIMIT_MASK = 196621
MSG_KEY_PARAMS_LISTEN_ENABLE_PORT_SHARING = 196622
MSG_KEY_PARAMS_LISTEN_CLIENT_SRC_PORT = 196623
MSG_KEY_PARAMS_LISTEN_CLIENT_SRC_ADDR = 196624
MSG_KEY_PARAMS_CONNECT = 262144
MSG_KEY_PARAMS_CONNECT_COMMON = 262145
MSG_KEY_PARAMS_CONNECT_STANDARD = 262146
MSG_KEY_PARAMS_CONNECT_SOCKET_INDEX = 262147
MSG_KEY_PARAMS_CONNECT_DST_PORT = 262148
MSG_KEY_PARAMS_CONNECT_SRC_PORT = 262149
MSG_KEY_PARAMS_CONNECT_TARGET_ADDR = 262150
MSG_KEY_PARAMS_CONNECT_TARGET_SRC_ADDR = 262151
MSG_KEY_COMMAND_CONNECT = 327680
MSG_KEY_COMMAND_CONNECT_COMMON = 327681
MSG_KEY_COMMAND_CONNECT_CMD_ID = 327682
MSG_KEY_COMMAND_CONNECT_REQUEST_SOCKET_INDEX = 327683
MSG_KEY_COMMAND_CONNECT_REMOTE_SOCKET_INDEX = 327684
MSG_KEY_COMMAND_CONNECT_ERROR_MODULE = 327685
MSG_KEY_COMMAND_CONNECT_ERROR_OS = 327686
MSG_KEY_COMMAND_STOP_ALL = 458752
MSG_KEY_COMMAND_STOP_ALL_COMMON = 458753
MSG_KEY_STATUS_ERROR = 524288
MSG_KEY_STATUS_ERROR_ERROR_MODULE = 524289
MSG_KEY_STATUS_ERROR_ERROR_OS = 524290
MSG_KEY_STATUS_CONNECTION = 589824
MSG_KEY_STATUS_CONNECTION_TYPE = 589825
MSG_KEY_STATUS_CONNECTION_SOCKET_TYPE = 589826
MSG_KEY_STATUS_CONNECTION_LOCAL_ADDR = 589827
MSG_KEY_STATUS_CONNECTION_LOCAL_PORT = 589828
MSG_KEY_STATUS_CONNECTION_REMOTE_ADDR = 589829
MSG_KEY_STATUS_CONNECTION_REMOTE_PORT = 589830
MSG_KEY_STATUS_CONNECTION_SOCKET_ERROR = 589831