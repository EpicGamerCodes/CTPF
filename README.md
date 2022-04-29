# How this works (PublicServer Example)

![Security Checks](https://github.com/EpicGamerCodes/CWPF/actions/workflows/codeql-analysis.yml/badge.svg)

How to connect:

1) Connect to PublicServer
2) Enter hostname (user who has created the SSP)
3) Enter Server Access Code

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
