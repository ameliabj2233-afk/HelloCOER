#nilai tukar rupiah ke dollr

import time #
import os #

def animasi_roti_memantul():
    durasi = 2  # Detik
    end_time = time.time() + durasi
    posisi = 0
    maju = True
    
    while time.time() < end_time:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Logika memantul
        # Jika posisi mencapai 20, arahkan mundur. Jika 0, arahkan maju.
        if posisi >= 20:
            maju = False
        elif posisi <= 0:
            maju = True
            
        # Update posisi
        if maju:
            posisi += 1
        else:
            posisi -= 1
            
        # Cetak animasi dengan spasi sebanyak 'posisi'
        print("Croisant is jumping back to the menu...")
        print(" " * posisi + "🥐")
        
        time.sleep(0.1) # Kecepatan pantulan


def animasi_pita_memantul():
    durasi = 2  # Detik
    end_time = time.time() + durasi
    posisi = 0
    maju = True
    
    while time.time() < end_time:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Logika memantul
        # Jika posisi mencapai 20, arahkan mundur. Jika 0, arahkan maju.
        if posisi >= 20:
            maju = False
        elif posisi <= 0:
            maju = True
            
        # Update posisi
        if maju:
            posisi += 1
        else:
            posisi -= 1
            
        # Cetak animasi dengan spasi sebanyak 'posisi'
        print("Ribbon is jumping back to the menu...")
        print(" " * posisi + "🎀")
        
        time.sleep(0.1) # Kecepatan pantulan


print ('Hello COER🫸')
c = input('Input your name = ')
while True:
  print ('Hi', c, 'Can i help you?')
  tanya = input('').lower()

  if 'usd' in tanya:
  # kode untuk usd 
    a = int(input('Enter your rupiah here! '))
    b = float(a * 0.000059)
    print ('rupiah to usd =', b, '$')
    print ('Thank you', c, 'for use this program🎀')
    print('Hi', c, 'Is there anything else I can help with? (yes/no)')
    Answer = input('').lower()

    if 'no' in Answer:
        print('back to menu in 2 seconds...')
        animasi_roti_memantul()
        continue
        
    else:
        print('Alright')
        continue

  elif 'yen' in tanya:
    # kode untuk yen
    d = int(input('Enter your rupiah here! '))
    e = float(d * 0.0093)
    print ('rupiah to yen =', e, '¥')
    print ('Thank you', c, 'for use this program🎀')
    print('Hi', c, 'Is there anything else I can help with? (yes/no)')
    answer = input('').lower()

    if 'no' in answer:
        print('back to menu in 2 seconds...')
        animasi_pita_memantul()
        continue
        
    else:
        print('Alright')
        continue
  else:
    print ('Sorry, currency conversion is not available here.(example: I want to change rupiah to usd)')
    continue


  



