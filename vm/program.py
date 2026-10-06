
# create vm private key
vmPrivateKey = int(open("/dev/random", "rb").read(32).hex(), 16)

longStandardPrime = 32317006071311007300338913926423828248817941241140239112842009751400741706634354222619689417363569347117901737909704191754605873209195028853758986185622153212175412514901774520270235796078236248884246189477587641105928646099411723245426622522193230540919037680524235519125679715870117001058055877651038861847280257976054903569732561526167081339361799541336476559160368317896729073178384589680639671900977202194168647225871031411336429319536193471636533209717077448227988588565369208645296636077250268955505928362751121174096972998068410554359584866583291642136218231078990999448652468262416972035911852507045361090559


#create vm public key
def make_public_key_from_vm_private_key(x, p):
        res = 1
        for bit in bin(x)[2:]:
                res = res * res % p
                if bit == "1":
                        res = res * 2 % p
        return res

vmPublicKey = make_public_key_from_vm_private_key(vmPrivateKey, longStandardPrime)
print("public key:", vmPublicKey)


# receive laptop public key
import socket
conn, _ = socket.create_server(("", 65535)).accept()
f = conn.makefile("rb")
laptopPublicKey = int(f.read(256).hex(), 16)


# create secret by merging laptop public key and vm private key
secret = pow(laptopPublicKey, vmPrivateKey, longStandardPrime)

# get video from laptop
encryptedVideo = f.read()
print(len(encryptedVideo))

# decrypt video using secret
import hashlib
keystream = hashlib.shake_256(str(secret).encode()).digest(len(encryptedVideo))
video = bytes(a ^ b for a, b in zip(encryptedVideo, keystream))
print(len(video))

# analyse video
import base64
videoText = base64.b64encode(video).decode()


# ask the llm about the video
import json
import urllib.request

while True:
        question = input("question: ")
        request = {
                "model": "Qwen/Qwen3.6-35B-A3B-FP8",
                "messages": [{"role": "user", "content": [
                        {"type": "video_url", "video_url": {"url": "data:video/mp4;base64," + videoText}},
                        {"type": "text", "text": question}]}],
                "max_tokens": 8000,
                "mm_processor_kwargs": {"fps": 1, "do_sample_frames": True},
        }
        req = urllib.request.Request("http://127.0.0.1:8000/v1/chat/completions",
                data=json.dumps(request).encode(), headers={"Content-Type": "application/json"})
        answer = json.load(urllib.request.urlopen(req))
        print(answer["choices"][0]["message"]["content"])