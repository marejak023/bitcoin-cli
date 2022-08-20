# bitcoin-cli
<p align="center">
  <img src="https://github.com/marejak023/bitcoin-cli/blob/main/logo.png">
</p>

<p align="center">
  <i>bitcoin-cli is a easy-to-use, free and open-source discord bot for bitcoin related commands</i>
</p>

## How to use
If you want to call an command, just use the prefix ```btc-cli!``` + ```command```, f.e. ```btc-cli! getdifficulty```. Simple as that!

### List of commands
Currently available commands are: </br>
getdifficulty, getblockcount, latesthash, btcperblock, totalbtc, probability, hashestowin, nextretarget,
avgtxsize, avgtxvalue, interval, eta, avgtxnumber

## TODO list
- [ ] Create/find someone with server/computer/RPi, where is downloaded Bitcoin Core, for being able to call commands (due to using the https://www.blockchain.com/api/q 
API, there is a GLOBAL 10 seconds cooldown). This is currently most important thing of the project since it is the biggest issue
- [ ] When calling commands, they are printed with unnecessary part, f.e. when calling ```btc-cli! getdifficulty```, the printed string is ```b'2.8351606743493E13'```. The b'' needs to be cutted out
- [ ] Add command for searching on the bitcoin wiki (https://en.bitcoin.it/wiki/Main_Page)
- [ ] Create a website
- [ ] Make new design
