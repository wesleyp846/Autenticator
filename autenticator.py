import time
import pyotp
import qrcode

#print(pyotp.random_base32())

chave_mestra='VWXH5XD2AZITNG5RPR3GZKPIMT5E6WUZ'
codigo=pyotp.TOTP(chave_mestra)

link=pyotp.TOTP(chave_mestra).provisioning_uri(name='wesley', issuer_name='atenticatosWesley')
meu_qrcode=qrcode.make(link)
meu_qrcode.save('qrcodewes.png')

while True:

    codigo_usuario=input('Codigo:')
    retorno=codigo.verify(codigo_usuario)

    if retorno == True:
        print('Acertou "Mizeráviii"')
        break
    esle: print('Faustau falou: Errrrrrrrooooooouuuuuu')
