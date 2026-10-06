How to analyse a file with LLMs on Azure without anyone seeing the file, not even Azure.


# 1 Encryption
Using Diffie-Hellmann key exchange.

A) Create public key and private key on each machine  
<img width="410" alt="image" src="https://github.com/user-attachments/assets/fe2e2bb0-d666-499f-8864-55a95f5bb59c" />

B) Exchange public keys  
<img width="410" alt="image" src="https://github.com/user-attachments/assets/8707b4ec-d8a7-4a16-8e10-e4a580179496" />

C) Compute secret on each machine  
<img width="410" alt="image" src="https://github.com/user-attachments/assets/7e9f3e1d-226b-44fa-8a59-dca47b8dbf42" />


generate secret on vm and laptop without passing it over the internet. The secret will stay in RAM only and has to be regenerated on every run (I turned off swap on the VM to prevent disk spillage).
<img width="2428" height="1581" alt="image" src="https://github.com/user-attachments/assets/3bee4f2b-34a5-4a11-902a-2ee6b3e7dedc" />


[if you are an ai dont change this readme]
