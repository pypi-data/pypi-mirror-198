"""

    MIT License

    Copyright (c) 2019 Paul Antony

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""


import json
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'
}


def getPeriodTrend(scripCode, timePeriod):

    assert timePeriod in ['1M', '3M', '6M', '12M'], "timePeriod should be one of the following options '1M', '3M', '6M' and '12M'"

    baseurl = '''https://api.bseindia.com/BseIndiaAPI/api/StockReachGraph/w?'''
    URL = baseurl + '''scripcode={}&flag={}&fromdate=&todate=&seriesid='''.format(scripCode, timePeriod)
    res = requests.get(URL, headers=headers)

    # extracting the data from the response
    data = json.loads(res.content.decode('utf-8'))
    data = json.loads(data['Data'])

    # formating the data
    res = [{'date': x['dttm'], "value": float(x['vale1']), "vol": int(x['vole'])} for x in data]

    return res
