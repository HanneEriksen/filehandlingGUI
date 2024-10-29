#Opprettes utenfor funksjon for bruk 
oppdretterfil=('oppdretter.txt')
hundefil=('hundefil.txt')
hundeeierfil=('hundeeier.txt')
def oppdretter_fil_behandling (oppdretterfil):
    try:
        #Oppretter dictionary for innholdet i oppdretter
        oppdretter={}

        #Åpner oppdretter fil
        oppdretterfil=open('oppdretter.txt','r',encoding='utf-8')

        #Leser første linje i oppdretter fil
        oppdretterID = oppdretterfil.readline()

        #While-løkke som går gjennom hele oppdretterfilen, linje for linje til den er tom
        while oppdretterID!='':
            #Stripper første linje i oppdretterfil
            oppdretterID=oppdretterID.rstrip('\n')

            #Leser videre i oppdretterfilen og stripper linjene
            kennelnavn=oppdretterfil.readline().rstrip('\n')
            kennelfornavn=oppdretterfil.readline().rstrip('\n')
            kenneletternavn=oppdretterfil.readline().rstrip('\n')

            #Legger til dataene i en todimensjonal dictionary
            oppdretter[oppdretterID]={'kennelnavn':kennelnavn,'kennelfornavn':kennelfornavn,'kenneletternavn':kenneletternavn}

            #Leser første linje i oppdretterfil
            oppdretterID=oppdretterfil.readline()

        #Lukker oppdretterfil
        oppdretterfil.close()

        #Returnerer verdiene i oppdretter
        return oppdretter
        
    except IOError:
        print('Oppdretterfil finnes ikke')


def hund_fil_behandling (hundefil):
    try:
        #Oppretter dictionary
        hund={}

        #Åpner hund fil
        hundefil=open('hund.txt','r',encoding='utf-8')

        #Leser første linje i hundefil
        hundeID=hundefil.readline()

        #While-løkke som går gjennom hele hundefilen, linje for linje til den er tom
        while hundeID!='':
            #Stripper første linje i hundefil
            hundeID=hundeID.rstrip('\n')

            #Leser resterende linjer i hundefil og stripper de 
            oppdretterID=hundefil.readline().rstrip('\n')
            hundeeierID=hundefil.readline().rstrip('\n')
            navn=hundefil.readline().rstrip('\n')
            kjonn=hundefil.readline().rstrip('\n')
            fodt=hundefil.readline().rstrip('\n')

            #Oppretter en todimensjonal dictionary
            hund[hundeID]={'oppdretterID':oppdretterID,'hundeeierID':hundeeierID,'navn':navn,'kjonn':kjonn,'fodt':fodt}

            #Leser første linje i hundefil
            hundeID=hundefil.readline()

        #Lukker hundefil 
        hundefil.close()

        #Returnerer verdiene til hund
        return hund

    except IOError:
        print('Hundefil finnes ikke')


def hundeeier_fil_behandling (hundeeierfil):
    try:
        #Oppretter dictionary
        hundeeier={}

        #Åpner hundeeier fil
        hundeeierfil=open('hundeeier.txt','r',encoding='utf-8')

        #Leser første linje i hundeeierfil
        hundeeierID=hundeeierfil.readline()

        #Whileløkke som leser hundeeierfil frem til den er tom
        while hundeeierID!='':
            #Stripper første linje i hundeeierfil
            hundeeierID=hundeeierID.rstrip('\n')

            #Leser resterende linjer i hundeeierfil og stripper de 
            fornavn=hundeeierfil.readline().rstrip('\n')
            etternavn=hundeeierfil.readline().rstrip('\n')

            #Oppretter en dictionary i dictionary struktur
            hundeeier[hundeeierID]={'fornavn':fornavn,'etternavn':etternavn}

            #Leser første linje i hundeeierfil
            hundeeierID=hundeeierfil.readline()
        
        #Lukker hundeeierfil 
        hundeeierfil.close()

        return hundeeier

    except IOError:
        print('Hundeeierfil finnes ikke')


def hundeopplysninger(hundeID):
    try:
        #Sjekker opplysninger opp mot dictionary
        #Oppretter variabler for å hente funksjonene
        oppdretter=oppdretter_fil_behandling(oppdretterfil)
        hund=hund_fil_behandling(hundefil)
        hundeeier=hundeeier_fil_behandling(hundeeierfil)
        hund_info=0
        oppdretter_info=0
        hundeeier_info=0

        #Sjekker om hundeID finnes i hund og legger til data i hund_info som brukes i neste funksjon
        if hundeID !='' and hundeID in hund:
            hund_info=hund[hundeID]
            oppdretterID=hund_info['oppdretterID']
            hundeeierID=hund_info['hundeeierID']

            #Sjekker om oppdretterID finnes/matches i oppdretter og legger i variabel oppdretter_info
            if oppdretterID in oppdretter:
                oppdretter_info = oppdretter[oppdretterID]

            #Sjekker om hundeeierID finnes/matches i hundeeier og legger i variabel hundeeier_info
            if hundeeierID in hundeeier:
                hundeeier_info = hundeeier[hundeeierID]
        else:
            print('Skriv inn gyldig hundeID')
        
        #Returnerer verdiene
        return hund_info, oppdretter_info, hundeeier_info

    #Litt dobbelt opp da jeg fikk problemer med except, derfor else testen over for å printe ut til bruker i terminal. Men konseptet er forstått og prøvd implementert.        
    except KeyError:
        print('HundeID finnes ikke')

#Funksjon for å sette de riktige verdiene til GUI
def vis_hundeopplysninger():
    hundeID_verdi = hundeID.get()
    hund_info, oppdretter_info, hundeeier_info = hundeopplysninger(hundeID_verdi)

    if hund_info:
        hundenavn.set(hund_info['navn'])
        kjonn.set(hund_info['kjonn'])

    if oppdretter_info:
        kennelnavn.set(oppdretter_info['kennelnavn'])

    if hundeeier_info:
        fornavn.set(hundeeier_info['fornavn'])
        etternavn.set(hundeeier_info['etternavn'])

#Importerer tkinter og oppretter vindu
from tkinter import * 
window=Tk()

#Gir vinduet et navn
window.title('Finn hund med opplysninger om kennel og eier')

#Lager ledetekster for hundeID, hundenavn, kjønn, kennelnavn, eiers fornavn og etternavn
lbl_hundeID=Label(window, text='Oppgi hundeID:')
lbl_hundeID.grid(row=0, column=0, padx=5, pady=5,sticky=E)

lbl_hundenavn=Label(window, text='Hundenavn:')
lbl_hundenavn.grid(row=3, column=0, padx=5, pady=5,sticky=E)

lbl_kjonn=Label(window, text='Kjønn:')
lbl_kjonn.grid(row=3, column=2, padx=5, pady=5,sticky=E)

lbl_kennelnavn=Label(window, text='Kennelnavn:')
lbl_kennelnavn.grid(row=4, column=0, padx=5, pady=5,sticky=E)

lbl_fornavn=Label(window, text='Eiers fornavn:')
lbl_fornavn.grid(row=5, column=0, padx=5, pady=5,sticky=E)

lbl_etternavn=Label(window, text='Eiers etternavn:')
lbl_etternavn.grid(row=5, column=2, padx=5, pady=5,sticky=E)

#Lager inndatafelt for oppgi hundeID
hundeID=StringVar()
ent_hundeID=Entry(window, width=9, textvariable=hundeID)
ent_hundeID.grid(row=0, column=1,padx=5, pady=5,sticky=W)

#Lager visningsfelt for hundenavn, kjønn, kennelnavn, eiers fornavn og etternavn
hundenavn=StringVar()
ent_hundenavn=Entry(window, width=15, state='readonly', textvariable=hundenavn)
ent_hundenavn.grid(row=3, column=1, padx=5, pady=5,sticky=W)

kjonn=StringVar()
ent_kjonn=Entry(window, width=7, state='readonly', textvariable=kjonn)
ent_kjonn.grid(row=3, column=3, padx=5, pady=5,sticky=W)

kennelnavn=StringVar()
ent_kennelnavn=Entry(window, width=20, state='readonly', textvariable=kennelnavn)
ent_kennelnavn.grid(row=4, column=1, padx=5, pady=5,sticky=W)

fornavn=StringVar()
ent_fornavn=Entry(window, width=10, state='readonly', textvariable=fornavn)
ent_fornavn.grid(row=5, column=1, padx=5, pady=5,sticky=W)

etternavn=StringVar()
ent_etternavn=Entry(window, width=10, state='readonly', textvariable=etternavn)
ent_etternavn.grid(row=5, column=3, padx=5, pady=5,sticky=W)

#Lager knapp for hundeopplysninger 
btn_finn=Button(window, text='Finn hundeopplysninger',command=vis_hundeopplysninger)
btn_finn.grid(row=0, column=2, pady=25, sticky=W)


#Lager knapp for å avslutte
btn_avslutt=Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=8, column=5, pady=25,sticky=W)

window.mainloop()