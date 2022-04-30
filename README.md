# Chat with Python File

![Security Checks](https://github.com/EpicGamerCodes/CTPF/actions/workflows/codeql-analysis.yml/badge.svg)

How to connect:

1) Connect to PublicServer
2) Enter hostname (user who has created the SSP)
3) Enter Server Access Code

## Notes

- A username is linked with the Windows Username, secondary preventing account creation.
- Each user can create a maximum of 3 chats (SSP's) and will be automaticly deleted if inactive by each Friday.
- Every Release is throughly checked for bugs and each commit for security issues.
- For bleeding edge builds, check out
- If you are not on the latest version, an alert will display, not allowing you to proceed with an older version.

## Commands

exit - Leaves the chat and exit the program
/reader - Open Reader Script
blacklist: - Prevent a user from a joining a chat (Disables whitelist)
whitelist: Allow only specific users to join a chat (Disables blacklist)
alert: Send an alert in the chat

## Wanings

By using this program, user data is collected for security of SSP's. User data is not used for any other reason.
If a critical change occours, on SSP load, the SSP will reset to prevent issues.
The creator of this program can broadcast a message across all active SSP's (If server is restarting or undergoing changes). Collected data: Windows Username

## Configs

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

Formation of PublicServer/{username}/{code}/config.json:

```json
{
    "perms": { - User permissions with chat
        "ExampleUser": { - User name
            "alert": true, - Alert command
            "blacklist": true, - Blacklist command
            "whitelist": true - Whitelist command
        }
    },
    "info": { - Chat version
        "creator": "ExampleUser", - Creator of chat
        "version": "1.0.0" - Version of config
    },
    "blacklist": [], - Users who are not allowed to join
    "whitelist": { - Whitelist dictionary
        "enabled": false, - If whitelist is Enabled
        "users": [] - Users who allowed to join
    }
}
```
