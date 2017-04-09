

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '198508248ade4986bf62870d1fc90299',
}

params = urllib.parse.urlencode({
})

def average (int_list):
    result = 0
    for i in int_list:
        result += i
    result = result / len(int_list)
    return result


list_of_pics = ['https://upload.wikimedia.org/wikipedia/commons/7/7f/Emma_Watson_2013.jpg',
                'http://cdnph.upi.com/svc/sv/upi/9611407252531/2014/1/d47b2139c479c116c9ac4e69fce6cb65/Emma-Watson-laughs-off-Turkish-politicians-claims-that-women-shouldnt-laugh-in-public.jpg',
                'http://unrealitymag.com/wp-content/uploads/2011/04/acid_picdump_011-465x611.jpg'
                ]

list_of_happy = []
list_of_angry = []
list_of_fear = []
list_of_disgust = []
list_of_sad = []
list_of_contempt = []
list_of_neutral = []
list_of_surprise = []

for pic in list_of_pics:
    body = "{ 'url': " + '"{}"'.format(pic) + "} "


    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read().decode("utf-8")
    
        d = json.loads(data)

        happy = d[0]['scores'].get('happiness')
        angry = d[0]['scores'].get('anger')
        fear = d[0]['scores'].get('fear')
        disgust = d[0]['scores'].get('disgust')
        sad = d[0]['scores'].get('sadness')
        contempt = d[0]['scores'].get('contempt')
        neutral = d[0]['scores'].get('neutral')
        surprise = d[0]['scores'].get('surprise')
        

        conn.close()

        list_of_happy.append(happy)
        list_of_angry.append(angry)
        list_of_fear.append(fear)
        list_of_disgust.append(disgust)
        list_of_sad.append(sad)
        list_of_contempt.append(contempt)
        list_of_neutral.append(neutral)
        list_of_surprise.append(surprise)
    
    
    except Exception as e:
        print(e.args)

list_of_emotion = [list_of_happy, list_of_angry, list_of_fear, list_of_disgust, list_of_sad, list_of_contempt, list_of_neutral, list_of_surprise]
i = 0
final_list = []
for i in range(len(list_of_emotion)-1):
    avg = average(list_of_emotion[i])
    final_list.append(avg)


emote_list = ["happy", "anger", "fear", "disgust", "sadness", "contempt", "neutral", "surprise"]
highest_mood = max(final_list)
mood_index = final_list.index(highest_mood)
print("Your most prominent mood is {} with a percentage of {}%!".format(emote_list[mood_index], highest_mood * 100))



