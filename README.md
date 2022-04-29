# How this works (PublicServer Example)

1) Connects to PublicServer
2) Creates a Server Storage Port using username
3) Server Access code is made

How to connect:

1) Connect to PublicServer
2) Enter your username
3) Enter hostname (user who has created the SSP)
4) Enter Server Access Code

WARNINGS:
By using this program, user data is collected for security of SSP's. User data is not used for any other reason.
If a critical change occours, on SSP load, the SSP will reset to prevent issues.
The creator of this program can broadcast a message across all active SSP's (If server is restarting or undergoing changes).

Formation of PublicServer/config.json:

```json
 {
    "status": { - Status of Server
        "online": true, - Online / Offline
        "reason": "Online", - Reason for being Online / Offline
        "eta": 0 - Time until Online
    },

    "banned": { - Banned users
        "users": [] - List of banned users
    },

    "users": { - Users
        "ExampleUser": ["EpicGamer", 0] - Name: nickname, number of chats
    }
}
```
