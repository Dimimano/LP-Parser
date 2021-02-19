import linecache
import numpy as np
import os
import sys
import time



start_time = time.time()



# Edw prepei na dhlwnetai to PATH toy arxeioy poy periexei to grammiko problima p.x. "F:\workspace\Parser\LP1.txt" !
FilePath = "F:\workspace\Parser\LP1.txt"

# Elegxos gia to an o fakelos einai adeios.
if os.stat(FilePath).st_size == 0:
    sys.exit("File is Empty!")

# Elegxos gia thn yparksi ths leksis 'min'/'max'     

#Briskoyme thn proti grammh twn dedomenwn toy LP1,dhladh thn antikeimenikh synartisi.
startOfData = 1

while(1):
    retrieved_line_with_spaces = linecache.getline(FilePath, startOfData)
    if retrieved_line_with_spaces.find('x') != -1:
        break;
    else:
        startOfData = startOfData + 1

# To programma termatizei sth grammh poy briskei th leksi 'end' opote ginetai elegxos an auth yparxei kai enimerwnetai o xrhsths sthn periptwsh pou den uparxei.
with open(FilePath) as file:
    contents = file.read()
    if 'end' not in contents:
        print ("The Linear problem's data must finish with keyword 'end' ! Parser is terminated.")
        sys.exit('Parser is terminated.')

# Briskoyme thn teleutaia grammh twn dedomenwn toy LP1.    
endOfData = startOfData
while(retrieved_line_with_spaces.find('end')== -1):
    retrieved_line_with_spaces = linecache.getline(FilePath, endOfData)
    endOfData = endOfData + 1   
    

# Arxikopoioyme diafores boithikes metablites.

# cList einai h lista poy topothetoume ta stoixeia toy c Matrix prin ta metatrepsoyme se pinaka.
cList = []
# AListHelper einai h lista poy topothetoume ta stoixeia toy A Matrix prin ta metatrepsoyme se pinaka.
AListHelper = []
# EqinList einai h lista poy topothetoume ta stoixeia toy Eqin Matrix prin ta metatrepsoyme se pinaka.
EqinList = []
# bList einai h lista poy topothetoume ta stoixeia toy b Matrix prin ta metatrepsoyme se pinaka.
bList = []

# sto programma genika otan eksetazoyme kathe grammi h prwth epanalipsi diaferei ston kwdika apo tis epomenes epanalipseis,opote h metablhth ayth ksexwrizei tis periptwseis aytes.
firstWhileLoopIteration = 0

# epishs h eksetasi ths prwths grammhs twn texnologikwn periorismwn diaferei sto kwdika apo tis ypoloipes
firstLineOfTechnologicalConstraints = 0
# opote oi dyo metablhtes aytes tis ksexwrizoyn.
remainingLinesOfTechnologicalConstraints = 0

# metraei poia grammh periorismwn eksetazoyme.
constraintCounter = 0

# exei na kanei to 'koympwma' mikroterwn pinakwn se ena megalytero wste na sxhmatistei o A Matrix.
firstIfFlag = 1


# Diasxizoyme grammh-pros-grammh ta dedomena toy LP1
for currentLine in range(startOfData,endOfData):

    
    retrieved_line_with_spaces = linecache.getline(FilePath, currentLine)
    
    # An anamesa sta dedomena yparxoyn kenes grammes pareleipse tis.(sta dedomena toy grammikoy problimatos kathe grammi exei estw ena x)
    if retrieved_line_with_spaces.find('x') == -1:
        continue
    
    # Se kathe grammi afairoyme ta kena
    retrieved_line = retrieved_line_with_spaces.replace(" ","")

    # kai apothikeuoyme to deikth poy deixnei sto telos ths grammhs '\n'
    endOfLine = retrieved_line.find('\n')
    
    # Elegxos gia tis yparksi mias apo tis lekseis min/max sthn Objective Function h opoia tha einai panta h prwth seira twn dedomenwn (currentLine = startOfData).
    if currentLine == startOfData:
        if retrieved_line.find('max',0,3) == -1 and retrieved_line.find('min',0,3) == -1:
            print('Objective function must contain either of {max,min} at the start!')
            sys.exit('Parses is terminated.')


    while(1):
    
        # Arxikopoioyme to boithitiko string z poy syllegei ena-pros-ena toys syntelestes mias metablitis apo th grammh poy eksetazoyme. Sthn synexeia antistrefetai kai metatre-
        # petai ston analogo typo.
        z = ""

        # An eimaste sthn antikeimeniki synartisi...
        if retrieved_line.find('min') != -1 or retrieved_line.find('max') != -1:
            # An eimaste sth prwth epanalipsi...
            if firstWhileLoopIteration == 0:
                
                
                
                # Ypologismos toy MinMax        
                if retrieved_line.find('max') == -1:
                    if retrieved_line.find('min') == -1:
                        sys.exit("Please determine if the linear problem is 'max' or 'min'!")
                    else: MinMax = -1
                else: MinMax = 1
        
                # Briskoume to index ths prwths metablitis mesa sthn grammh.
                # Kai epishs briskoyme to index kai tis epomenis metablitis,ksekinontas mia anazitisi apo ekei poy brikame th prwth.
                # Epeidh oi anazitiseis ginontai me bash to 'x' otan h antikeimenikh synarthsh exei th morfh 'max' ksekiname amesws meta apo th leksi ayth thn anazitisi.
                if MinMax == 1:
                    indexOfVariable = retrieved_line.find('x',4)
                    indexOfNextVariable = retrieved_line.find('x',indexOfVariable+1)
                else: 
                    indexOfVariable = retrieved_line.find('x')
                    indexOfNextVariable = retrieved_line.find('x',indexOfVariable+1)
                
                
                
                # Gia na broyme ton deikth ths metablhths auths akoloythoyme ton eksis algorithmo.
            
                # Arxikopoioyme tis boithikes metablites.
                helpString = ""
                forLoopCounter = 0
            
                # Ksekiname mia for anazitisis mesa sth grammh,arxizontas amesws meta tin thesi tis prwtis metablitis mexri tin thesi thn epomenhs metablitis.
                for i in range(indexOfVariable+1,indexOfNextVariable):
                    # Ayksanoyme ton deikth poy metra tis epanalipseis tis for.
                    forLoopCounter = forLoopCounter + 1
                    # H for tha diakopsei otan ftasoyme eite sto symbolo '+' eite sto '-' kathws ekei akribws einai poy teliwnoyn ta 'psifia' toy deikti tis metablitis mas.
                    # Ayto oysiastika ginetai gia tin periptwsi poy deikths einai panw apo 9 (p.x. x10) kai ta psifia einai perisotera apo 1.
                    if retrieved_line[i] == '+' or retrieved_line[i] == '-':
                        break;
                    # Oso den exoyme brei ta symbola ayta synexise na katagrafeis sto helpString ta psifia toy deikth.
                    elif retrieved_line[i] != '+' and retrieved_line[i] != '-':
                        helpString = retrieved_line[i] + helpString
                        i = i + 1
            
                    # An kaname perisoteres apo mia epanalipseis tote..
                    if forLoopCounter > 1:
                        # Antistrepse to helpString.
                        helpString = helpString[::-1]
                        # Metatrepse to se int kai dwsto sth metabliti pointerOfVariable.
                        pointerOfVariable = int(helpString)
                        # Apothikeyse th giati tha th xreiastoyme se epomenes epanalipseis.
                        pointerOfPreviousVariable = pointerOfVariable
                    # An kaname mono mia shmainei oti eimastan sthn apla periptwsh opoy o deikths exei ena mono pshfio to opoio tha einai sth grammh amesws meta th metablhth mas.
                    else:
                        pointerOfVariable = int(retrieved_line[indexOfVariable+1])
                        pointerOfPreviousVariable = pointerOfVariable
            
            
                
                # (An eimaste sth prwth epanalipsi) kai h prwth metabliti den einai to 'x1'...
                if pointerOfVariable > 1:
                    #bale 0 sth lista c stoys syntelestes twn metablhtwn poy paraleipontai.
                    for i in range(0,pointerOfVariable-1):
                        cList.insert(i,0)
            
            
                # these thn metablhth poy brikame ws antikeimeniki metablhth
                indexOfObjectiveVariable = indexOfVariable
            
                # To apothikeyoume giati stis epomenes epanalipseis tou while apo edw tha ksekiname thn anazitisi mexri tin epomenh metabliti etsi wste na briskoyme ton
                # syntelesti tis.
                indexOfPreviousObjectiveVariable = indexOfVariable
                
                
                # Elegxos gia to an yparxei {+,-} meta th metablhth.
                if retrieved_line.find('+', indexOfObjectiveVariable, indexOfNextVariable) == -1 and retrieved_line.find('-',indexOfObjectiveVariable, indexOfNextVariable) == -1:
                    print('The Objective Function is incomplete: Math Symbol {+,-} is missing!')
                    sys.exit("Parser is terminated")
    
                # bres to symbolo ths isothtas poy yparxei mono mia fora meta to onoma ths antikeimenikhs synartisis.
                # stin periptwsi tis prwths metablitis tin a/khs synarthshs ksekiname thn anazitisi apo to '=' kai meta gia na broyme ton syntelesth.   
                indexOfEqlSymbol = retrieved_line.find('=')
                # An to epomeno stoixeio meta to ison einai to 'x'...(dhladh den grafetai kapoios syntelestis gia thn metablith)
                if retrieved_line[indexOfEqlSymbol+1] == 'x':
                    # tote o syntelestis tha einai isos me 1
                    cList.insert(pointerOfVariable,1)
    
                    # An anamesa sto '=' kai to 'x' breis ena meion '-' tote einai arnhtikos... 
                elif retrieved_line.find('-', indexOfEqlSymbol, indexOfObjectiveVariable) != -1:
                    # krata th thesi toy meion mesa sth grammh
                    indexOfMinus = retrieved_line.find('-')
        
                    # An amesws meta to meion breis to 'x' tote...
                    if retrieved_line[indexOfMinus+1] == 'x':
                        # o syntelestis tha einai isos me -1
                        cList.insert(pointerOfVariable,-1)
        
                    # An anamesa sto symbolo '=' kai to 'x' breis mia teleia '.' tote o syntelestis einai dekadikos...
                    elif retrieved_line.find('.', indexOfEqlSymbol, indexOfObjectiveVariable) != -1:
                        # me mia for syllekse ena-pros-ena ta psifia toy syntelesth sto boithiko string z...
                        for x in range(indexOfEqlSymbol+1,indexOfObjectiveVariable):
                            z = retrieved_line[x] + z
                        # antistrepse ton...
                        z = z[::-1]
                        # kai balton sth c ws float.
                        cList.insert(pointerOfVariable,float(z))
                    # An den breis teleia '.' tote o syntelestis einai akeraios...
                    elif retrieved_line.find('.', indexOfEqlSymbol, indexOfObjectiveVariable) == -1:
                        # me mia for syllekse ena-pros-ena ta psifia toy syntelesth sto boithitiko string z...
                        for x in range(indexOfMinus,indexOfObjectiveVariable):
                            z = retrieved_line[x] + z
                        # antistrepse ton...
                        z = z[::-1]
                        # kai balton sth c ws int.
                        cList.insert(pointerOfVariable,int(z))
                # An den breis meion '-' tote einai thetikos...
                elif retrieved_line.find('-', indexOfEqlSymbol, indexOfObjectiveVariable) == -1:
                    # An einai dekadikos...
                    if retrieved_line.find('.', indexOfEqlSymbol, indexOfObjectiveVariable) != -1:
                        for x in range(indexOfEqlSymbol+1,indexOfObjectiveVariable):
                            z = retrieved_line[x] + z
                        z = z[::-1]
                        cList.insert(pointerOfVariable,float(z))
                    # An einai akeraios...
                    elif retrieved_line.find('.', indexOfEqlSymbol, indexOfObjectiveVariable) == -1:
                        for x in range(indexOfEqlSymbol+1,indexOfObjectiveVariable):
                            z = retrieved_line[x] + z
                        z = z[::-1]
                        cList.insert(pointerOfVariable,int(z))
        
        
         
            # An den hmaste sth prwth epanalhpsh...
            elif firstWhileLoopIteration == 1:
                z = ""
            
                # Stin proigoymeni epanalipsi toy while apothikeysame th metablhth poy tha eksetasoyme twra.
                indexOfObjectiveVariable = indexOfNextVariable
            
                # Briskoume thn epomenh metablhth h opoia tha mas boithisei na eleksoume an anamesa toys yparxei eite to sumbolo '+' eite to '-'.
                indexOfNextVariable = retrieved_line.find('x',indexOfObjectiveVariable+1)
            
                # Arxika elegxoume mipws briskomaste sth teleytaia metablhth giati meta apo ayth den tha yparxei kanena apo ta 2 symbola eks orismoy.
                if retrieved_line.find('x',indexOfObjectiveVariable+1,endOfLine) != -1:
                    # Ginetai o elegxos kai bganei to katallilo mynhma.
                    if retrieved_line.find('+', indexOfObjectiveVariable, indexOfNextVariable) == -1 and retrieved_line.find('-',indexOfObjectiveVariable, indexOfNextVariable) == -1:
                        print('The Objective Function is incomplete: Math Symbol {+,-} is missing!')
                        sys.exit("Parser is terminated")
            
            
                # Gia na broume ton deikth ths metablhths ayths tha xrhsimopoihsoyme ena while loop.
                # An exoume mia a/kh synarthsh p.x. 'x1 + x100 + x101' gia na broume to deikth ths deuteris metablhths dhladh toy 'x100' tha ksekinisoyme thn anazitisi mia thesi meta to 'x'
                # kai tha stamatisoume otan broume to '+'.
                # Ayto pou allazei se sxesi me thn prwth epanalipsi einai oti twra yparxei h periptwsh poy ftanoume sth teleytaia metablhth (p.x. x101).
                # Edw pera epomenws den mporoume dhladh na oriothetoyme thn anazitisi tws pshfiwn anamesa mono sta '+' h '-' giati h teleytaia metablhth den exei kapoio apo ayta meta ths.
                # Epomenws to while loop tha termatizei otan brei kapoia apo ayta ta symbola h to telos ths grammhs.
            
                # Arxikopoioyme tis boithikes metablites.
                helpString = ""
                whileLoopCounter = 0
                i = indexOfObjectiveVariable + 1
            
                while (retrieved_line[i] != '+' and retrieved_line[i] != '-' and retrieved_line[i] != '\n' ):
                    # Ayksanoyme ton deikth poy metra tis epanalipseis tou while.
                    whileLoopCounter = whileLoopCounter + 1
                    helpString = retrieved_line[i] + helpString
                    i = i + 1
            
                # An kaname perisoteres apo mia epanalipseis tote..
                if whileLoopCounter > 1:
                    # Antistrepse to helpString.
                    helpString = helpString[::-1]
                    # Metatrepse to se int kai dwsto sth metabliti pointerOfVariable.
                    pointerOfVariable = int(helpString)
                
                # An kaname mono mia shmainei oti eimastan sthn aplh periptwsh opoy o deikths exei ena mono pshfio to opoio tha einai sth grammh amesws meta th metablhth mas.
                else:
                    pointerOfVariable = int(retrieved_line[indexOfObjectiveVariable+1])
            
                # Prepei twra sthn periptwsh poy gia paradeigma hmastan sthn metablhth x3 kai pigame sthn x6 na mhdenisoyme toys syntelestes olwn ton endiameswn metablhtwn,
                # gia to paradeigma aytoi tha einai: x4, x5.
            
                # Gia na to kanoyme ayto apo ton deikth ths metablitis poy eksetazoyme twra afairoyme ton deikth ths proigoumenis poy apothikeysame sthn prohgoymenh epanalipsi,
                # h diafora toys tha mas dwsei to plithos alla kai tis theseis twn metablitwn twn opoiwn toys syntelestes prepei na mhdenisoyme.
                if pointerOfVariable - pointerOfPreviousVariable > 1:
                    for i in range(pointerOfPreviousVariable+1,pointerOfVariable):
                        cList.insert(i,0)
                    
                # Apothikeyoume thn metabliti me to megalitero dikti(thn teleytaia ousiastika).
                if pointerOfVariable>pointerOfPreviousVariable:
                    maxVariable = pointerOfVariable
                    
                # Se ayto to shmeio to mono poy leipei gia na proxwrisoyme ston ypologismo toy sentelesth ths metablhths poy eksetazoyme einai h thesi toy symbolou '+' h toy symboloy '-'
                # to opoio panta einai mia thesh pisw akribws apo ton syntelesti poy psaxnoyme.
                # Apo to symbolo ayto tha oriothetisoyme mia anazitish kai sylleksi kathe psifioy toy syntelesti perilambanontas kai to '-' sthn periptwsh poy einai arnhtikos.
            
            
            
                # An einai thetikos...
                if retrieved_line.find('+',indexOfPreviousObjectiveVariable,indexOfObjectiveVariable) != -1:
                    # krata th thesh toy plus mesa sth grammh.
                    indexOfPlus = retrieved_line.find('+',indexOfPreviousObjectiveVariable,indexOfObjectiveVariable)
                    # An einai dekadikos...
                    if retrieved_line.find('.', indexOfPlus, indexOfObjectiveVariable) != -1:
                        for x in range(indexOfPlus+1,indexOfObjectiveVariable):
                            z = retrieved_line[x] + z
                        z = z[::-1]
                        cList.insert(pointerOfVariable,float(z))
                    # An den yparxei syntelestis...
                    elif retrieved_line[indexOfPlus+1] == 'x':
                        cList.insert(pointerOfVariable,1)
                    # An einai akeraios...
                    elif retrieved_line.find('.', indexOfPlus, indexOfObjectiveVariable) == -1:
                        for x in range(indexOfPlus+1,indexOfObjectiveVariable):
                            z = retrieved_line[x] + z
                        z = z[::-1]
                        cList.insert(pointerOfVariable,int(z))
                
                # An einai arnhtikos...  
                elif retrieved_line.find('-', indexOfPreviousObjectiveVariable, indexOfObjectiveVariable) != -1:
                    # krata th thesi toy meion mesa sth grammh.
                    indexOfMinus = retrieved_line.find('-',indexOfPreviousObjectiveVariable,indexOfObjectiveVariable)
                    # An den yparxei sentelestis...
                    if retrieved_line[indexOfMinus+1] == 'x':
                        cList.insert(pointerOfVariable,-1)
        
                    # An einai dekadikos...
                    elif retrieved_line.find('.', indexOfMinus, indexOfObjectiveVariable) != -1:
                        for x in range(indexOfMinus,indexOfObjectiveVariable):
                            z = retrieved_line[x] + z
                        z = z[::-1]
                        cList.insert(pointerOfVariable,float(z))
                    # An einai akeraios...
                    elif retrieved_line.find('.', indexOfMinus, indexOfObjectiveVariable) == -1:
                        for x in range(indexOfMinus,indexOfObjectiveVariable):
                            z = retrieved_line[x] + z
                        z = z[::-1]
                        cList.insert(pointerOfVariable,int(z))   
            
                # Elegxoume an exoyme ftasei sth teleytaia metabliti opou kai prepei to while na termatisei.
                if retrieved_line.find('x',indexOfObjectiveVariable+1,endOfLine) == -1:
                    # Efoson teliwsame me thn ant/kh synarthsh eidopoioume to programma oti seira exei h prwth grammh twn texnologikwn periorismwn.
                    firstLineOfTechnologicalConstraints = 1
                    firstWhileLoopIteration = 0
                    break;    
               
                #Telos prepei na proetoimasoyme tis metablites gia tin epomenh epanalipsi.
                indexOfPreviousObjectiveVariable = indexOfObjectiveVariable
                pointerOfPreviousVariable = pointerOfVariable
        
            
            firstWhileLoopIteration = 1
        
        # An eimaste sth prwth seira twn texnologikwn periorismwn kai sthn prwth epanalipsi toy while gia texnologikoys periorismoys...   
        if firstLineOfTechnologicalConstraints == 1 and firstWhileLoopIteration == 0:
            
            #Ayksanoyme ton deikth poy metra se poio periosmo eimaste wste na enhmerwnontai katallila Eqin and b.
            constraintCounter = constraintCounter  + 1
            
            
            #Eelegxos gia tin yparksi mias apo tis 3 periptwseis syntaksis toy s.t..
            if retrieved_line.find('st:') == -1 and retrieved_line.find('s.t.:') == -1 and retrieved_line.find('subject to:'):
                sys.exit("Syntax Error: The first line of the Technological Constraints must contain either 'st:' or 's.t.:' or 'subject to:'.") 
            
            
            
            # Briskoume to index ths prwths metablitis mesa sthn grammh.
            # Kai epishs briskoyme to index kai tis epomenis metablitis,ksekinontas mia anazitisi apo ekei poy brikame th prwth.
            indexOfVariable = retrieved_line.find('x')
            indexOfNextVariable = retrieved_line.find('x',indexOfVariable+1)
            
                
        
            # Gia na broyme ton deikth ths metablhths auths akoloythoyme ton eksis algorithmo.
            
            # Arxikopoioyme tis boithikes metablites.
            helpString = ""
            forLoopCounter = 0
            
            # Ksekiname mia for anazitisis mesa sth grammh,arxizontas amesws meta tin thesi tis prwtis metablitis mexri tin thesi thn epomenhs metablitis.
            for i in range(indexOfVariable+1,indexOfNextVariable):
                # Ayksanoyme ton deikth poy metra tis epanalipseis tis for.
                forLoopCounter = forLoopCounter + 1
                # H for tha diakopsei otan ftasoyme eite sto symbolo '+' eite sto '-' kathws ekei akribws einai poy teliwnoyn ta 'psifia' toy deikti tis metablitis mas.
                # Ayto oysiastika ginetai gia tin periptwsi poy deikths einai panw apo 9 (p.x. x10) kai ta psifia einai perisotera apo 1.
                if retrieved_line[i] == '+' or retrieved_line[i] == '-':
                    break;
                # Oso den exoyme brei ta symbola ayta synexise na katagrafeis sto helpString ta psifia toy deikth.
                elif retrieved_line[i] != '+' and retrieved_line[i] != '-':
                    helpString = retrieved_line[i] + helpString
                    i = i + 1
            
            # An kaname perisoteres apo mia epanalipseis tote..
            if forLoopCounter > 1:
                # Antistrepse to helpString.
                helpString = helpString[::-1]
                # Metatrepse to se int kai dwsto sth metabliti pointerOfVariable.
                pointerOfVariable = int(helpString)
                # Apothikeyse th giati tha th xreiastoyme se epomenes epanalipseis.
                pointerOfPreviousVariable = pointerOfVariable
                # An kaname mono mia shmainei oti eimastan sthn apla periptwsh opoy o deikths exei ena mono pshfio to opoio tha einai sth grammh amesws meta th metablhth mas.
            else:
                pointerOfVariable = int(retrieved_line[indexOfVariable+1])
                pointerOfPreviousVariable = pointerOfVariable
            
            
            
            # (An eimaste sth prwth epanalipsi) kai h prwth metabliti den einai to 'x1'...
            if pointerOfVariable > 1:
                #bale 0 sth lista a stoys syntelestes twn metablhtwn poy paraleipontai.
                for i in range(0,pointerOfVariable-1):
                    AListHelper.insert(i,0)
                
            # these thn metablhth poy brikame ws metablhth periorismoy
            indexOfConstraintVariable = indexOfVariable
            
            # To apothikeyoume giati stis epomenes epanalipseis tou while apo edw tha ksekiname thn anazitisi mexri tin epomenh metabliti etsi wste na briskoyme ton
            # syntelesti tis.
            indexOfPreviousConstraintVariable = indexOfVariable
            
            # Elegxos an yparxei plus or minus anamesa se kathe metabliti.
            # Arxika elegxoume mipws briskomaste sth teleytaia metablhth giati meta apo ayth den tha yparxei kanena apo ta 2 symbola eks orismoy.
            if retrieved_line.find('x',indexOfConstraintVariable+1,endOfLine) != -1:
                # Elegxos gia to an yparxei {+,-} meta th metablhth.
                if retrieved_line.find('+', indexOfConstraintVariable, indexOfNextVariable) == -1 and retrieved_line.find('-',indexOfConstraintVariable, indexOfNextVariable) == -1:
                    print('Constraint Function 1 is incomplete: Math Symbol {+,-} is missing!')
                    sys.exit("Parser is terminated")
            
            # Prokeimenoy na oriotheteitai h anazhthsh toy syntelesth ths prwths metablhths sth syntaksi twn dedomenwn yparxei enas epipleon kanonas se aytoys pou dinei h askhsh,
            # o opoios einai otan to 'subject to' se opoiadhpote apo tis 3 periptwseis syntaksis toy na teliwnei me anw kai katw teleia ':'
            # Epomenws sthn prwth epanalipsi ths prwths grammhs twn periorismwn ksekiname thn anazitisi apo to xarakthra ':'   
            indexOfColonSymbol = retrieved_line.find(':')
            
            
            # An to epomeno stoixeio meta to colon(:) einai to 'x'...(dhladh den grafetai kapoios syntelestis gia thn metablith)
            if retrieved_line[indexOfColonSymbol+1] == 'x':
                # tote o syntelestis tha einai isos me 1
                AListHelper.insert(pointerOfVariable,1)
    
                # An anamesa sto ':' kai to 'x' breis ena meion '-' tote einai arnhtikos... 
            elif retrieved_line.find('-', indexOfColonSymbol, indexOfConstraintVariable) != -1:
                # krata th thesi toy meion mesa sth grammh
                indexOfMinus = retrieved_line.find('-')
        
                # An amesws meta to meion breis to 'x' tote...
                if retrieved_line[indexOfMinus+1] == 'x':
                    # o syntelestis tha einai isos me -1
                    AListHelper.insert(pointerOfVariable,-1)
        
                # An anamesa sto symbolo ':' kai to 'x' breis mia teleia '.' tote o syntelestis einai dekadikos...
                elif retrieved_line.find('.', indexOfColonSymbol, indexOfConstraintVariable) != -1:
                    # me mia for syllekse ena-pros-ena ta psifia toy syntelesth sto boithiko string z...
                    for x in range(indexOfColonSymbol+1,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    # antistrepse ton...
                    z = z[::-1]
                    # kai balton sth c ws float.
                    AListHelper.insert(pointerOfVariable,float(z))
                # An den breis teleia '.' tote o syntelestis einai akeraios...
                elif retrieved_line.find('.', indexOfColonSymbol, indexOfConstraintVariable) == -1:
                    # me mia for syllekse ena-pros-ena ta psifia toy syntelesth sto boithitiko string z...
                    for x in range(indexOfMinus,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    # antistrepse ton...
                    z = z[::-1]
                    # kai balton sth c ws int.
                    AListHelper.insert(pointerOfVariable,int(z))
            # An den breis meion '-' tote einai thetikos...
            elif retrieved_line.find('-', indexOfColonSymbol, indexOfConstraintVariable) == -1:
                # An einai dekadikos...
                if retrieved_line.find('.', indexOfColonSymbol, indexOfConstraintVariable) != -1:
                    for x in range(indexOfColonSymbol+1,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    AListHelper.insert(pointerOfVariable,float(z))
                # An einai akeraios...
                elif retrieved_line.find('.', indexOfColonSymbol, indexOfConstraintVariable) == -1:
                    for x in range(indexOfColonSymbol+1,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    AListHelper.insert(pointerOfVariable,int(z))
                    
            # Prepei twra na broyme ti eidoys einai o periorismos poy eksetazoyme kai na enhmerwsoyme to EqinList, elegxontas parallila an exei oristei to eidos toy periorismoy.
            
            # Mas endiaferei an o periorismos einai isothta h kapoios apo tis alles 2 periptwseis opote shmeiwnoyme ton typo toy.
            constraintType = 0
            
            if retrieved_line.find('>=') != -1:
                EqinList.insert(constraintCounter, 1)
                constraintType = 1
                constraintPosition = retrieved_line.find('>=')
            elif retrieved_line.find('<=') != -1:
                EqinList.insert(constraintCounter, -1)
                constraintType = 1
                constraintPosition = retrieved_line.find('<=')
            elif retrieved_line.find('=') != -1:
                EqinList.insert(constraintCounter, 0)
                constraintType = 2
                constraintPosition = retrieved_line.find('=')
            else:
                print('Syntax Error: One of the symbols {<=,>=,=} is missing from the Constraint ',constraintCounter)
                sys.exit('Parser is terminated!')
                
            # Epishs prepei na broume to deksi meros toy periorismoy,elegxontas parallila an yparxei, kai na enimerwsoyme to bList.
            
            # Exontas to eidos toy periosmoy mporoume na kseroyme se poia thesi ths grammhs na perimenoyme na broyme to deksi meros.
            # Stoys periorismoys {<=,>=} tha koitame 2 theseis meta.
            if constraintType == 1:
                
                z = ""
                
                # An ekei broume ton telos tis grammis tote syntax error.
                if retrieved_line[constraintPosition+2] == '\n':
                    print('Syntax Error: Right hand side of Constraint ',constraintCounter,' is missing!')
                    sys.exit('Parser is terminated!')
                    
        
                # An einai dekadikos...
                if retrieved_line.find('.', constraintPosition+2, endOfLine) != -1:
                    for x in range(constraintPosition+2,endOfLine):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    bList.insert(constraintCounter,float(z))
                # An einai akeraios...
                elif retrieved_line.find('.', constraintPosition+2, endOfLine) == -1:
                    for x in range(constraintPosition+2,endOfLine):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    bList.insert(constraintCounter,int(z))
                    
            # Stoys periorismoys isothtas tha koitame 1 thesh meta.       
            if constraintType == 2:
                
                z = ""
                
                # An ekei broume ton telos tis grammis tote syntax error.
                if retrieved_line[constraintPosition+1] == '\n':
                    print('Syntax Error: Right hand side of Constraint ',constraintCounter,' is missing!')
                    sys.exit('Parser is terminated!')
                
                # An einai dekadikos...
                if retrieved_line.find('.', constraintPosition+1, endOfLine) != -1:
                    for x in range(constraintPosition+1,endOfLine):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    bList.insert(constraintCounter,float(z))
                # An einai akeraios...
                elif retrieved_line.find('.', constraintPosition+1, endOfLine) == -1:
                    for x in range(constraintPosition+1,endOfLine):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    bList.insert(constraintCounter,int(z))
            # Ayto to if elegxei thn periptwsh poy exoyme periorismoys pou apoteloyntai apo mono mia metablith!
            if(indexOfNextVariable == -1):
                AMatrixFirstLine = np.asarray(AListHelper)
                # Efoson teliwsame me thn prwth grammh twn periorismwn eidopoioume to programma oti seira exoun oi epomenes grammes twn texnologikwn periorismwn.
                firstLineOfTechnologicalConstraints = 0
                remainingLinesOfTechnologicalConstraints = 1
                firstWhileLoopIteration = 0
                # Mhdenise tous syntelestes olwn twn metablhtwn poy exoyn deikth mikrotero apo ton max deikth toy problhmatos.
                if pointerOfVariable < maxVariable:
                #bale 0 sth lista a stoys syntelestes twn metablhtwn poy paraleipontai.
                    for i in range(pointerOfVariable,maxVariable):
                        AListHelper.insert(i,0) 
                break
            else:        
                firstWhileLoopIteration = 1
                continue
          
        # An eimaste sth prwth seira twn texnologikwn periorismwn kai  OXI sthn prwth epanalipsi toy while...   
        if firstLineOfTechnologicalConstraints == 1 and firstWhileLoopIteration == 1:
            
        
            z = ""
            
            # Stin proigoymeni epanalipsi toy while apothikeysame th metablhth poy tha eksetasoyme twra.
            indexOfConstraintVariable = indexOfNextVariable
            # Briskoume thn epomenh metablhth h opoia tha mas boithisei na eleksoume an anamesa toys yparxei eite to sumbolo '+' eite to '-'.
            indexOfNextVariable = retrieved_line.find('x',indexOfConstraintVariable+1)
            
            # Elegxos an yparxei plus or minus anamesa se kathe metabliti.
            # Arxika elegxoume mipws briskomaste sth teleytaia metablhth giati meta apo ayth den tha yparxei kanena apo ta 2 symbola eks orismoy.
            if retrieved_line.find('x',indexOfConstraintVariable+1,endOfLine) != -1:
                # Ginetai o elegxos kai bganei to katallilo mynhma.
                if retrieved_line.find('+', indexOfConstraintVariable, indexOfNextVariable) == -1 and retrieved_line.find('-',indexOfConstraintVariable, indexOfNextVariable) == -1:
                    print('Constraint Function',constraintCounter,'is incomplete: Math Symbol {+,-} is missing!') 
                    sys.exit("Parser is terminated")
                    
                    
            # Gia na broume ton deikth ths metablhths ayths tha xrhsimopoihsoyme ena while loop.
            # An exoume mia a/kh synarthsh p.x. 'x1 + x100 + x101' gia na broume to deikth ths deuteris metablhths dhladh toy 'x100' tha ksekinisoyme thn anazitisi mia thesi meta to 'x'
            # kai tha stamatisoume otan broume to '+'.
            # Ayto pou allazei se sxesi me thn prwth epanalipsi einai oti twra yparxei h periptwsh poy ftanoume sth teleytaia metablhth (p.x. x101).
            # Edw pera epomenws den mporoume dhladh na oriothetoyme thn anazitisi tws pshfiwn anamesa mono sta '+' h '-' giati h teleytaia metablhth den exei kapoio apo ayta meta ths.
            # Epomenws to while loop tha prepei na termatizei otan brei ena apo ta {<,>,=} pragma poy shmainei oti ekei ksekinaei to deksi meros toy periorismoy.
            # Prosoxh enw to arxeio tha periexei toys periorismoys se morfh {<=,>=,=} emeis sta prwta 2 kanoyme elegxo xwris to iso giati o elegxos ginetai sta symbola ena-pros-ena.
            
            # Arxikopoioyme tis boithikes metablites.
            helpString = ""
            whileLoopCounter = 0
            i = indexOfConstraintVariable + 1
            
            while (retrieved_line[i] != '+' and retrieved_line[i] != '-' and retrieved_line[i] != '<' and retrieved_line[i] != '>' and retrieved_line[i] != '='):
                # Ayksanoyme ton deikth poy metra tis epanalipseis tou while.
                whileLoopCounter = whileLoopCounter + 1
                helpString = retrieved_line[i] + helpString
                i = i + 1
            
            # An kaname perisoteres apo mia epanalipseis tote..
            if whileLoopCounter > 1:
                # Antistrepse to helpString.
                helpString = helpString[::-1]
                # Metatrepse to se int kai dwsto sth metabliti pointerOfVariable.
                pointerOfVariable = int(helpString)
                
            # An kaname mono mia shmainei oti eimastan sthn aplh periptwsh opoy o deikths exei ena mono pshfio to opoio tha einai sth grammh amesws meta th metablhth mas.
            else:
                pointerOfVariable = int(retrieved_line[indexOfConstraintVariable+1])
            
                
            # Prepei twra sthn periptwsh poy gia paradeigma hmastan sthn metablhth x3 kai pigame sthn x6 na mhdenisoyme toys syntelestes olwn ton endiameswn metablhtwn,
            # gia to paradeigma aytoi tha einai: x4, x5.
            
            # Gia na to kanoyme ayto apo ton deikth ths metablitis poy eksetazoyme twra afairoyme ton deikth ths proigoumenis poy apothikeysame sthn prohgoymenh epanalipsi,
            # h diafora toys tha mas dwsei to plithos alla kai tis theseis twn metablitwn twn opoiwn toys syntelestes prepei na mhdenisoyme.
            if pointerOfVariable - pointerOfPreviousVariable > 1:
                for i in range(pointerOfPreviousVariable+1,pointerOfVariable):
                    AListHelper.insert(i,0)
                    
            # Se ayto to shmeio to mono poy leipei gia na proxwrisoyme ston ypologismo toy sentelesth ths metablhths poy eksetazoyme einai h thesi toy symbolou '+' h toy symboloy '-'
            # to opoio panta einai mia thesh pisw akribws apo ton syntelesti poy psaxnoyme.
            # Apo to symbolo ayto tha oriothetisoyme mia anazitish kai sylleksi kathe psifioy toy syntelesti perilambanontas kai to '-' sthn periptwsh poy einai arnhtikos.
            
            
            
            # An einai thetikos...
            if retrieved_line.find('+',indexOfPreviousConstraintVariable,indexOfConstraintVariable) != -1:
                # krata th thesh toy plus mesa sth grammh.
                indexOfPlus = retrieved_line.find('+',indexOfPreviousConstraintVariable,indexOfConstraintVariable)
                # An einai dekadikos...
                if retrieved_line.find('.', indexOfPlus, indexOfConstraintVariable) != -1:
                    for x in range(indexOfPlus+1,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    AListHelper.insert(pointerOfVariable,float(z))
                # An den yparxei syntelestis...
                elif retrieved_line[indexOfPlus+1] == 'x':
                    AListHelper.insert(pointerOfVariable,1)
                # An einai akeraios...
                elif retrieved_line.find('.', indexOfPlus, indexOfConstraintVariable) == -1:
                    for x in range(indexOfPlus+1,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    AListHelper.insert(pointerOfVariable,int(z))
                    
            # An einai arnhtikos...  
            elif retrieved_line.find('-', indexOfPreviousConstraintVariable, indexOfConstraintVariable) != -1:
                # krata th thesi toy meion mesa sth grammh.
                indexOfMinus = retrieved_line.find('-',indexOfPreviousConstraintVariable,indexOfConstraintVariable)
                # An den yparxei sentelestis...
                if retrieved_line[indexOfMinus+1] == 'x':
                    AListHelper.insert(pointerOfVariable,-1)
        
                # An einai dekadikos...
                elif retrieved_line.find('.', indexOfMinus, indexOfConstraintVariable) != -1:
                    for x in range(indexOfMinus,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    AListHelper.insert(pointerOfVariable,float(z))
                # An einai akeraios...
                elif retrieved_line.find('.', indexOfMinus, indexOfConstraintVariable) == -1:
                    for x in range(indexOfMinus,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    AListHelper.insert(pointerOfVariable,int(z)) 
            
            # Elegxoume an exoyme ftasei sth teleytaia metabliti opou kai prepei to while na termatisei.
            if retrieved_line.find('x',indexOfConstraintVariable+1,endOfLine) == -1:
                
            
                if pointerOfVariable < maxVariable:
                #bale 0 sth lista a stoys syntelestes twn metablhtwn poy paraleipontai.
                    for i in range(pointerOfVariable,maxVariable):
                        AListHelper.insert(i,0)
               
                AMatrixFirstLine = np.asarray(AListHelper)
                # Efoson teliwsame me thn prwth grammh twn periorismwn eidopoioume to programma oti seira exoun oi epomenes grammes twn texnologikwn periorismwn.
                firstLineOfTechnologicalConstraints = 0
                remainingLinesOfTechnologicalConstraints = 1
                firstWhileLoopIteration = 0 
                break;
                
            #Telos prepei na proetoimasoyme tis metablites gia tin epomenh epanalipsi.
            indexOfPreviousConstraintVariable = indexOfConstraintVariable
            pointerOfPreviousVariable = pointerOfVariable
        
        # An eimaste stis upoloipes grammes twv texnologikwn periosmwn kai sthn prwth epanalipsi poy ginetai gia kathemia apo tis ypoloipes grammes twn tex/kwn periorismwn.
        if remainingLinesOfTechnologicalConstraints == 1 and firstWhileLoopIteration == 0:
            
            #Arxikopoioume kai pali ton AListHelper giati periexei toys syntelestes toy prwtoy periourismoy ta opoia exoyme apothikeysei ston AAray.
            AListHelper = []
            
            #Ayksanoyme ton deikth poy metra se poio periosmo eimaste wste na enhmerwnontai katallila Eqin and b.
            constraintCounter = constraintCounter  + 1
            
            # Briskoume to index ths prwths metablitis mesa sthn grammh.
            # Kai epishs briskoyme to index kai tis epomenis metablitis,ksekinontas mia anazitisi apo ekei poy brikame th prwth.
            indexOfVariable = retrieved_line.find('x')
            indexOfNextVariable = retrieved_line.find('x',indexOfVariable+1)
        
            # Gia na broyme ton deikth ths metablhths auths akoloythoyme ton eksis algorithmo.
            
            # Arxikopoioyme tis boithikes metablites.
            helpString = ""
            forLoopCounter = 0
            
            # Ksekiname mia for anazitisis mesa sth grammh,arxizontas amesws meta tin thesi tis prwtis metablitis mexri tin thesi thn epomenhs metablitis.
            for i in range(indexOfVariable+1,indexOfNextVariable):
                # Ayksanoyme ton deikth poy metra tis epanalipseis tis for.
                forLoopCounter = forLoopCounter + 1
                # H for tha diakopsei otan ftasoyme eite sto symbolo '+' eite sto '-' kathws ekei akribws einai poy teliwnoyn ta 'psifia' toy deikti tis metablitis mas.
                # Ayto oysiastika ginetai gia tin periptwsi poy deikths einai panw apo 9 (p.x. x10) kai ta psifia einai perisotera apo 1.
                if retrieved_line[i] == '+' or retrieved_line[i] == '-':
                    break;
                # Oso den exoyme brei ta symbola ayta synexise na katagrafeis sto helpString ta psifia toy deikth.
                elif retrieved_line[i] != '+' and retrieved_line[i] != '-':
                    helpString = retrieved_line[i] + helpString
                    i = i + 1
            
            # An kaname perisoteres apo mia epanalipseis tote..
            if forLoopCounter > 1:
                # Antistrepse to helpString.
                helpString = helpString[::-1]
                # Metatrepse to se int kai dwsto sth metabliti pointerOfVariable.
                pointerOfVariable = int(helpString)
                # Apothikeyse th giati tha th xreiastoyme se epomenes epanalipseis.
                pointerOfPreviousVariable = pointerOfVariable
                # An kaname mono mia shmainei oti eimastan sthn apla periptwsh opoy o deikths exei ena mono pshfio to opoio tha einai sth grammh amesws meta th metablhth mas.
            else:
                pointerOfVariable = int(retrieved_line[indexOfVariable+1])
                pointerOfPreviousVariable = pointerOfVariable
            
            
            
            # (An eimaste sth prwth epanalipsi) kai h prwth metabliti den einai to 'x1'...
            if pointerOfVariable > 1:
                #bale 0 sth lista a stoys syntelestes twn metablhtwn poy paraleipontai.
                for i in range(0,pointerOfVariable-1):
                    AListHelper.insert(i,0)
                
            # these thn metablhth poy brikame ws metablhth periorismoy
            indexOfConstraintVariable = indexOfVariable
            
            # To apothikeyoume giati stis epomenes epanalipseis tou while apo edw tha ksekiname thn anazitisi mexri tin epomenh metabliti etsi wste na briskoyme ton
            # syntelesti tis.
            indexOfPreviousConstraintVariable = indexOfVariable
            
            
            # Elegxos an yparxei plus or minus anamesa se kathe metabliti.
            # Arxika elegxoume mipws briskomaste sth teleytaia metablhth giati meta apo ayth den tha yparxei kanena apo ta 2 symbola eks orismoy.
            if retrieved_line.find('x',indexOfConstraintVariable+1,endOfLine) != -1:
                # Elegxos gia to an yparxei {+,-} meta th metablhth.
                if retrieved_line.find('+', indexOfConstraintVariable, indexOfNextVariable) == -1 and retrieved_line.find('-',indexOfConstraintVariable, indexOfNextVariable) == -1:
                    print('Constraint Function',constraintCounter,' is incomplete: Math Symbol {+,-} is missing!')
                    sys.exit("Parser is terminated")
            
            # Edw pera oriothetoume thn anazitisi toy suntelesth ths prwths metablhths toy periorismoy apo to prwto xarakthra ths grammhs ayths.   
                      
            # An o prwtos xarakthras ths grammhs einai to 'x'...(dhladh den grafetai kapoios syntelestis gia thn metablith)
            if retrieved_line[0] == 'x':
                # tote o syntelestis tha einai isos me 1
                AListHelper.insert(pointerOfVariable,1)
    
                # An o prwtos xarakthras ths grammhs einai to '-' tote o syntelesths einai arnhtikos... 
            elif retrieved_line[0] == '-':
                # krata th thesi toy meion mesa sth grammh
                indexOfMinus = 0
        
                # An amesws meta to meion breis to 'x' tote...
                if retrieved_line[indexOfMinus+1] == 'x':
                    # o syntelestis tha einai isos me -1
                    AListHelper.insert(pointerOfVariable,-1)
        
                # An anamesa sto '-' kai to 'x' breis mia teleia '.' tote o syntelestis einai dekadikos...
                elif retrieved_line.find('.', indexOfMinus, indexOfConstraintVariable) != -1:
                    # me mia for syllekse ena-pros-ena ta psifia toy syntelesth sto boithiko string z...
                    for x in range(indexOfMinus,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    # antistrepse ton...
                    z = z[::-1]
                    # kai balton sth c ws float.
                    AListHelper.insert(pointerOfVariable,float(z))
                # An den breis teleia '.' tote o syntelestis einai akeraios...
                elif retrieved_line.find('.', indexOfMinus, indexOfConstraintVariable) == -1:
                    # me mia for syllekse ena-pros-ena ta psifia toy syntelesth sto boithitiko string z...
                    for x in range(indexOfMinus,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    # antistrepse ton...
                    z = z[::-1]
                    # kai balton sth c ws int.
                    AListHelper.insert(pointerOfVariable,int(z))
            # An den breis meion '-' tote einai thetikos...
            elif retrieved_line[0] != '-':
                # An einai dekadikos...
                if retrieved_line.find('.', 0, indexOfConstraintVariable) != -1:
                    for x in range(0,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    AListHelper.insert(pointerOfVariable,float(z))
                # An einai akeraios...
                elif retrieved_line.find('.', 0, indexOfConstraintVariable) == -1:
                    for x in range(0,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    AListHelper.insert(pointerOfVariable,int(z))
                    
            # Prepei twra na broyme ti eidoys einai o periorismos poy eksetazoyme kai na enhmerwsoyme to EqinList, elegxontas parallila an exei oristei to eidos toy periorismoy.
            
            # Mas endiaferei an o periorismos einai isothta h kapoios apo tis alles 2 periptwseis opote shmeiwnoyme ton typo toy.
            constraintType = 0
            if retrieved_line.find('>=') != -1:
                EqinList.insert(constraintCounter, 1)
                constraintType = 1
                constraintPosition = retrieved_line.find('>=')
            elif retrieved_line.find('<=') != -1:
                EqinList.insert(constraintCounter, -1)
                constraintType = 1
                constraintPosition = retrieved_line.find('<=')
            elif retrieved_line.find('=') != -1:
                EqinList.insert(constraintCounter, 0)
                constraintType = 2
                constraintPosition = retrieved_line.find('=')
            else:
                print('Syntax Error: One of the symbols {<=,>=,=} is missing from the Constraint ',constraintCounter)
                sys.exit('Parser is terminated!')
            
            # Epishs prepei na broume to deksi meros toy periorismoy,elegxontas parallila an yparxei, kai na enimerwsoyme to bList.
            
            # Exontas to eidos toy periosmoy mporoume na kseroyme se poia thesi ths grammhs na perimenoyme na broyme to deksi meros.
            # Stoys periorismoys {<=,>=} tha koitame 2 theseis meta.
            if constraintType == 1:
                
                z = ""
                
                # An ekei broume ton telos tis grammis tote syntax error.
                if retrieved_line[constraintPosition+2] == '\n':
                    print('Syntax Error: Right hand side of Constraint ',constraintCounter,' is missing!')
                    sys.exit('Parser is terminated!')
                    
        
                # An einai dekadikos...
                if retrieved_line.find('.', constraintPosition+2, endOfLine) != -1:
                    for x in range(constraintPosition+2,endOfLine):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    bList.insert(constraintCounter,float(z))
                # An einai akeraios...
                elif retrieved_line.find('.', constraintPosition+2, endOfLine) == -1:
                    for x in range(constraintPosition+2,endOfLine):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    bList.insert(constraintCounter,int(z))
            
             
            # Stoys periorismoys isothtas tha koitame 1 thesh meta.       
            if constraintType == 2:
                
                z = ""
                
                # An ekei broume ton telos tis grammis tote syntax error.
                if retrieved_line[constraintPosition+1] == '\n':
                    print('Syntax Error: Right hand side of Constraint ',constraintCounter,' is missing!')
                    sys.exit('Parser is terminated!')
                
                # An einai dekadikos...
                if retrieved_line.find('.', constraintPosition+1, endOfLine) != -1:
                    for x in range(constraintPosition+1,endOfLine):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    bList.insert(constraintCounter,float(z))
                # An einai akeraios...
                elif retrieved_line.find('.', constraintPosition+1, endOfLine) == -1:
                    for x in range(constraintPosition+1,endOfLine):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    bList.insert(constraintCounter,int(z))
            
            
            # Elegxoume an exoyme ftasei sth teleytaia metabliti opou kai prepei to while na termatisei.
            if retrieved_line.find('x',indexOfConstraintVariable+1,endOfLine) == -1:
                
                
                if pointerOfVariable < maxVariable:
                #bale 0 sth lista a stoys syntelestes twn metablhtwn poy paraleipontai.
                    for i in range(pointerOfVariable,maxVariable):
                        AListHelper.insert(i,0)
                
                
                
                # To programma antimetwpizei diaforetika thn prwth grammh twn periorismwn poy periexei to s.t. kai alliws ta remaining lines tws periorismwn.
                # Sthn prwth toy epanalipsi ayto to kommati toy algorithmoy prepei na syndesei thn prwth grammh periorismwn me thn deyterh mesa ston teliko AMatrix mesw ths vstack.
                if firstIfFlag == 1:
                    AMatrixSecondLine = np.asarray(AListHelper)
                    FinalAMatrix = np.vstack((AMatrixFirstLine,AMatrixSecondLine))
                    firstIfFlag = 0
                # kai apo th deyterh epanalipsi kai meta prepei na syndeei kathe grammi periorismwn poy ypologizei ston teliko AMatrix.
                else:
                    AMatrixRemainingLine = np.asarray(AListHelper)
                    FinalAMatrix = np.vstack((FinalAMatrix,AMatrixRemainingLine))
                break
                
            firstWhileLoopIteration = 1
            continue
        
        # An eksetazoume tis ypoloipes grammes twn texn/kwn periorismwn kai den eimaste sthn prwth epanalhpsh toy while gia kathemia apo aytes...
        if remainingLinesOfTechnologicalConstraints == 1 and firstWhileLoopIteration == 1:
            
            z = ""
            
            # Stin proigoymeni epanalipsi toy while apothikeysame th metablhth poy tha eksetasoyme twra.
            indexOfConstraintVariable = indexOfNextVariable
            
            # Briskoume thn epomenh metablhth h opoia tha mas boithisei na eleksoume an anamesa toys yparxei eite to sumbolo '+' eite to '-'.
            indexOfNextVariable = retrieved_line.find('x',indexOfConstraintVariable+1)
            
            # Elegxos an yparxei plus or minus anamesa se kathe metabliti.
            # Arxika elegxoume mipws briskomaste sth teleytaia metablhth giati meta apo ayth den tha yparxei kanena apo ta 2 symbola eks orismoy.
            if retrieved_line.find('x',indexOfConstraintVariable+2,endOfLine) != -1:
                # Ginetai o elegxos kai bganei to katallilo mynhma.
                if retrieved_line.find('+', indexOfConstraintVariable, indexOfNextVariable) == -1 and retrieved_line.find('-',indexOfConstraintVariable, indexOfNextVariable) == -1:
                    print('Constraint Function',constraintCounter,'is incomplete: Math Symbol {+,-} is missing!') 
                    sys.exit("Parser is terminated")
            
            # Gia na broume ton deikth ths metablhths ayths tha xrhsimopoihsoyme ena while loop.
            # An exoume mia a/kh synarthsh p.x. 'x1 + x100 + x101' gia na broume to deikth ths deuteris metablhths dhladh toy 'x100' tha ksekinisoyme thn anazitisi mia thesi meta to 'x'
            # kai tha stamatisoume otan broume to '+'.
            # Ayto pou allazei se sxesi me thn prwth epanalipsi einai oti twra yparxei h periptwsh poy ftanoume sth teleytaia metablhth (p.x. x101).
            # Edw pera epomenws den mporoume dhladh na oriothetoyme thn anazitisi tws pshfiwn anamesa mono sta '+' h '-' giati h teleytaia metablhth den exei kapoio apo ayta meta ths.
            # Epomenws to while loop tha prepei na termatizei otan brei ena apo ta {<,>,=} pragma poy shmainei oti ekei ksekinaei to deksi meros toy periorismoy.
            # Prosoxh enw to arxeio tha periexei toys periorismoys se morfh {<=,>=,=} emeis sta prwta 2 kanoyme elegxo xwris to iso giati o elegxos ginetai sta symbola ena-pros-ena.
            
            # Arxikopoioyme tis boithikes metablites.
            helpString = ""
            whileLoopCounter = 0
            i = indexOfConstraintVariable + 1
            
            while (retrieved_line[i] != '+' and retrieved_line[i] != '-' and retrieved_line[i] != '<' and retrieved_line[i] != '>' and retrieved_line[i] != '='):
                # Ayksanoyme ton deikth poy metra tis epanalipseis tou while.
                whileLoopCounter = whileLoopCounter + 1
                helpString = retrieved_line[i] + helpString
                i = i + 1
            
            # An kaname perisoteres apo mia epanalipseis tote..
            if whileLoopCounter > 1:
                # Antistrepse to helpString.
                helpString = helpString[::-1]
                # Metatrepse to se int kai dwsto sth metabliti pointerOfVariable.
                pointerOfVariable = int(helpString)
                
            # An kaname mono mia shmainei oti eimastan sthn aplh periptwsh opoy o deikths exei ena mono pshfio to opoio tha einai sth grammh amesws meta th metablhth mas.
            else:
                pointerOfVariable = int(retrieved_line[indexOfConstraintVariable+1])
                
            # Prepei twra sthn periptwsh poy gia paradeigma hmastan sthn metablhth x3 kai pigame sthn x6 na mhdenisoyme toys syntelestes olwn ton endiameswn metablhtwn,
            # gia to paradeigma aytoi tha einai: x4, x5.
            
            # Gia na to kanoyme ayto apo ton deikth ths metablitis poy eksetazoyme twra afairoyme ton deikth ths proigoumenis poy apothikeysame sthn prohgoymenh epanalipsi,
            # h diafora toys tha mas dwsei to plithos alla kai tis theseis twn metablitwn twn opoiwn toys syntelestes prepei na mhdenisoyme.
            if pointerOfVariable - pointerOfPreviousVariable > 1:
                for i in range(pointerOfPreviousVariable+1,pointerOfVariable):
                    AListHelper.insert(i,0)
                    
            # Se ayto to shmeio to mono poy leipei gia na proxwrisoyme ston ypologismo toy sentelesth ths metablhths poy eksetazoyme einai h thesi toy symbolou '+' h toy symboloy '-'
            # to opoio panta einai mia thesh pisw akribws apo ton syntelesti poy psaxnoyme.
            # Apo to symbolo ayto tha oriothetisoyme mia anazitish kai sylleksi kathe psifioy toy syntelesti perilambanontas kai to '-' sthn periptwsh poy einai arnhtikos.
            
            
            
            # An einai thetikos...
            if retrieved_line.find('+',indexOfPreviousConstraintVariable,indexOfConstraintVariable) != -1:
                # krata th thesh toy plus mesa sth grammh.
                indexOfPlus = retrieved_line.find('+',indexOfPreviousConstraintVariable,indexOfConstraintVariable)
                # An einai dekadikos...
                if retrieved_line.find('.', indexOfPlus, indexOfConstraintVariable) != -1:
                    for x in range(indexOfPlus+1,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    AListHelper.insert(pointerOfVariable,float(z))
                # An den yparxei syntelestis...
                elif retrieved_line[indexOfPlus+1] == 'x':
                    AListHelper.insert(pointerOfVariable,1)
                # An einai akeraios...
                elif retrieved_line.find('.', indexOfPlus, indexOfConstraintVariable) == -1:
                    for x in range(indexOfPlus+1,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    AListHelper.insert(pointerOfVariable,int(z))
                    
            # An einai arnhtikos...  
            elif retrieved_line.find('-', indexOfPreviousConstraintVariable, indexOfConstraintVariable) != -1:
                # krata th thesi toy meion mesa sth grammh.
                indexOfMinus = retrieved_line.find('-',indexOfPreviousConstraintVariable,indexOfConstraintVariable)
                # An den yparxei sentelestis...
                if retrieved_line[indexOfMinus+1] == 'x':
                    AListHelper.insert(pointerOfVariable,-1)
        
                # An einai dekadikos...
                elif retrieved_line.find('.', indexOfMinus, indexOfConstraintVariable) != -1:
                    for x in range(indexOfMinus,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    AListHelper.insert(pointerOfVariable,float(z))
                # An einai akeraios...
                elif retrieved_line.find('.', indexOfMinus, indexOfConstraintVariable) == -1:
                    for x in range(indexOfMinus,indexOfConstraintVariable):
                        z = retrieved_line[x] + z
                    z = z[::-1]
                    AListHelper.insert(pointerOfVariable,int(z)) 
            
            # Elegxoume an exoyme ftasei sth teleytaia metabliti opou kai prepei to while na termatisei.
            if retrieved_line.find('x',indexOfConstraintVariable+1,endOfLine) == -1:
                
                if pointerOfVariable < maxVariable:
                #bale 0 sth lista a stoys syntelestes twn metablhtwn poy paraleipontai.
                    for i in range(pointerOfVariable,maxVariable):
                        AListHelper.insert(i,0)
                
                # To programma antimetwpizei diaforetika thn prwth grammh twn periorismwn poy periexei to s.t. kai alliws ta remaining lines tws periorismwn.
                # Sthn prwth toy epanalipsi ayto to kommati toy algorithmoy prepei na syndesei thn prwth grammh periorismwn me thn deyterh mesa ston teliko AMatrix mesw ths vstack.
                if firstIfFlag == 1:
                    AMatrixSecondLine = np.asarray(AListHelper)
                    FinalAMatrix = np.vstack((AMatrixFirstLine,AMatrixSecondLine))
                # kai apo th deyterh epanalipsi kai meta prepei na syndeei kathe grammi periorismwn poy ypologizei ston teliko AMatrix.
                else:
                    AMatrixRemainingLine = np.asarray(AListHelper)
                    FinalAMatrix = np.vstack((FinalAMatrix,AMatrixRemainingLine))
                firstIfFlag = 0
                firstWhileLoopIteration = 0
                       
                
                break;
                
            #Telos prepei na proetoimasoyme tis metablites gia tin epomenh epanalipsi.
            indexOfPreviousConstraintVariable = indexOfConstraintVariable
            pointerOfPreviousVariable = pointerOfVariable
            
     
# Sto teleytaio kommati dhmioyrgoume to txt arxeio opoy tha apothikeutei to dyiko problhma kai kanoyme thn metatroph.        
file = open("LP2.txt", "a")

# Analoga me to eidos ths beltistopoihshs toy prwteywn problhmatos ektypvnoyme thn antistofh gia to dyiko.
if MinMax == 1:
    file.write("min z = ")
else:
    file.write("max z = ")
    
# Gia na dhmioyrghsoyme tin antikeimenikh synartish toy duikoy tha paroyme enas pros ena ta stoixeia toy bList,
# dhladh thn lista poy periexei ta deksia merh twn periorismwn.
numberOfConstraints = len(bList)

# O counter paizei ton rolo toy deikth kathe metablitis sthn a/kh synartish kai toys periorismoys.
# p.x. ta 1,2 stis metablites ta w1,w2.
counter = 1

# Diasxizoyme tin lista b (deksia merh).
for i in range(0,numberOfConstraints):
    # Otan synantame mhdeniko deksio meros to prospername giati den grafetai sthn antikeimenikh synarthsh.
    if bList[i] == 0:
        counter = counter + 1
        continue
    # Gia tin prwth metablhth, h ektypwsh diaferei se sxesh me tis alles giati den mas endiaferei sthn periptwsh poy einai thetikos o syntelestis na shmeiwsoyme to proshmo toy.
    if counter == 1:
        # An einai arnhtikos o syntelestis..
        if bList[i] < 0:
            # kai oxi monadiaios, tote shmeiwse ton syntelesti mazi me ena meion.
            if bList[i] != -1:
                bListHelper = bList[i]*(-1)
                file.write('-')
                file.write(str(bListHelper))
                file.write('w')
                file.write(str(counter))
                counter = counter + 1
            # alliws (an einai monadiaios) shmeiwse mono ena meion prin th metablhth.
            else:
                file.write("-w",counter)
                file.write(str(counter))
                counter = counter + 1
        # An einai monadiaios.. shmeiwse mono thn metablhth xwris ton syntelesti.
        elif bList[i] == 1:
            file.write("w")
            file.write(str(counter))
            counter = counter + 1
        # Alliws an einai thetikos kai diaforos ths monadas o syntelestis shmeiwse ton.
        else:
            file.write(str(bList[i]))
            file.write('w')
            file.write(str(counter))
            counter = counter + 1
    # An den eksetazoyme thn prwth metablhth..
    else:
        if bList[i] < 0:
            if bList[i] != -1:
                bListHelper = bList[i]*(-1)
                file.write(' - ')
                file.write(str(bListHelper))
                file.write('w')
                file.write(str(counter))
                counter = counter + 1
            else:
                file.write('- w')
                file.write(str(counter))
                counter = counter + 1
        elif bList[i] == 1:
            file.write('w')
            file.write(str(counter))
        # edw einai h mono diafora me ton parapanw kwdika ths prwths metablhths,
        # kathws shmeiwnoyme kai to proshmo '+' prin kathe metablith me thetiko syntelesti.
        else:
            file.write(' + ')
            file.write(str(bList[i]))
            file.write('w')
            file.write(str(counter))
            counter = counter + 1


# Ksekiname thn epeksergasia twn perioristikwn syntelestwn, oi opoioi prokyptoun kanontas transpose ton arxiko pinaka toy prwteywn problhmatos.
PrimalAMatrix = np.matrix(FinalAMatrix)
DualAMatrix = np.transpose(PrimalAMatrix)

# Katagrafoyme tis diastaseis toy pinaka se metablites.
numberOfRows = DualAMatrix.shape[0]
numberOfColumns = DualAMatrix.shape[1]

file.write('\n')
file.write('s.t.')

# Diasxizoyme ton pinaka twn periostikwn syntelestwn.
for i in range(0,numberOfRows):
    # O counter paizei kai pali ton rolo toy deikth.
    counter = 1
    file.write('\n')
    
    # H epeksergasia kai h ektypwsh twn stoixeiwn toy pinaka ginetai me panomoitypo tropo me thn parapanw epekshghsh.
    for j in range(0,numberOfColumns):
        
        # otan synantame mhdeniko syntelesti ton prospername alla prwta elegxoyme mhpws htan o teleytaios toy periorismoy aytoy..
        if DualAMatrix[i,j] == 0:
            counter = counter + 1
            # ..giati an einai o teleytaios, tha prepei na oloklhrwsoyme ton periosmo bazontas to symbolo poy orizei to eidos toy {<=,>=,=} alla kai to deksi meros toy.
            # gia to eidos toy periorismoy koitame an to problhma einai min h max kathws exoyme ws dedomeno oti sto prwteyon oi metablites einai >= 0.
            # gia to deksi meros koitame toys syntelestes tis antikeimenikhs synarthshs toy prwteywn problhmatos.
            if j == numberOfColumns-1: 
                if MinMax == 1: 
                    file.write(' >= ')
                    file.write(str(cList[i]))  
                elif MinMax == -1:
                    file.write(' <= ')
                    file.write(str(cList[i]))
            continue
        if counter == 1:
            if DualAMatrix[i,j] < 0:
                if DualAMatrix[i,j] != -1:
                    DualAMatrixHelper = DualAMatrix[i,j]*(-1)
                    file.write('-')
                    file.write(str(DualAMatrixHelper))
                    file.write('w')
                    file.write(str(counter))
                    counter = counter + 1
                else:
                    file.write('-w')
                    file.write(str(counter))
                    counter = counter + 1
            elif DualAMatrix[i,j] == 1:
                file.write('w')
                file.write(str(counter))
                counter = counter + 1
            else:
                file.write(str(DualAMatrix[i,j]))
                file.write('w')
                file.write(str(counter))
                counter = counter + 1
        else:
            if DualAMatrix[i,j] < 0:
                if DualAMatrix[i,j] != -1:
                    DualAMatrixHelper = DualAMatrix[i,j]*(-1)
                    file.write(' - ')
                    file.write(str(DualAMatrixHelper))
                    file.write('w')
                    file.write(str(counter))
                    counter = counter + 1
                else:
                    file.write('- w')
                    file.write(str(counter))
                    counter = counter + 1
            elif DualAMatrix[i,j] == 1:
                file.write(' + w')
                file.write(str(counter))
                counter = counter + 1
            else:
                file.write(' + ')
                file.write(str(DualAMatrix[i,j]))
                file.write('w')
                file.write(str(counter))
                counter = counter + 1
        # Kathe fora poy teliwnoyme me mia sthlh elegxoyme mhpws htan h teleytaia giati tote tha prepei na oloklhrwsoyme ton periorismo me to deksi meros kai to antoisixo symbolo.
        if j == numberOfColumns-1: 
            if MinMax == 1: 
                file.write(' >= ')
                file.write(str(cList[i]))  
            elif MinMax == -1:
                file.write(' <= ')
                file.write(str(cList[i]))

file.write('\n')
counter = 1

# Telos shmeiwnoyme gia kathe metabliti to pedio orismoy ths analoga me to eidos ths beltistopoihshs toy prwteywn problhmatos alla kai analoga me to eidos twn periorismwn toy prwteywn kai pali problhmatos.
for i in range(0,numberOfConstraints):
    if MinMax == 1:
        if EqinList[i] == -1:
            file.write('w')
            file.write(str(counter))
            file.write(' >= 0, ')
            counter = counter + 1
        if EqinList[i] == 0:
            file.write('w')
            file.write(str(counter))
            file.write('-eleutheri, ')
            counter = counter + 1
        if EqinList[i] == 1:
            file.write('w')
            file.write(str(counter))
            file.write(' <= 0, ')
            counter = counter + 1
    if MinMax == -1:
        if EqinList[i] == -1:
            file.write('w')
            file.write(str(counter))
            file.write(' <= 0, ')
            counter = counter + 1
        if EqinList[i] == 0:
            file.write('w')
            file.write(str(counter))
            file.write('-eleutheri, ')
            counter = counter + 1
        if EqinList[i] == 1:
            file.write('w')
            file.write(str(counter))
            file.write(' >= 0, ')
            counter = counter + 1
