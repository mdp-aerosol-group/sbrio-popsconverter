#!/usr/bin/env python

def convert():
    print('Greetings from the POPS Converter')
    mypath = '20220620/'

    for file in os.listdir(mypath):
        if file.endswith('Peak.bin'):
            print(file)
            pops=POPStool.read_binary(mypath+file)
            a = file.split('.')    
            pd.DataFrame(pops.data).to_csv(a[0] + '.csv')

if __name__ == '__main__':
    import os
    import mypeaks as POPStool
    import pandas as pd
    convert()
