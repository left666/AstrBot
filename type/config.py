VERSION = '3.3.8'

DEFAULT_CONFIG = {
    "qqbot": {
        "enable": False,
        "appid": "",
        "token": "",
    },
    "gocqbot": {
        "enable": False,
    },
    "uniqueSessionMode": False,
    "dump_history_interval": 10,
    "limit": {
        "time": 60,
        "count": 30,
    },
    "notice": "",
    "direct_message_mode": True,
    "reply_prefix": "",
    "baidu_aip": {
        "enable": False,
        "app_id": "",
        "api_key": "",
        "secret_key": ""
    },
    "openai": {
        "key": [],
        "api_base": "",
        "chatGPTConfigs": {
            "model": "gpt-4o",
            "max_tokens": 6000,
            "temperature": 0.9,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
        },
        "total_tokens_limit": 10000,
    },
    "qq_forward_threshold": 200,
    "qq_welcome": "",
    "qq_pic_mode": True,
    "gocq_host": "127.0.0.1",
    "gocq_http_port": 5700,
    "gocq_websocket_port": 6700,
    "gocq_react_group": True,
    "gocq_react_guild": True,
    "gocq_react_friend": True,
    "gocq_react_group_increase": True,
    "other_admins": [],
    "CHATGPT_BASE_URL": "",
    "qqbot_secret": "",
    "qqofficial_enable_group_message": False,
    "admin_qq": "",
    "nick_qq": ["/", "!"],
    "admin_qqchan": "",
    "llm_env_prompt": "",
    "llm_wake_prefix": "",
    "default_personality_str": "",
    "openai_image_generate": {
        "model": "dall-e-3",
        "size": "1024x1024",
        "style": "vivid",
        "quality": "standard",
    },
    "http_proxy": "",
    "https_proxy": "",
    "dashboard_username": "",
    "dashboard_password": "",
    "aiocqhttp": {
        "enable": False,
        "ws_reverse_host": "",
        "ws_reverse_port": 0,
    }
}