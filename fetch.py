
import urllib3
import json
import requests

with open('settings.json') as json_file:
    settings = json.load(json_file)


def telegram_bot_sendtext(bot_message):
    
    send_text = 'https://api.telegram.org/bot' + settings["charToken"] + '/sendMessage?chat_id=' + settings["chatId"] + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()




body= {"topLevelTestCentreId":"CVD19","postcode":"BH20 6JF","testCentreGroupIds":["GR_RTS","GR_STS","GR_MTU"],"startDate":"2020-09-17T00:00:00","numberOfDays":5,"appointmentTypeCode":"ATCOM05","paging":{"currentPage":1,"pageSize":3}}


encoded_body = json.dumps(body)

headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-GB,en;q=0.5",
        "x-urlcode": "WI1DLV4Q5LXFTVV5",
        "Content-Type": "application/json",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }


http = urllib3.PoolManager()

r = http.request('POST', 'https://ads-prd-gov-1-sp.test-for-coronavirus.service.gov.uk/testcentres/availabilityquery',
                 headers=headers,
                 body=encoded_body)

body=r.data.decode("utf-8")

json_body= json.loads(body)


for testCenter in json_body["testCentres"]:
    distance =int(testCenter["geolocation"]["distance"])
    testCenterName = testCenter["testCentre"]["displayName"]
    
    if distance<settings["maxDistance"]:

        message = "Test available "+str(distance)+" miles, "+testCenterName 
    
        telegram_bot_sendtext(message)





