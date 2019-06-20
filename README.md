# Creates XEL wallet vanity addresses

## Install python 
```
sudo apt-get update
```
```
sudo apt-get install python3.6
```
## Install python pip 

```
sudo apt install python3-pip
```
## Make xel.py executible 

```
sudo chmod +x xel.py
```

## Run it 

```
sudo ./xel.py
```

## Change Prefix 

```
poss = ['1337', '1337-H4X0R']
```
Change to what you want to have , for example  `KING` . You can have as meny as you want , bear in mind search will take some time . 

## Change node 
```
url_pw = 'http://localhost:17876/nxt?=%2Fnxt&requestType=getAccountId&secretPhrase={}'
url_bal = 'http://localhost:17876/nxt?=%2Fnxt&requestType=getBalance&account={}'
```
change node to external one if you like to for examlpe 

```
url_pw = 'http://testnet-01.xel.org:16876/nxt?=%2Fnxt&requestType=getAccountId&secretPhrase={}'
url_bal = 'http://testnet-01.xel.org:16876/nxt?=%2Fnxt&requestType=getBalance&account={}'
```
## change secret ke simbols as you please if you dont trust ones in the code 

```
BASE58 = '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
```
For example

```
BASE58 = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ'
```


