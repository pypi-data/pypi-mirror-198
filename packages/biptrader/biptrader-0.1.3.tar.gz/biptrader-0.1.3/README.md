## KuCoin

###  مستندات API
https://api-docs.wallex.ir/?python#

### احراز هویت و توکن
https://wallex.ir/app/my-account/settings

## Crypto Trading Bot

### Building a Basic Crypto Trading Bot in Python
https://medium.com/geekculture/building-a-basic-crypto-trading-bot-in-python-4f272693c375


* SimpleTradingBot
  git clone https://github.com/Lakshmi-1212/SimpleTradingBot.git
* Welcome to python-wazirx v1.0.0
  git clone https://github.com/WazirX/wazirx-connector-python.git
* CCXT – CryptoCurrency eXchange Trading Library
  pip install ccxt
* Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools":
  https://visualstudio.microsoft.com/visual-cpp-build-tools/
* TA-Lib Unofficial
* TA-Lib : Technical Analysis Library
  pip install ta-lib
  
# Commands
// pip install pipreqs
pipreqs .
export SETUP_VERSION="0.1"
export SETUP_LICENSE="MIT"
export SETUP_URL="https://github.com/adramazany/biptrader"
export SETUP_AUTHOR="Adel Ramezani"
export SETUP_AUTHOR_EMAIL="adramazany@gmail.com"
export SETUP_CLASSIFIERS="classifiers.txt"
export SETUP_DESCRIPTION="cryptocurrency trading helper library"
export SETUP_KEYWORDS="cryptocurrency kucoin technical-analysis"
export SETUP_LONG_DESCRIPTION="README.md"
export SETUP_INSTALL_REQUIRES="requirements.txt"
// pip install setuppy-generator
python3 -m setuppy_generator > setup.py
python3 setup.py sdist
twine upload dist/*
