

import operator


portfolio = {
    'accounts': ['SBI', 'IOB'],
    'shares': ['HDFC', 'ICICI', 'TM', 'TCS'],
    'ornaments': ['10gm gold', '1 kg silver']

}

portfolio['MF'] = ['Relaince', 'ABSL']
print(portfolio)
portfolio['accounts'] = ['Axis', 'BOB']
print(portfolio)
lst = portfolio['shares']
portfolio['shares'] = sorted(lst)

print(portfolio)

del (portfolio['ornaments'])
print(portfolio)
