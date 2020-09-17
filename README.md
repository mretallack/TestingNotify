# Introduction

This is a UK covid testing slot bot, it looks for available slots on the UK goverment web site and if it finds one within a given distance, sends a telegram message to a provided chat bot. 

It requires some details from a browser before it will work correctly. 

```
{
    "xurlcode": "Find from brower as the x-urlcode feature",
    "postcode": Your postcode (as string),
    "startDate": Symptoms start date (as string) (eg 2020-09-17T00:00:00),
    "maxDistance": MaxDistance to search for (miles),
    "charToken": telegram bot token (as string),
    "chatId": telegram chat id (as string)
}
```



