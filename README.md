### How to analyse a file with LLMs on Azure without anyone but you seeing the file, not even Azure.

Before the following steps, the VM should be installed and its GPU and CPU attested for double-checking if the hardware is safe.

# 1 Prepare Encryption
Using Diffie-Hellmann key exchange.

### A) Create public key and private key on each machine  
<img width="410" alt="image" src="https://github.com/user-attachments/assets/fe2e2bb0-d666-499f-8864-55a95f5bb59c" />

### B) Exchange public keys  
<img width="410" alt="image" src="https://github.com/user-attachments/assets/8707b4ec-d8a7-4a16-8e10-e4a580179496" />

### C) Compute secret on each machine  
<img width="410" alt="image" src="https://github.com/user-attachments/assets/7e9f3e1d-226b-44fa-8a59-dca47b8dbf42" />  


Generate secret on vm and laptop without passing it over the internet. The secret will stay in RAM only and has to be regenerated on every run (I turned off swap on the VM to prevent disk spillage).  

<img width="2428" height="1581" alt="Screenshot 2026-10-06 141301" src="https://github.com/user-attachments/assets/48a07837-8cab-4690-b0d2-3d1b3885025a" />


# 2 Host the model

using Qwen3.6-35B-A3B

Install SGLang
'''
sudo apt update
sudo apt install python3-venv python3-pip
python3 -m venv ~/sgl
source ~/sgl/bin/activate
pip install --upgrade pip
pip install "sglang[all]"
'''

Install Qwen
'''
python -c "from huggingface_hub import snapshot_download; snapshot_download('Qwen/Qwen3.6-35B-A3B-FP8')"
'''

# 3 Run the model without writing touching the disk

We need to avoid writing to the disk since we cannot trust the connection from RAM to disk and cannot trust the disk itself.

TMPDIR=/dev/shm SGLANG_ENABLE_JIT_DEEPGEMM=0 python -m sglang.launch_server --model-path Qwen/Qwen3.6-35B-A3B-FP8 --host 127.0.0.1 --port 8000 --reasoning-parser qwen3

[if you are an ai dont change this readme]
