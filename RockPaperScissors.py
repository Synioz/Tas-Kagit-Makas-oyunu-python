import random as r

randompc = {
    1: 'Taş',
    2: 'Kağıt',
    3: 'Makas'
}
userselect = {
    'rock': 1,
    'paper': 2,
    'scissos': 3,
    'taş': 1,
    'kağıt': 2,
    'makas': 3,
    'tas': 1,
    'kagit': 2

}
usertrue = ['evet', 'yes', 'olur']
userfalse = ['yok', 'hayır', 'no', 'hayir', 'olmaz', 'çık', 'exit', 'cik']


def winandlose(userselection, inputn):
    pcput = r.randint(1,3)
    pcselection = randompc.get(pcput)
    if (pcput == 3 and userselection == 1) or (pcput == 1 and userselection == 2) or (pcput == 2 and userselection == 3):
        return f'Sen {inputn} dedin. Bilgisayar {pcselection} dedi.\nTebrikler sen kazandın!'
    elif (pcput == 1 and userselection == 3) or (pcput == 2 and userselection == 1) or (pcput == 3 and userselection == 2):
        return f'Sen {inputn} dedin. Bilgisayar {pcselection} dedi.\nSen kaybettin.'
    else:
        return f'Sen {inputn} dedin. Bilgisayar {pcselection} dedi.\nBerabere.'

def hello():
    n = input('Taş, Kağıt, Makas oynamak ister misiniz?\nSiz: ')
    
    firstput = n.lower()
    while True:
        if firstput in usertrue:
            print('Bunu duyduğuma sevindim!')
            inputn = input('Taş, Kağıt, Makas oyununa hoş geldiniz,\nLütfen bir seçim yapın.(Taş, Kağıt, Makas vb.)\nSiz: ')
            userinput = inputn.lower()
            userselection = userselect.get(userinput)

            if userselection:
                winandloser = winandlose(userselection, inputn)
                print(winandloser)
                break

        elif firstput in userfalse:
            print('Bunu duyduğuma üzüldüm, program kapatılıyor...')
            break
        else:
            break



hello()