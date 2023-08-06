def syntacticAnaliz(inputW, root, OT, FEL, OLMOSH, NUMBER, SIFAT, model):
    #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
    inputl = list()
    turkuml = list()
    rootl = list()
    suffixl = list()
    analizl = list()
    syntantic = list()
    #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
    #simplejson.dumps({'aaData': root}
    root_3 = list()
    stem = list()
    a = ''
    yx = ''
    otstem = ''
    felstem = ''
    olmoshstem = ''
    numberstem = ''
    sifatstem = ''
    boglamastem = ''
    ravishdosh = ''
    ravish = ''
    sifatdosh = ''
    harakatnomi = ''
    invword = ''
    inturkum = '' 
    if inputW is not None:
        inputext2 = inputW.split()
        for w in inputext2:
            w1 = w.replace("‘", "`")
            w2 = w1.replace("'", "`")
            w3 = w2.replace("’", "`")
            w4 = w3.replace('"', '')
            w5 = w4.replace('“', '') 
            w6 = w5.replace('”', '') 
            w = w6
            stem.append(w.lower())
    for i in stem:
        yx = ''
        ry = ''
        for y in i:
            yx += y
            for r in root:
                if yx == r['lotin']:
                    if r['turkum'] == 'NOUN' or r['turkum'] == 'VOUN':
                        otstem = yx
                    if r['turkum'] == 'VERB':
                        felstem = yx
                    if r['turkum'] == 'P':
                        olmoshstem = yx
                    if r['turkum'] == 'NUM':
                        numberstem = yx
                    if r['turkum'] == 'ADJ':
                        sifatstem = yx
                    if r['turkum'] == 'CONJ':
                        boglamastem = yx
                    if r['turkum'] == 'V_P':
                        ravishdosh = yx
                    if r['turkum'] == 'V_N':
                        harakatnomi = yx
                    if r['turkum'] == 'ADV':
                        ravish = yx
                    if r['turkum'] == 'V_O':
                        sifatdosh = yx
                    else:
                        invword = yx
                        inturkum = r['turkum']

        #########################################
        #syntantic(felstem)
        #syntantic(str(otstem))
        diffsifatdosh = i.replace(sifatdosh, "")#get suffix ot
        if diffsifatdosh == sifatdosh:
            diffsifatdosh = ''
        diffravish = i.replace(ravish, "")#get suffix ot
        if diffravish == ravish:
            diffravish = ''
        diffharakatnomi = i.replace(harakatnomi, "")#get suffix ot
        if diffharakatnomi == harakatnomi:
            diffharakatnomi = ''
        diffravishdosh = i.replace(ravishdosh, "")#get suffix ot
        if diffravishdosh == ravishdosh:
            diffravishdosh = ''
        diffboglama = i.replace(boglamastem, "")#get suffix ot
        if diffboglama == boglamastem:
            diffboglama = ''
        diffot = i.replace(otstem, "")#get suffix ot
        if diffot == otstem:
            diffot = ''
        difffel = i.replace(felstem, "")#get suffix fel
        if difffel == felstem:
            difffel = ''
        diffolmosh = i.replace(olmoshstem, "")#get suffix fel
        if diffolmosh == olmoshstem:
            diffolmosh = ''
        diffnumber = i.replace(numberstem, "")#get suffix fel
        if diffnumber == numberstem: 
            diffnumber = ''
        diffsifat = i.replace(sifatstem, "")#get suffix fel
        if diffsifat == sifatstem: 
            diffsifat = ''
        ###############################################
        ###############################################
        analizsifat = ''
        analiznumber = ''
        analizolmosh = ''
        analizfel = ''
        analizot = '' 
        if len(otstem) > len(sifatdosh) and len(otstem) > len(ravish) and len(otstem) > len(harakatnomi) and len(otstem) > len(ravishdosh) and len(otstem) > len(boglamastem) and len(otstem) > len(felstem) and len(otstem) > len(olmoshstem) and len(otstem) > len(numberstem) and len(otstem) > len(sifatstem):
            analizot = findOtSuffix(OT, diffot)      
        if len(felstem) > len(sifatdosh) and  len(felstem) > len(ravish) and len(felstem) > len(harakatnomi) and len(felstem) > len(ravishdosh) and len(felstem) > len(boglamastem) and len(felstem) > len(otstem) and len(felstem) > len(olmoshstem) and len(felstem) > len(numberstem) and len(felstem) > len(sifatstem):                
            analizfel = findOtSuffix(FEL, difffel)   
        if len(olmoshstem) > len(sifatdosh) and len(olmoshstem) > len(ravish) and len(olmoshstem) > len(harakatnomi) and len(olmoshstem) > len(ravishdosh) and len(olmoshstem) > len(boglamastem) and len(olmoshstem) > len(otstem) and len(olmoshstem) > len(felstem) and len(olmoshstem) > len(numberstem) and len(olmoshstem) > len(sifatstem):                
            analizolmosh = findOtSuffix(OLMOSH, diffolmosh)
        if len(numberstem) > len(sifatdosh) and len(numberstem) > len(ravish) and len(numberstem) > len(harakatnomi) and len(numberstem) > len(ravishdosh) and len(numberstem) > len(boglamastem) and len(numberstem) > len(felstem) and len(numberstem) > len(olmoshstem) and len(numberstem) > len(otstem) and len(numberstem) > len(sifatstem):
            analiznumber = findOtSuffix(NUMBER, diffnumber)      
        if len(sifatstem) > len(sifatdosh) and len(sifatstem) > len(ravish) and len(sifatstem) > len(harakatnomi) and len(sifatstem) > len(ravishdosh) and len(sifatstem) > len(boglamastem) and len(sifatstem) > len(felstem) and len(sifatstem) > len(olmoshstem) and len(sifatstem) > len(numberstem) and len(sifatstem) > len(otstem):
            analizsifat = findOtSuffix(SIFAT, diffsifat)
        ###############################################
        count = 0;
        #agar so`z topilas va qo`shimchasi bo`lsa va qo`shimcha bazadagi qo`shimchalarga mos kelsa` 
        if len(analizot.replace(" Modeli: ->", "")) > 0 and len(otstem) > 0:
            root_3.append('Input:'+i+'->Root word: '+otstem+"->Turkum: NOUN"+'->Suffix:'+diffot+"->Analiz noun:"+analizot)
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            inputl.append(i)
            rootl.append(otstem)
            turkuml.append("NOUN")
            suffixl.append(diffot)
            analizl.append(analizot)
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)    
            otstem = ''
            diffot = ''
            analizot = ''
            count +=1
        if len(analizfel.replace(" Modeli: ->", "")) > 0 and len(felstem) > 0:  
            root_3.append('Input:'+i+'->Root word: '+felstem+"->Turkum: VERB"+'->Suffix:'+difffel+"->Analiz Verb:"+analizfel)    
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            inputl.append(i)
            rootl.append(felstem)
            turkuml.append("VERB")
            suffixl.append(difffel)
            analizl.append(analizfel)
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            felstem = ''
            difffel = ''
            analizfel = ''
            count +=1
        if len(analizolmosh.replace(" Modeli: ->", "")) > 0 and len(olmoshstem) > 0:  
            root_3.append('Input:'+i+'->Root word: '+olmoshstem+"->Turkum: PRONOUN"+'->Suffix:'+diffolmosh+"->Analiz Pronoun:"+analizolmosh)
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)    
            inputl.append(i)
            rootl.append(olmoshstem)
            turkuml.append("PRONOUN")
            suffixl.append(diffolmosh)
            analizl.append(analizolmosh)
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            olmoshstem = ''
            diffolmosh = ''
            analizolmosh = ''
            count +=1
        if len(analiznumber.replace(" Modeli: ->", "")) > 0 and len(numberstem) > 0:  
            root_3.append('Input:'+i+'->Root word: '+numberstem+"->Turkum: NUMBER"+'->Suffix:'+diffnumber+"->Analiz Num:"+analiznumber)
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)    
            inputl.append(i)
            rootl.append(numberstem)
            turkuml.append("NUMBER")
            suffixl.append(diffnumber)
            analizl.append(analiznumber)
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            numberstem = ''
            diffnumber = ''
            analiznumber = ''
            count +=1
        if len(analizsifat.replace(" Modeli: ->", "")) > 0 and len(sifatstem) > 0:  
            root_3.append('Input:'+i+'->Root word: '+sifatstem+"->Turkum: ADJECTIVE"+'->Suffix:'+diffsifat+"->Analiz ADJ:"+analizsifat)
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)       
            inputl.append(i)
            rootl.append(sifatstem)
            turkuml.append("ADJECTIVE")
            suffixl.append(diffsifat)
            analizl.append(analizsifat)
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            sifatstem = ''
            diffsifat = ''
            analizsifat = ''
            count +=1
        #agar so`z topils va qo`shimchasi bo`lsa va qo`shimcha bazadagi qo`shimchalarga mos kelsa` 
        #agar so`z bazada topilsa va qo`shimchasi bo`lmasa
        #agar so`z bazada topilsa va qo`shimchasi bo`lmasa
        if len(diffsifatdosh) == 0 and len(sifatdosh) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
            root_3.append('Input:'+i+'->Root word: '+sifatdosh+"->Turkum: V_O"+'->Suffix: NONE->Analiz V_O: NONE')
            inputl.append(i)
            rootl.append(sifatdosh)
            turkuml.append("V_O") 
            suffixl.append("NONE")
            analizl.append("NONE")
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            otstem = ''
            diffot = ''
            analizot = '' 
            count +=1

        if len(diffravish) == 0 and len(ravish) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
            root_3.append('Input:'+i+'->Root word: '+ravish+"->Turkum: ADV"+'->Suffix: NONE->Analiz ADV: NONE')
            inputl.append(i)
            rootl.append(ravish)
            turkuml.append("ADV") 
            suffixl.append("NONE")
            analizl.append("NONE")
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            otstem = ''
            diffot = ''
            analizot = ''
            count +=1

        if len(diffharakatnomi) == 0 and len(harakatnomi) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
            root_3.append('Input:'+i+'->Root word: '+harakatnomi+"->Turkum: V_N"+'->Suffix: NONE->Analiz V_N: NONE')
            inputl.append(i)
            rootl.append(harakatnomi)
            turkuml.append("V_N") 
            suffixl.append("NONE")
            analizl.append("NONE")
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            otstem = ''
            diffot = ''
            analizot = ''
            count +=1

        if len(diffravishdosh) == 0 and len(ravishdosh) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
            root_3.append('Input:'+i+'->Root word: '+ravishdosh+"->Turkum: V_P"+'->Suffix: NONE->Analiz V_P: NONE')
            inputl.append(i)
            rootl.append(ravishdosh)
            turkuml.append("V_P") 
            suffixl.append("NONE")
            analizl.append("NONE")
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            otstem = ''
            diffot = ''
            analizot = ''
            count +=1

        if len(diffboglama) == 0 and len(boglamastem) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
            root_3.append('Input:'+i+'->Root word: '+boglamastem+"->Turkum: CONJ"+'->Suffix: NONE->Analiz CONJ: NONE')
            inputl.append(i)
            rootl.append(boglamastem)
            turkuml.append("CONJ")
            suffixl.append("NONE")
            analizl.append("NONE")
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            otstem = ''
            diffot = ''
            analizot = ''
            count +=1

        if len(diffot) == 0 and len(otstem) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
            root_3.append('Input:'+i+'->Root word: '+otstem+"->Turkum: NOUN"+'->Suffix: NONE->Analiz Noun: NONE')
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            inputl.append(i)
            rootl.append(otstem)
            turkuml.append("NOUN")
            suffixl.append("NONE")
            analizl.append("NONE")
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            otstem = ''
            diffot = ''
            analizot = ''
            count +=1
        if len(difffel) == 0 and len(felstem) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
            root_3.append('Input:'+i+'->Root word: '+felstem+"->Turkum: VERB"+'->Suffix: VERB->Analiz Noun: NONE')
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            inputl.append(i)
            rootl.append(felstem)
            turkuml.append("V")
            suffixl.append("NONE")
            analizl.append("NONE")
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            felstem = ''
            difffel = ''
            analizfel = ''
            count +=1
        if len(diffolmosh) == 0 and len(olmoshstem) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
            root_3.append('Input:'+i+'->Root word: '+olmoshstem+"->Turkum: PRONOUN"+'->Suffix: NONE->Analiz Pronoun: NONE')
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            inputl.append(i)
            rootl.append(olmoshstem)
            turkuml.append("P")
            suffixl.append("NONE")
            analizl.append("NONE")
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            olmoshstem = ''
            diffolmosh = ''
            analizolmosh = ''
            count +=1
        if len(diffnumber) == 0 and len(numberstem) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
            root_3.append('Input:'+i+'->Root word: '+numberstem+"->Turkum: NUMBER"+'->Suffix: NONE->Analiz NUMBER: NONE')
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            inputl.append(i)
            rootl.append(numberstem)
            turkuml.append("NUM")
            suffixl.append("NONE")
            analizl.append("NONE")
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            numberstem = ''
            diffnumber = ''
            analiznumber = ''
            count +=1
        if len(diffsifat) == 0 and len(sifatstem) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
            root_3.append('Input:'+i+'->Root word: '+sifatstem+"->Turkum: ADJ"+'->Suffix: NONE->Analiz ADJ: NONE')
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            inputl.append(i)
            rootl.append(sifatstem)
            turkuml.append("ADJ")
            suffixl.append("NONE")
            analizl.append("NONE")
            #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
            sifatstem = ''
            diffsifat = ''
            analizsifat = ''
            count +=1
        ################################################## 
        # agar so`z bazadan topilsa lekin qo`shimchasi topilmasa va turkumi boshqa bo`lsa`   
        if count == 0:
            if len(inturkum) > 0:
                root_3.append('Input:'+i+'->Root word: '+invword+"->Turkum: "+inturkum) 
                #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
                inputl.append(i)
                rootl.append(invword)
                turkuml.append(inturkum)
                suffixl.append("NONE")
                analizl.append("NONE")
                #for syntactic purpose, enter into kist, every morphological analzed morphome (NOUN, VERB, SUFFIX)
                invword = ''
                inturkum = ''
                sifatstem = ''
                diffsifat = ''
                analizsifat = ''
                numberstem = ''
                diffnumber = ''
                analiznumber = ''
                olmoshstem = ''
                diffolmosh = ''
                analizolmosh = ''
                felstem = ''
                difffel = ''
                analizfel = ''
                otstem = ''
                diffot = ''
                analizot = ''
            else:
                root_3.append('Input:'+i+'->Root word: NOT FOUND FROM DB')
                inputl.append(i)
                rootl.append("NONE")
                turkuml.append("NONE")
                suffixl.append("NONE")
                analizl.append("NONE")
                sifatstem = ''
                diffsifat = ''
                analizsifat = ''
                numberstem = ''
                diffnumber = ''
                analiznumber = ''
                olmoshstem = ''
                diffolmosh = ''
                analizolmosh = ''
                felstem = ''
                difffel = ''
                analizfel = ''
                otstem = ''
                diffot = ''
                analizot = ''
                invword = ''
                inturkum = ''     
        ##############################################
        #agar so`z bazadan topilsa lekin qo`shimchasi topilmasa va turkumi boshqa bo`lsa
        count = 0
        invword = ''
        inturkum = ''
        sifatstem = ''
        diffsifat = ''
        analizsifat = ''
        numberstem = ''
        diffnumber = ''
        analiznumber = ''
        olmoshstem = ''
        diffolmosh = ''
        analizolmosh = ''
        felstem = ''
        difffel = ''
        analizfel = ''
        otstem = ''
        diffot = ''
        analizot = '' 
    #######################################################
    # syntactic start here###############################################    
    syn = ''
    synkesim = ''
    synhol = ''
    synaniqlovchi = ''
    synega = ''
    syntoldiruvchi = ''
    index = 0
    inputl2 = list()
    turkumuz = ''            
    inputl2 = inputl.copy()
    totalNumber = len(rootl)

    while index < len(rootl):
        syn += "["+inputl2[index]+"->"+turkuml[index]+"->"+rootl[index]+"->"+suffixl[index]+"]"
        if turkuml[index] == 'ADJ' or turkuml[index] == 'ADJECTIVE':
            turkumuz += "sifat+"
        if turkuml[index] == 'ADP' or turkuml[index] == 'ADP':
            turkumuz += "komakchi+"
        if turkuml[index] == 'ADV' or turkuml[index] == 'ADVERB':
            turkumuz += "ravish+"
        if turkuml[index] == 'AFF' or turkuml[index] == 'AFF':
            turkumuz += "bolishli+"
        if turkuml[index] == 'CONJ' or turkuml[index] == 'CONJr':
            turkumuz += "boglama+"
        if turkuml[index] == 'EXL':
            turkumuz += "undovsoz+"
        if turkuml[index] == 'limit':
            turkumuz += "taqlid+"
        if turkuml[index] == 'MW' or turkuml[index] == 'mw':
            turkumuz += "modalsoz+" 
        if turkuml[index] == 'NOUN' or turkuml[index] == 'VOUN':
            c = 0
            if inputl2[index].endswith("ning") :
                c += 1
                turkumuz += "ot+ning+"
            elif inputl2[index].endswith("ga"):
                c += 1
                turkumuz += "ot+ga+"
            elif inputl2[index].endswith("dagi"):
                c += 1
                turkumuz += "ot+dagi+"
            elif inputl2[index].endswith("da"):
                c += 1
                turkumuz += "ot+da+"
            elif inputl2[index].endswith("ga"):
                c += 1
                turkumuz += "ot+ga+"
            elif inputl2[index].endswith("ni"):
                c += 1
                turkumuz += "ot+ni+"
            elif inputl2[index].endswith("dan"):
                c += 1
                turkumuz += "ot+dan+"
            elif inputl2[index].endswith("man"):
                c += 1
                turkumuz += "ot+man+"
            if c == 0:
                turkumuz += "ot+"
            c = 0    
        if turkuml[index] == 'NUM' or turkuml[index] == 'NUMBER':
            c = 0
            if inputl2[index].endswith("dan"):
                c += 1
                turkumuz += "son+dan+"
            if c == 0:
                turkumuz += "son+"
            c = 0
        if turkuml[index] == 'P' or turkuml[index] == 'PRONOUN':
            c = 0
            if inputl2[index].endswith("ning") :
                c += 1
                turkumuz += "olmosh+ning+"
            if inputl2[index].endswith("da") :
                c += 1
                turkumuz += "olmosh+da+"
            if inputl2[index].endswith("ga") :
                c += 1
                turkumuz += "olmosh+ga+"
            if inputl2[index].endswith("ni"):
                c += 1
                turkumuz += "olmosh+ni+"
            if c == 0:
                turkumuz += "olmosh+"
            c = 0
        if turkuml[index] == 'Part' or turkuml[index] == 'PART':
            turkumuz += "yuklama+"
        if turkuml[index] == 'V_N':
            turkumuz += "harakatnomi+" 
        if turkuml[index] == 'V_O':
            turkumuz += "sifatdosh+" 
        if turkuml[index] == 'V_P':
            turkumuz += "ravishdosh+"
        if turkuml[index] == 'V_PASS':
            turkumuz += "majhul+"
        if turkuml[index] == 'V' or turkuml[index] == 'verb' or turkuml[index] == 'VERB':
            c = 0
            if inputl2[index].endswith("man"):
                c += 1
                turkumuz += "fel+man+"
            if inputl2[index].endswith("da"):
                c += 1
                turkumuz += "fel+da+"
            if c == 0:
                turkumuz += "fel+"
            c = 0
        index += 1

    modelcount = 0
    modelcount2 = 0
    getModel = ''
    for x in model:
        modelcount += 1
        if x['model'] == turkumuz[:-1]:
            turkumuz += "topildi"
            getModel = x['model2']
 
    getModel2 = getModel.split("+")
    getModel3 = str(getModel2).split("]") 
    c1 = 0;
    synega2 = ''
    for xy in getModel3:
        xy = xy.replace("'", "")
        xy = xy.replace(",", " ")
        xy = xy.replace("[", " ")  
        if len(xy) > 0:
            c1 += 1
            res = [int(i) for i in xy.split() if i.isdigit()]
            xy = '' .join((z for z in xy if not z.isdigit()))
            for v in res:
                synega2 += inputl2[v]+" "
            if len(synega2) > 0:
                synega2+= "=>["+xy.replace(" ", "")+"] "
            #syntantic.append(synega2)
    if len(synega2) > 0:
        syntantic.append(synega2)
    if len(synega2) == 0:
        syntantic.append("Model topilmadi")
    if syn != '':
        return syntantic
        synega = ''
        synhol = ''
        synaniqlovchi = ''
        syntoldiruvchi = ''
        synkesim = ''
    else:
        return 'xato'
        synega = ''
        synhol = ''
        synaniqlovchi = ''
        syntoldiruvchi = ''
        synkesim = ''
    #return root_3  
def findOtSuffix2(suffix, inputsuffix):
    analizot = ''
    go =''
    model = ''
    analizot1= ''
    count = 0
    l = list()
    for gword in inputsuffix:
        go += gword
        for o in suffix:
            analizot1 = o['suffix']
            if go == analizot1: 
               analizot += go+'+'
               model += o['tegi']+'+'
               go = ''

    return analizot+model 

def findOtSuffix(suffix, inputsuffix):
    analizot = ''
    model = ''
    analizot1= ''
    inputsuffix1 = ''
    l = list()
    for gword in inputsuffix:
        inputsuffix1 = inputsuffix.replace(analizot1, "", 1)#remove found suffixes
        if len(inputsuffix) == 0:
            break
        else:   
            analizot1 += AnalizSuffix(suffix, inputsuffix1)#add found suffixes
            l.append(AnalizSuffix(suffix, inputsuffix1))#add to list found suffixes
            while '' in l:
                l.remove("")#remove empty value

    for x in l:
        analizot += x+"+"
        for o in suffix:
            if x == o['suffix']:
                model += o['tegi']+"+"
    #if len(inputsuffix1) > 0:
    #   return ''
    #else:
    return analizot[:-1]+" Modeli: ->"+model[:-1]     

def AnalizSuffix(suffix, inputsuffix):#search longest end then return
    go = ''
    analizot = ''
    model = ''
    for x in inputsuffix:
        go += x
        for o in suffix:
            model = o['suffix']
            if go == model: 
               analizot = go
               model = o['tegi']

    return analizot