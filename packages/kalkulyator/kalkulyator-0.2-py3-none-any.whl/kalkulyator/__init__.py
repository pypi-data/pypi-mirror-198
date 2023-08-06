def syntacticAnaliz(self, inputW, root, OT, FEL, OLMOSH, NUMBER, SIFAT, model):
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
        
        if len(inputW) > 1:
            for i in inputW:
                i = i.replace(',', '')
                num = isinstance(i, int)
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

            egasiz = 0
            #model
            model = [
                {"model": "sifat+ot+ot+ning+ot+komakchi+ot+ga+fel", "model2": "aniqlovchi[0]+ega[1]+aniqlovchi[2]+to‘ldiruvchi[3]+kesim[4,5]", }, #1
                {"model": "olmosh+ot+ot+ning+olmosh+komakchi+sifat+komakchi+ot+ning+ot+ga+sifat", "model2": "aniqlovchi[0]+ega[1]+aniqlovchi[2]+to‘ldiruvchi[3,4]+aniqlovchi[5,6]+aniqlovchi[7]+to‘ldiruvchi[8]+kesim[9] "},#2
                {"model": "ot+ot+son+ot+ot+ot+ning+ot+ot+dagi+ot+ot+da+ot+fel", "model2": "ega[0,1]+hol[2,3]+aniqlovchi[4,5]+aniqlovchi[6,7,8]+hol[9]+kesim[10,11]"},#3
                {"model": "sifat+ot+ni+ravishdosh+ot+ot+ot+ning+ot+ot+da+ot+fel", "model2": "aniqlovchi[0]+to‘ldiruvchi[1]+hol[2]+aniqlovchi[3,4,5]+aniqlovchi[6]+hol[7]+kesim[8,9]"},#4
                {"model": "ot+ot+ot+ning+ot+da+fel", "model2": "aniqlovchi[0,1]+aniqlovchi[2]+hol[3]+kesim[4]"},#5
                {"model": "olmosh+ning+ot+fel+ot+ga+ot+son+sifat+ot+son+ot+da+fel+fel", "model2": "aniqlovchi[0]+aniqlovchi[1,2,3,4,5,6]+ega[7]+hol[8,9]+kesim[10,11]"},#6
                {"model": "ot+ot+da+ot+ot+ning+ot+ravish+sifat+fel", "model2": "hol[0,1]+aniqlovchi[2,3]+ega[4]+hol[5,6]+kesim[7]"},#7
                {"model": "ot+dagi+ravish+sifat+ot+ot+ot+ot+da+fel", "model2": "hol[0]+aniqlovchi[1,2]+ega[3,4]+aniqlovchi[5]+hol[6]+kesim[7]"},#8
                {"model": "ot+dagi+ravish+sifat+ot+ot+ning+sifat+ot+da+fel", "model2": "hol[0]+aniqlovchi[1,2]+ega[3]+aniqlovchi[4]+hol[5,6]+kesim[7]"},#9
                {"model": "ot+ot+sifat+ot+ot+ni+ot+ni+fel", "model2": "aniqlovchi[0]+ega[1]+aniqlovchi[2]+to‘ldiruvchi[3,4,5]+kesim[6]"},#10
                {"model": "sifat+sifat+son+ot+ot+dan+son+son+dan+sifat+ot+harakatnomi+boglama", "model2": "aniqlovchi[0,1]+hol[2,3]+to‘ldiruvchi[4]+hol[5,6,7]+ega[8]+kesim[9,10]"}, #11
                {"model": "ot+ot+ot+ot+dagi+ot+ot+ning+son+ot+ni+fel", "model2": "ega[0,1]+aniqlovchi[2]+hol[3]+aniqlovchi[4,5]+hol[6]+to‘ldiruvchi[7]+kesim[8]"}, #12
                {"model": "ravish+son+ot+ot+sifatdosh+ot+ot+da+son+dan+sifat+ot+fel", "model2": "aniqlovchi[0,1,2,3,4]+aniqlovchi[5]+hol[6]+aniqlovchi[7,8]+ega[9]+kesim[10]"}, #13
                {"model": "sifat+ot+da+sifat+ot+ni+ot+komakchi+son+son+ot+ot+ot", "model2": ""}, #14
                {"model": "olmosh+ot+ot+da+ravish+ravish+ot+ga+ot+ga+ot+fel", "model2": ""}, #15
                {"model": "olmosh+sifat+ot+ni+ot+ot+ni+qoshmafel", "model2": ""}, #16
                {"model": "olmosh+sifat+ot+ning+sifat+ot+man", "model2": "ega[0]+aniqlovchi[1,2] + aniqlovchi[3] + kesim[4]"}, #17
                {"model": "olmosh+olmosh+ni+olmosh+ot+ravish+ravish+ot+fel+man", "model2": "ega[0]+to‘ldiruvchi[1]+hol[2,3,4]+hol[5]+kesim[6]"}, #18
                {"model": "kirishsoz+olmosh+ot+ot+man", "model2": ""}, #19
                {"model": "ravish+ot+ot+boglama+sifat+ot+ot+da+fel+man", "model2": "hol[0]+hol[1,2,3,4,5,6]+kesim[7]"}, #20
                {"model": "sifat+fel+man", "model2": "aniqlovchi[0] + kesim[1]"}, #21
                {"model": "olmosh+ni+sifat+ot+ot+ot+ot+komakchi+sifat+ot+dan+fel", "model2": ""}, #22
                {"model": "ot+ot+ot+ot+ot+ot+ni+olmosh+da+sifatdosh+ot+ot", "model2": "ega[0] + aniqlovchi[1,2,3,4] + to‘ldiruvchi[5] + aniqlovchi[6,7] + kesim[8,9]"}, #23
                {"model": "olmosh+sifat+ot+ravish+ravish+sifat+sifat+boglama", "model2": ""}, #24
                {"model": "son+ot+da+ravish+fel+fel+man", "model2": "hol[0] + to‘ldiruvchi[1] + hol[2] + kesim[3,4]"}, #25 
                {"model": "olmosh+ot+ot+da+ot+ning+qoshmafel+boglama", "model2": ""}, #26
                {"model": "olmosh+ot+ot+ot+ning+ot+da+modalsoz", "model2": "aniqlovchi[0]+ega[1,2]+aniqlovchi[3]+hol[4]+kesim[5]"}, #27
                {"model": "olmosh+ot+ni+sifat+ot+fel+ravish+ot+fel", "model2": ""}, #28
                {"model": "ot+ot+sifat+ot+ot+sifat+ot+ning+sifat+qoshmafel", "model2": ""}, #29
                {"model": "ot+da+fel+da+sifat+ot+ning+ot+da+fel", "model2": ""}, #30
                {"model": "olmosh+ot+dan+ibora+fel", "model2": ""}, #31
                {"model": "olmosh+iot+dan+ot+ning+son+olmosh+ga+ibora+sifat+komakchi+fel", "model2": ""}, #32
                {"model": "ot+ot+ot+ot+da+olmosh+ga+ot+ravish+sifat+fel", "model2": ""}, #33
                {"model": "olmosh+ot+ot+da+ot+da+ravish+iot+ning+ot+dan+fel", "model2": ""}, #34
                {"model": "ot+ot+ot+da+sifat+ot+ot+ot+ot+ni+fel", "model2": ""}, #35
                {"model": "ravish+sifat+ot+ni+ravishdosh+ot+ni+fel", "model2": "hol[0] + aniqlovchi[1] + to‘ldiruvchi[2] + hol[3] + to‘ldiruvchi[4] + kesim[5]"}, #36
                {"model": "ot+ning+ot+da+isifat+ot+ning+ot+ni+fel+boglama", "model2": ""}, #37
                {"model": "ravish+ot+da+ot+olmosh+ot+ga+fel", "model2": ""}, #38
                {"model": "ot+olmosh+sifat+sifat+ot+ot+ot+komakchi+isifat+ot", "model2": ""}, #39
                {"model": "ravish+ot+da+ot+dan+sifat+fel+boglama", "model2": "hol[0,1] +to‘ldiruvchi[2] + aniqlovchi[3] + to‘ldiruvchi[4] +kesim[5,6]"}, #40
                {"model": "ot+olmosh+son+ot+ot+da+fel+yuklama+sifat+ot+harakatnomi+boglama", "model2": ""}, #41
                {"model": "ot+ot+ga+ot+da+ot+dan+ravish+fel", "model2": "ega[0] + hol[1,2] + to‘ldiruvchi[3] + hol[4] + kesim[5]"}, #42
                {"model": "ot+sifat+ot+ning+sifat+ot+da+fel", "model2": "ega[0] + hol[1,2,3,4] + kesim[5]"}, #43
                {"model": "boglovchi+ot+ot+da+olmosh+ot+ning+son+dan+son+ot+fel", "model2": ""}, #44
                {"model": "ot+ning+ot+ot+ga+ot+komakchi+ravish+ot+da+ot+ning+ot+ni+fel", "model2": ""}, #45
                {"model": "boglama+olmosh+ot+sifat+ot+ot+komakchi+ravish+son+ot+fel+da", "model2": "bog‘lovchi[0] + aniqlovchi[1] + ega[2] + to‘ldiruvchi[3,4,5,6] +hol[7,8,9] + kesim[10]"}, #46
                {"model": "sifat+ot+ni+olmosh+ravish+ravish+fel", "model2": ""}, #47
                {"model": "sifat+ot+da+ot+sifat+ot+ni+ot+komakchi+ravish+ravish+fel", "model2": "aniqlovchi[0] + to‘ldiruvchi[1] + to‘ldiruvchi[2,3,4,5,6] + hol[7,8] + kesim[9]"}, #48
                {"model": "ot+ot+ot+ning+ot+ni+sifat+ot+ni+fel", "model2": ""}, #49
                {"model": "ot+ot+dagi+sifat+ot+sifat+ot+ga+komakchi+ravish+ravish+fel+olmosh+ga+sifat", "model2": "aniqlovchi[0,1] + aniqlovchi[2] + aniqlovchi[3] + aniqlovchi[4] + to‘ldiruvchi[5] + ko‘makchi[6] + aniqlovchi[7] + ega[8,9] + to‘ldiruvchi[10] + kesim[11]"}, #50
                {"model": "ot+ning+ot+fel+ga+ot+yuklama+olmosh+harakatnomi+boglama", "model2": ""}, #51
                {"model": "ot+ga+ravishdosh+ot+fel+sifat", "model2": ""}, #52
                {"model": "ot+ot+da+fel+komakchi+ot+sifatdosh+sifat+ot+ot+ot+da+fel", "model2": ""}, #53
                {"model": "sifat+ot+ning+ravish+ravish+harakatnomi", "model2": ""}, #54
                {"model": "ot+yuklama+sifat+ot+ni+harakatnomi+ot+komakchi+fel", "model2": ""}, #55
                {"model": "sifat+ot+dagi+ot+ni+olmosh+ot+ni+ot+komakchi+ot+dan+fel", "model2": ""}, #56
                {"model": "ot+ot+ot+ning+ot+ot+da+harakatnomi+da+sifat+sifat+ot+ning+sifat+ot+fel", "model2": ""}, #57
                {"model": "undalma+olmosh+olmosh+ni+sifat+ot+ga+sifatdosh+sifat+ot+sifat+ot", "model2": ""}, #58
                {"model": "sifat+ot+ning+ot+ni+ravishdosh+ot+ot+komakchi+sifatdosh+yuklama+olmosh", "model2": ""}, #59
                {"model": "olmosh,+ot+son+ga+fel", "model2": ""}, #60
                {"model": "sifat+ot+ga+boglovchi+sifat+ot+ga+sifat+fel", "model2": ""}, #61
                {"model": "olmosh+ot+olmosh+ot+ot+ni+sifat+ot+ot+ni+fel", "model2": ""}, #62
                {"model": "sifat+fel+ot+da+harakatnomi+ot+da++sifat+ot+fel", "model2": ""}, #63
                {"model": "olmosh+ot+ot+ning+ot+ot+ga+sifat+ot+ot++ot+da+fel", "model2": ""}, #64
                {"model": "ot+ning+ot+ot+ot+ning+ot+da+fel", "model2": ""}, #65
                {"model": "olmosh+olmosh+sifatdosh+ot+da+sifat+ot+ot+fel+boglovchi+sifat+ot+fel", "model2": ""}, #66
                {"model": "ot+da+ot+da+sifat+ot+ga+sifat+son+ot+ot+ni+ot+ga+harakatnomi+sifat+toliqsizfel", "model2": ""}, #67
                {"model": "olmosh+ning+ot+ot+ot+dadi+ot+ni+olmosh+ot+da+sifatdosh+komakchi+fel", "model2": ""}, #68
                {"model": "ot+ravish+ot+fel",  "model2": ""}, #70
                ]
            #model
   
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
                    '''
                    if modelcount == 1:
                        synega += inputl2[0]+" [aniqlovchi] "+inputl2[1]+" [ega] "+inputl2[2]+" [aniqlovchi] "+inputl2[3]+" [to`ldiruvchi] "+inputl2[4]+" "+inputl2[5]+" [kesim] "
                    elif modelcount == 2:
                        synega += inputl2[0]+" [aniqlovchi] "+inputl2[1]+" [ega] "+inputl2[2]+" [aniqlovchi] "+inputl2[3]+" "+inputl2[4]+" [to`ldiruvchi] "+inputl2[5]+" "+inputl2[6]+" "+inputl2[7]+" "" [aniqlovchi]"+inputl2[8]+" [to`ldiruvchi]"+inputl2[9]+" [kesim]"
                    elif modelcount == 3:
                        synega += inputl2[0]+" "+inputl2[1]+" [ega] "+inputl2[2]+" "+inputl2[3]+" [hol] "+inputl2[4]+" "+inputl2[5]+" [aniqlovchi] "+inputl2[6]+" "+inputl2[7]+" "+inputl2[8]+" [aniqlovchi]"+inputl2[9]+" [hol]"+inputl2[10]+" "+inputl2[11]+" [kesim]"
                    else: 
                        synega += inputl2[0]+"[bog`lovchi]"+inputl2[1]+" "+inputl2[2]+" [hol] "+inputl2[3]+" "+inputl2[4]+"[aniqlovchi] "+inputl2[5]+" "+inputl2[6]+" "+inputl2[7]+"[ega] "+inputl2[8]+"[kesim]"
                    ''' 
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
                    synega2+= "=>["+xy.replace(" ", "")+"] "
                    #syntantic.append(synega2)
            syntantic.append(synega2)
            while index < len(rootl):
                syn += "["+inputl2[index]+"->"+turkuml[index]+"->"+rootl[index]+"->"+suffixl[index]+"]"
                sanoq = 0
                #ega topish juft so`zlar`
                #shaxs songa qarab egani topish
                if inputl[totalNumber-1].endswith("im") or inputl[totalNumber-1].endswith("sam") or inputl[totalNumber-1].endswith("man") or inputl[totalNumber-1].endswith("m") and index == 0:  
                    if len(synega) == 0:
                        for i in range(len(inputl)):
                            if inputl[i] == 'men' or inputl[i] == 'man' or inputl[i] == 'kamina':
                                synega += inputl[i]+" (Ega_1)"
                                #if len(synaniqlovchi) == 0:
                                #    for j in range(i):
                                #        synaniqlovchi += inputl[j]+"(aniqlovchi)"
                
                #kesimni topish
                if index == totalNumber-1:
                    if inputl[index] == 'ekanmi' or inputl[index] == 'ekan':
                        if len(synkesim) == 0:
                            if turkuml[index-2] == 'VERB':
                                synkesim += inputl[index-2]+" "+inputl[index-1]+" "+inputl[index]+"(Kesim)"
                            else:
                                synkesim += inputl[index-1]+" "+inputl[index]+"(Kesim)"

                
                index += 1
                
            #syntactic start here
            if egasiz > 0 and len(synega) == 0:
                    synega += '(Egasiz gap!)' 
            syntantic.append(syn) 
            syntantic.append(turkumuz) 
            syntantic.append(synega+" "+synhol+" "+synaniqlovchi+" "+syntoldiruvchi+" "+synkesim) 
            #syntantic.append(getModel)
            #syntantic.append(getModel2)
            #syntantic.append(getModel3)
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
        else:
            for x in inputW: 
                a += x.strip() 
                a.strip() 
                stem.append(x)
                for y in stem:
                    for x1 in y:
                        yx += x1
                        count = 2; #change to 0, our db table starts with id 2
                        for r in root:
                            count += 1    
                            if yx == r['lotin']: 
                                if r['turkum'] == 'NOUN' or r['turkum'] == 'VOUN':
                                    otstem = yx 
                                elif r['turkum'] == 'VERB':
                                    felstem = yx
                                elif r['turkum'] == 'P':
                                    olmoshstem = yx
                                elif r['turkum'] == 'NUM':
                                    numberstem = yx
                                elif r['turkum'] == 'ADJ':
                                    sifatstem = yx
                                elif r['turkum'] == 'CONJ':
                                    boglamastem = yx
                                else:
                                    invword = yx
                                    inturkum = r['turkum']
            
                #########################################
                diffboglama = x.replace(boglamastem, "")#get suffix ot
                if diffboglama == boglamastem:
                    diffboglama = ''
                diffot = x.replace(otstem, "")#get suffix ot
                if diffot == otstem:
                    diffot = ''
                difffel = x.replace(felstem, "")#get suffix fel
                if difffel == felstem:
                    difffel = ''
                diffolmosh = x.replace(olmoshstem, "")#get suffix fel
                if diffolmosh == olmoshstem:
                    diffolmosh = ''
                diffnumber = x.replace(numberstem, "")#get suffix fel
                if diffnumber == numberstem:
                    diffnumber = ''
                diffsifat = x.replace(sifatstem, "")#get suffix fel
                if diffsifat == sifatstem:
                    diffsifat = ''
                ###############################################
                root_3.append(x)
                analizsifat = ''
                analiznumber = ''
                analizolmosh = ''
                analizfel = ''
                analizot = '' 
                if len(otstem) > len(boglamastem) and len(otstem) > len(felstem) and len(otstem) > len(olmoshstem) and len(otstem) > len(numberstem) and len(otstem) > len(sifatstem):
                    analizot = findOtSuffix(OT, diffot)      
                if len(felstem) > len(boglamastem) and len(felstem) > len(otstem) and len(felstem) > len(olmoshstem) and len(felstem) > len(numberstem) and len(felstem) > len(sifatstem):                
                    analizfel = findOtSuffix(FEL, difffel)   
                if len(olmoshstem) > len(boglamastem) and len(olmoshstem) > len(otstem) and len(olmoshstem) > len(felstem) and len(olmoshstem) > len(numberstem) and len(olmoshstem) > len(sifatstem):                
                    analizolmosh = findOtSuffix(OLMOSH, diffolmosh)
                if len(numberstem) > len(boglamastem) and len(numberstem) > len(felstem) and len(numberstem) > len(olmoshstem) and len(numberstem) > len(otstem) and len(numberstem) > len(sifatstem):
                    analiznumber = findOtSuffix(NUMBER, diffnumber)      
                if len(sifatstem) > len(boglamastem) and len(sifatstem) > len(felstem) and len(sifatstem) > len(olmoshstem) and len(sifatstem) > len(numberstem) and len(sifatstem) > len(otstem):
                    analizsifat = findOtSuffix(SIFAT, diffsifat)
                ###############################################
                count = 0;
                #agar so`z topils va qo`shimchasi bo`lsa va qo`shimcha bazadagi qo`shimchalarga mos kelsa` 
                if len(analizot.replace(" Modeli: ->", "")) > 0 and len(otstem) > 0:
                    root_3.append('Input:'+x+'->Root word: '+otstem+"->Turkum: NOUN"+'->Suffix:'+diffot+"->Analiz noun:"+analizot)
                    count +=1
                if len(analizfel.replace(" Modeli: ->", "")) > 0 and len(felstem) > 0:  
                    root_3.append('Input:'+x+'->Root word: '+felstem+"->Turkum: VERB"+'->Suffix:'+difffel+"->Analiz Verb:"+analizfel)    
                    count +=1
                if len(analizolmosh.replace(" Modeli: ->", "")) > 0 and len(olmoshstem) > 0:  
                    root_3.append('Input:'+x+'->Root word: '+olmoshstem+"->Turkum: PRONOUN"+'->Suffix:'+diffolmosh+"->Analiz Pronoun:"+analizolmosh)    
                    count +=1
                if len(analiznumber.replace(" Modeli: ->", "")) > 0 and len(numberstem) > 0:  
                    root_3.append('Input:'+x+'->Root word: '+numberstem+"->Turkum: NUMBER"+'->Suffix:'+diffnumber+"->Analiz Num:"+analiznumber)    
                    count +=1
                if len(analizsifat.replace(" Modeli: ->", "")) > 0 and len(sifatstem) > 0:  
                    root_3.append('Input:'+x+'->Root word: '+sifatstem+"->Turkum: ADJECTIVE"+'->Suffix:'+diffsifat+"->Analiz ADJ:"+analizsifat)       
                    count +=1
                #agar so`z topils va qo`shimchasi bo`lsa va qo`shimcha bazadagi qo`shimchalarga mos kelsa` 
                
                #agar so`z bazada topilsa va qo`shimchasi bo`lmasa
                if len(diffboglama) == 0 and len(boglamastem) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
                    root_3.append('Input:'+x+'->Root word: '+boglamastem+"->Turkum: CONJ"+'->Suffix: NONE->Analiz CONJ: NONE')
                    count +=1
                if len(diffot) == 0 and len(otstem) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
                    root_3.append('Input:'+x+'->Root word: '+otstem+"->Turkum: NOUN"+'->Suffix: NONE->Analiz Noun: NONE')
                    count +=1
                if len(difffel) == 0 and len(felstem) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
                    root_3.append('Input:'+x+'->Root word: '+felstem+"->Turkum: VERB"+'->Suffix: VERB->Analiz Noun: NONE')
                    count +=1
                if len(diffolmosh) == 0 and len(olmoshstem) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
                    root_3.append('Input:'+x+'->Root word: '+olmoshstem+"->Turkum: PRONOUN"+'->Suffix: NONE->Analiz Pronoun: NONE')
                    count +=1
                if len(diffnumber) == 0 and len(numberstem) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
                    root_3.append('Input:'+x+'->Root word: '+numberstem+"->Turkum: NUMBER"+'->Suffix: NONE->Analiz NUMBER: NONE')
                    count +=1
                if len(diffsifat) == 0 and len(sifatstem) > 0 and count == 0:#agar so`z bazada topilsa va qo`shimchasi bo`lmasa
                    root_3.append('Input:'+x+'->Root word: '+sifatstem+"->Turkum: ADJ"+'->Suffix: NONE->Analiz ADJ: NONE')
                    count +=1
                ################################################## 
                # agar so`z bazadan topilsa lekin qo`shimchasi topilmasa va turkumi boshqa bo`lsa`   
                if count == 0:
                    if len(inturkum) > 0:
                        root_3.append('Input:'+x+'->Root word: '+invword+"->Turkum: "+inturkum) 
                    else:
                        root_3.append('Input:'+x+'->Root word: NOT FOUND FROM DB')     
                ##############################################
                #agar so`z bazadan topilsa lekin qo`shimchasi topilmasa va turkumi boshqa bo`lsa
                if x != 'none':
                    return root_3
                else:
                    return ''
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