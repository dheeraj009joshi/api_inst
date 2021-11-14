from os import error
from instagrapi import Client
from flask import Flask,jsonify
import json
import random

# print('Login in..')

# def write_file(data, filename):
#     fh = open(filename, "w")
#     print("oppen file")
#     try:
#         fh.write(json.dumps(data))
#     finally:
#         fh.close()
        

# def read_file(filename):
#     fh= open(filename, "r")
#     return json.load(fh)



# ACCOUNT_USERNAME = 'dlovej009'
# ACCOUNT_PASSWORD = '12345678999'

# IG_CREDENTIAL = ACCOUNT_USERNAME
# # # IG_CREDENTIAL = random.choice(ACCOUNT_USERNAMES)
# print(IG_CREDENTIAL)
# cl = None

# try:
#     cl = Client(read_file(IG_CREDENTIAL))
#     print("valid credentials.json")

# except:
#     print("invalid credentials.json")

#     cl = Client()
#     print('done')
#     cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
#     print(cl)
    
#     print("valid login")
#     write_file(cl.get_settings(), IG_CREDENTIAL)
session_ids=[{'uuids': {'phone_id': '1270e408-8b9c-4fb8-891f-4e41422a14f3', 'uuid': 'f515e22c-8920-4c3f-adbf-081d6c86de5e', 'client_session_id': '29908170-d6b6-4e60-a757-48010a85a837', 'advertising_id': '4c2e1991-b359-494f-b17d-5a57d0d82bcc', 'android_device_id': 'android-48ddef64433b3198', 'request_id': '24573228-d889-4f27-85f8-41bbbeb39dcd', 'tray_session_id': '0ad06bb6-8e38-452b-8810-9b57616bf276'}, 'mid': 'YZEpxQABAAH7Jd4fanZauCbmgbQE', 'ig_u_rur': None, 'ig_www_claim': None, 'authorization_data': {'ds_user_id': '44806131974', 'sessionid': '44806131974%3Ae7uhx0tdYd2zDD%3A6', 'should_use_header_over_cookies': True}, 'cookies': {}, 'last_login': 1636903379.9740357, 'device_settings': {'app_version': '203.0.0.29.118', 'android_version': 26, 'android_release': '8.0.0', 'dpi': '480dpi', 'resolution': '1080x1920', 'manufacturer': 'Xiaomi', 'device': 'MI 5s', 'model': 'capricorn', 'cpu': 'qcom', 'version_code': '314665256'}, 'user_agent': 'Instagram 203.0.0.29.118 Android (26/8.0.0; 480dpi; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; en_US; 314665256)', 'country': 'US', 'country_code': 1, 'locale': 'en_US', 'timezone_offset': -14400},
             {'uuids': {'phone_id': 'bdc23f3a-d5a9-41f4-8ce0-680e53a82238', 'uuid': '58088265-9687-4da7-a153-2e548a86eb9e', 'client_session_id': 'b68c216f-c82e-4f77-9019-0e9db90f84d5', 'advertising_id': '3be90445-e75f-48d3-a180-54b83df768d5', 'android_device_id': 'android-2cc5c804af7843d7', 'request_id': 'a3cff3d2-108e-421d-9333-c2d11fd42f9d', 'tray_session_id': 'bb80d24b-31bd-4e80-966b-ed6c207a1087'}, 'mid': 'YZEqwAABAAFuM6TfHAq2A74uE5WJ', 'ig_u_rur': None, 'ig_www_claim': None, 'authorization_data': {'ds_user_id': '50103262815', 'sessionid': '50103262815%3AGTnGXflpojfziD%3A12', 'should_use_header_over_cookies': True}, 'cookies': {}, 'last_login': 1636903629.0919607, 'device_settings': {'app_version': '203.0.0.29.118', 'android_version': 26, 'android_release': '8.0.0', 'dpi': '480dpi', 'resolution': '1080x1920', 'manufacturer': 'Xiaomi', 'device': 'MI 5s', 'model': 'capricorn', 'cpu': 'qcom', 'version_code': '314665256'}, 'user_agent': 'Instagram 203.0.0.29.118 Android (26/8.0.0; 480dpi; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; en_US; 314665256)', 'country': 'US', 'country_code': 1, 'locale': 'en_US', 'timezone_offset': -14400},
             {'uuids': {'phone_id': '59763247-8e25-45c0-abcf-1f29f0e0a8dd', 'uuid': '2a933a6d-7627-4838-8ceb-24cbe026e369', 'client_session_id': 'e624cec9-d033-4a67-be62-d653d7c2aa9a', 'advertising_id': 'f8ac6406-53b5-417d-8fe7-b075390231cf', 'android_device_id': 'android-8e953cbf7b575a01', 'request_id': '830661b9-edc4-4b26-89a5-e4a5e7bbb5d4', 'tray_session_id': 'a5d60e34-dadb-4768-9b45-643e9eb81517'}, 'mid': 'YZEqzAABAAEVKoR6vGNAntozNWLd', 'ig_u_rur': None, 'ig_www_claim': None, 'authorization_data': {'ds_user_id': '50648708396', 'sessionid': '50648708396%3Ajfki66hFHeRMm5%3A1', 'should_use_header_over_cookies': True}, 'cookies': {}, 'last_login': 1636903638.9610536, 'device_settings': {'app_version': '203.0.0.29.118', 'android_version': 26, 'android_release': '8.0.0', 'dpi': '480dpi', 'resolution': '1080x1920', 'manufacturer': 'Xiaomi', 'device': 'MI 5s', 'model': 'capricorn', 'cpu': 'qcom', 'version_code': '314665256'}, 'user_agent': 'Instagram 203.0.0.29.118 Android (26/8.0.0; 480dpi; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; en_US; 314665256)', 'country': 'US', 'country_code': 1, 'locale': 'en_US', 'timezone_offset': -14400}]
app = Flask(__name__)

a=0
@app.route("/")
def index():
    try:
        return "Hello World!"
    except:
        return 'Please Connect to internet'
@app.route("/favicon.ico")
def index2():
    try:
        print('faviconn')
        return "favicon.ico"
    except:
        return 'Please Connect to internet'
# @app.route("/user/<username>")
# def user(username):
#     user_id = cl.user_id_from_username(username)
#     medias = cl.user_info(user_id).dict()
#     print(type(medias))
#     return medias
@app.route("/location/recent/<username>")
def loc_recent(username):
    global a
    cl=Client(session_ids[a])

    med=[]
    location_id = cl.fbsearch_places(username)[0].dict()["pk"]
    print(location_id)
    medias = cl.location_medias_recent(location_id,50)
    for i in medias:
        med.append(i.json())
    print(type(medias))
    a=a+1
    if a >=len(session_ids):
        a=0
    print(a)
    return str(med)
@app.route("/location/top/<username>")
def loc_top(username):
    global a
    cl=Client(session_ids[a])
    med=[]
    location_id = cl.fbsearch_places(username)[0].dict()["pk"]
    print(location_id)
    medias = cl.location_medias_top(location_id,50)
    for i in medias:
        med.append(i.json())
    
    if a >=len(session_ids):
        a=0
    print(a)
    return str(med)
    






if __name__ == '__main__': 
    # app.run(debug=True,port=8080)
    app.run(debug=True,host='172.31.85.28',port=8080)#  for server 





























# @app.route('/followers/<username>')
# def followers(username):  
   
    
#     user_id = cl.user_id_from_username(username)
#     medias = cl.user_followers(user_id)
#     medias=str(medias)
#     list=medias.replace("), 'media_type'","', 'media_type'")
#     list=list.replace('HttpUrl(','')
#     list=list.replace("='",":'")
#     list=list.replace(",'username'","','username'")
#     list=list.replace("UserShort(pk","UserShort{pk")
#     list=list.replace("pk=","pk:")
#     list=list.replace(",username","',username")
#     list=list.replace("stories=[])","stories=[]}")
#     list=list.replace("UserShort","")
#     list=list.replace(")","")
#     list=list.replace(", stories=[]","")
#     list=list.replace("full_name=","full_name:")
#     list=list.replace("'",'"')
#     list=list.replace(",",', "')
#     list=list.replace(":",'" :')
#     list=list.replace('"https" :','"https:')
#     list=list.replace('{','{"')
#     list=list.replace('_ ','_')
 
    
#     print(list)
#     data=json.loads(list)
#     temp = []
#     for t in data:
#         data[t].pop(" full_name",None)
#         data[t].pop(' scheme',None)
#         data[t].pop(' host',None)
#         data[t].pop(' tld',None)
#         data[t].pop(' host_type',None)
#         data[t].pop(' path',None)
#         data[t].pop(' query',None)
#         print(data[t])
#         print(type(data[t]))
#         print(type(data[t]))
#         temp.append(data[t])
#     return jsonify(temp) 



# @app.route('/following/<username>')
# def following(username): 
    
    
#     user_id = cl.user_id_from_username(username)
#     medias = cl.user_following(user_id)
#     medias=str(medias)
#     list=medias.replace("), 'media_type'","', 'media_type'")
#     list=list.replace('HttpUrl(','')
#     list=list.replace("='",":'")
#     list=list.replace(",'username'","','username'")
#     list=list.replace("UserShort(pk","UserShort{pk")
#     list=list.replace("pk=","pk:")
#     list=list.replace(",username","',username")
#     list=list.replace("stories=[])","stories=[]}")
#     list=list.replace("UserShort","")
#     list=list.replace(")","")
#     list=list.replace(", stories=[]","")
#     list=list.replace("full_name=","full_name:")
#     list=list.replace("{","{'")
#     list=list.replace(":","':")
#     list=list.replace('" ','" ')
#     json.dumps(list)
#     return list    

# @app.route("/hastag/top/<hastag>")
# def hastag_top(hastag):
    
#     medias = cl.hashtag_medias_top(str(hastag),50)
#     hastag=[]
#     for aap in medias:
#         data=aap.dict()
#         data.pop("caption_text",None)
#         print(data)
#         hastag.append(data)
#     list=str(hastag)
#     list=list.replace("), 'media_type'","', 'media_type'")
#     list=list.replace('HttpUrl(','')
    
    
   
    
#     json.dumps(hastag)
#     return hastag

# @app.route("/hastag/recent/<hastag>")
# def hastag_recent(hastag):
    
#     medias = cl.hashtag_medias_recent(str(hastag),50)
#     hastag=[]
#     for aap in medias:
#         data=aap.json()
#         print(data)
#         hastag.append(data)
#     hastag=str(hastag)
#     json.dumps(hastag)
#     return hastag


# @app.route("/stories/<username>")
# def user_stories(username):
    
#     user_id = cl.user_id_from_username(username)
#     data= cl.user_stories(user_id)
#     story=[]
#     for media in data:
#         media=media.json()
#         story.append(media)
#     list=str(story)
#     list=list.replace("'","")
#     list=list.replace("']","]")
#     json.dumps(list)

#     return list

# @app.route("/posts/<username>")
# def user_posts(username):
   
    
#     user_id = cl.user_id_from_username(username)
#     medias = cl.user_medias(user_id)
#     list=[]
#     for medis in medias:
#         # print(type(medias))
#         # print(type(medis))
#         data=medis.json()
#         # print(type(data))
#         dictiy=json.loads(data)
#         # print(type(dictiy))
#         dictiy.pop("caption_text", None)
#         data=json.dumps(dictiy)

#         list.append(data)
        
        
#     list=str(list)
    
#     list=list.replace("'","")
#     list=list.replace("']","]")
#     json.dumps(list)
#     return list


# @app.route("/media-comments/<media_id>")
# def media_comment(media_id):
    
#     medias = cl.media_comments(str(media_id))
#     list=[]
#     for i in medias:
#         comments=i.json()
#         print(comments)
#         list.append(comments)
#     list=str(list)
#     list=list.replace("'","")
#     list=list.replace("']","]")
#     json.dumps(list)
#     return list

# @app.route("/media-likes/<media_id>")
# def media_like(media_id):
    
#     medias = cl.media_likers(str(media_id))
#     list=[]
#     for i in medias:
#         comments=i.json()
#         print(comments)
#         list.append(comments)
#     list=str(list)
#     list=list.replace("\\", '')
#     list=list.replace("'","")
#     list=list.replace("']","]")
#     json.dumps(list)
#     return list
# @app.route('/me-not-following-back/<username>')
# def me_not_following_back(username):
   
#     user_id = cl.user_id_from_username(username)
#     followers=cl.user_followers(user_id)
#     following=cl.user_following(user_id)
#     data=[]
#     for items in followers:
#      if items not in following:
#         users=cl.user_info(items).json()
#         data.append(users)
#         print(users)
#     data=str(data)
#     list=data.replace("'","")
#     # list=list.replace("']","]")
#     json.dumps(list)  
#     return list

# @app.route('/they-not-following-back/<username>')
# def they_not_following_back(username):
    
#     user_id = cl.user_id_from_username(username)
#     followers=cl.user_followers(user_id)
#     following=cl.user_following(user_id)
#     data=[]
#     for items in following:
#      if items not in followers:
#         users=cl.user_info(items)
#         data.append(users)
#         print(users)
#     data=str(data)
#     list=data.replace("'","")
#     list=list.replace("']","]")
#     json.dumps(data)  
#     return data


