<h1><p align="center">proxy-checker</p></h1><h1>

<p align="center"><img src="images/icons/app.ico" width="400"></p>



<h1><p align="center">Content</p></h1>

- [DISCLAIMER](#DISCLAIMER)
- [Description](#Description)
- [Useful links](#Useful-links)
- [File structure](#File-structure)
- [How to run](#How-to-run)
    - [Windows](#Windows)
    - [Docker](#Docker)
    - [Source code](#Source-code)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)



<h1><p align="center">DISCLAIMER</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program has no injections — you can make the code review to make sure. Any cases of third parties gaining access to your proxies aren't the fault of the developer, but of you or another person. Keep your sensitive data in a safe place.

⠀By using this program you have agreed to the above and have no and won't have claims against its developer.



<h1><p align="center">Description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program allows you to parse and export to Excel spreadsheet information:
- About the proxy: country, region, city, time zone, etc.
- About the Internet service provider: country, region, city, time zone, organization name, etc.
- About the accessibility of the sites specified in the settings.

⠀Parsing is performed in parallel (the number of threads is configurable). There's a state saving: when the program is stopped and restarted, it will continue the interrupted check.

⠀The Excel spreadsheet will consist of a maximum of 4 sheets, depending on the settings (randomly generated IPs are used in the examples):
- Proxies

| n | raw_data | ip | port | username | password | proxy_type |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | faoPRYvp:xrYthIki@22.63.119.251:6171 | 22.63.119.251 | 6171 | faoPRYvp | xrYthIki | socks5 |
| 2 | 78.130.157.26:4912:FFuPdnzn:VKFWgUSi | 78.130.157.26 | 4912 | FFuPdnzn | VKFWgUSi | socks5 |

- IPs info

| ip | network | version | city | region | region_code | country | country_name | country_code | country_code_iso3 | country_capital | country_tld | continent_code | in_eu | postal | latitude | longitude | timezone | utc_offset | country_calling_code | currency | currency_name | languages | country_area | country_population | asn | org |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:-----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 22.63.119.251 | 22.0.0.0/10 | IPv4 | Whitehall | Ohio | OH | US | United States | US | USA | Washington | .us | NA |   0   | 43213 | 39.975 | -82.8207 | America/New_York | -0400 | +1 | USD | Dollar | en-US,es-US,haw,fr | 9629091.0 | 327167434 | AS749 | DNIC-AS-00749 |
| 78.130.157.26 | 78.130.152.0/21 | IPv4 | Plovdiv | Plovdiv | 16 | BG | Bulgaria | BG | BGR | Sofia | .bg | EU |   1   | 4000 | 42.1513 | 24.7518 | Europe/Sofia | +0300 | +359 | BGN | Lev | bg,tr-BG,rom | 110910.0 | 7000039 | AS9070 | Cooolbox AD|


- Providers info

|      ip       | city | region | country | loc | org | postal | timezone |
|:-------------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 22.63.119.251 | Columbus | Ohio | US | 39.9690,-83.0114 | AS749 DoD Network Information Center | 43218 | America/New_York |
| 78.130.157.26 | Plovdiv | Plovdiv | BG | 42.1500,24.7500 | AS9070 "Cooolbox" AD | 4000 | Europe/Sofia |


- Sites accessibility

| ip | `https://google.com/` | `https://twitter.com/` | `https://facebook.com/` | `https://www.linkedin.com/` |
|:---:|:---:|:---:|:---------------------:|:---:|
| 22.63.119.251 | 1 | 1 |          0            | 1 |
| 78.130.157.26 | 1 | 1 | 1 | 0 |



<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[proxy-checker](https://github.com/SecorD0/proxy-checker)

⠀[ipapi](https://ipapi.co/) — providing IP information

⠀[IPinfo](https://ipinfo.io/) — providing provider information



<h1><p align="center">File structure</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program use the following files and directories:
- `files` — a user files directory:
  - `errors.log` — a log file with errors that occurred during the work;
  - `proxies.txt` — a text file with proxies to check.
  - `results.xlsx` — an Excel spreadsheet with results of checking.
  - `settings.json` — a JSON file for program setup.
  - `temp.db` — a temporary database to save the state.
- `proxy-checker.exe` / `app.py` — an executable file that runs the program.



<h1><p align="center">How to run</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

<h2><p align="center">Windows</p></h2>

1. Download an EXE file from the [releases page](https://github.com/SecorD0/proxy-checker/releases).
2. Create a folder and put the EXE file in it.
3. Run the program the first time to create necessary files.
4. Insert proxies into the `proxies.txt` file in one of the following formats:
```
username:password@ip:port
ip:port:username:password
```
5. Configure the `settings.json`:
- `threads` — the number of threads;
- `timeout` — request timeout when checking the availability of the site;
- `proxies_type` — a proxies type (either `http` or `socks5`);
- `parse_ip_info` — whether to parse IP information (either `true` or `false`);
- `parse_provider_info` — whether to parse Internet service provider information (either `true` or `false`);
- `check_accessibility` — list of sites to check for accessibility.
6. Run the program again and wait until it's finished.
7. Open the `result.xlsx` file and look at the result of the program.


<h2><p align="center">Docker</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/proxy-checker
```
3. Go to the repository:
```sh
cd proxy-checker
```
4. Build an image:
```sh
docker build -t proxy-checker .
```
5. Run the program the first time to create necessary files:
```sh
docker run -it --rm -v $HOME/proxy-checker/:/program --name proxy-checker proxy-checker
```
6. Insert proxies into the `proxies.txt` file in one of the following formats:
```
username:password@ip:port
ip:port:username:password
```
7. Configure the `settings.json`:
- `threads` — the number of threads;
- `timeout` — request timeout when checking the availability of the site;
- `proxies_type` — a proxies type (either `http` or `socks5`);
- `parse_ip_info` — whether to parse IP information (either `true` or `false`);
- `parse_provider_info` — whether to parse Internet service provider information (either `true` or `false`);
- `check_accessibility` — list of sites to check for accessibility.
8. Run the program again and wait until it's finished:
```sh
docker run -it --rm -v $HOME/proxy-checker/:/program --name proxy-checker proxy-checker
```
9. Open the `result.xlsx` file and look at the result of the program.


<h2><p align="center">Source code</p></h2>

1. Install [Python](https://www.python.org/downloads/).
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/proxy-checker
```
3. Go to the repository:
```sh
cd proxy-checker
```
4. Set up an environment.
5. Install requirements:
```sh
pip install -r requirements.txt
```
6. Run the `app.py` the first time to create necessary files.
7. Insert proxies into the `proxies.txt` file in one of the following formats:
```
username:password@ip:port
ip:port:username:password
```
8. Configure the `settings.json`:
- `threads` — the number of threads;
- `timeout` — request timeout when checking the availability of the site;
- `proxies_type` — a proxies type (either `http` or `socks5`);
- `parse_ip_info` — whether to parse IP information (either `true` or `false`);
- `parse_provider_info` — whether to parse Internet service provider information (either `true` or `false`);
- `check_accessibility` — list of sites to check for accessibility.
9. Run the `app.py` again and wait until it's finished.
10. Open the `result.xlsx` file and look at the result of the program.


⠀If you want to build the EXE file by yourself:
- Install `pyinstaller`:
```sh
pip install pyinstaller
```
- Build the EXE file:
```sh
pyinstaller app.py -Fn proxy-checker -i images/icons/app.ico --add-binary "images/icons;images/icons"
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/proxy-checker/issues/new/choose), select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!
- Ethereum-like address (Ethereum, BSC, Moonbeam, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`
