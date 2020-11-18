import random
from time import sleep
primes = ['101', '103', '107', '109', '113', '127', '131', '137', '139', '149',
'151', '157', '163', '167', '173', '179', '181', '191', '193', '197', '199',
'211', '223', '227', '229', '233', '239', '241', '251', '257', '263', '269',
'271', '277', '281', '283', '293', '307', '311', '313', '317', '331', '337',
'347', '349', '353', '359', '367', '373', '379', '383', '389', '397', '401',
'409', '419', '421', '431', '433', '439', '443', '449', '457', '461', '463',
'467', '479', '487', '491', '499', '503', '509', '521', '523', '541', '547',
'557', '563', '569', '571', '577', '587', '593', '599', '601', '607', '613',
'617', '619', '631', '641', '643', '647', '653', '659', '661', '673', '677',
'683', '691', '701', '709', '719', '727', '733', '739', '743', '751', '757',
'761', '769', '773', '787', '797', '809', '811', '821', '823', '827', '829',
'839', '853', '857', '859', '863', '877', '881', '883', '887', '907', '911',
'919', '929', '937', '941', '947', '953', '967', '971', '977', '983', '991', '997']

def coprime(p,q):
	while q != 0:
		t = p%q
		p = q
		q = t

	return p == 1


def get_enc(phiN,N):
	enc = []
	for i in range(2, phiN + 1):
		if coprime(i, phiN) == True and coprime(i, N) == True:
			enc.append(i)
	return enc


def get_dec(enc, phiN):
    dec = []
    for i in range(enc, enc * 10):
        if enc * i % phiN == 1:
            dec.append(i)
    return dec


def encrypt(l, enc, N):
    out = []
    for i in l:
        out.append(i ** enc % N)
    return out

def decrypt(l, dec, N):
    out = []
    for i in l:
        out.append(i ** dec % N)
    return out

while True:
    p = int(primes[random.randint(0,len(primes)-1)])
    q = int(primes[random.randint(0,len(primes)-1)])
    if p != q:
        break

print('Generating keys..')
sleep(1)
N = q*p
phiN = (p - 1) * (q - 1)
enc = get_enc(phiN, N)
enc = enc[random.randint(0,len(enc) - 1)]
dec = get_dec(enc, phiN)
while True:
    try:
        dec = dec[random.randint(0,len(dec) - 1)]
        break
    except ValueError:
        continue

print(f'prime number 1 = {p}')
print(f'prime number 2 = {q}')
print(f'Product of both (N) = {N}')
print(f'Coprime with N = {phiN}')
print(f'Public key for encryption = {enc}')
print(f'Private key decryption = {dec}')

input_message = input('Type a message to encrypt:\n')

message = []
for c in input_message:
    message.append(ord(c))
print(f'ASCII-code {message}')

e_message = encrypt(message, enc, N)
output_message = []
for i in e_message:
    output_message.append(i)
output_message = '-'.join(str(x) for x in output_message)
print(f'Encrypted decimal = {str(output_message)}')

d_message = decrypt(e_message, dec, N)
output_message = []
for i in d_message:
    output_message.append(chr(i))
output_message = ''.join(str(x) for x in output_message)

print(str(output_message))
