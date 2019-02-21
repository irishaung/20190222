mathscores = [10,4,56,44,89,10,7]
print(mathscores[3])
print(mathscores[2:4])
print(mathscores[-1]) #倒數1個
print(mathscores[:5])
print(mathscores[5:])
print(mathscores[-2:])
print(len(mathscores)) #數字的長度
print(sum(mathscores)) #總和
print(max(mathscores))
print(min(mathscores))
apple=sum(mathscores) /len(mathscores)
print (apple)
ls = []
ls.append(7)
ls.append(10)
ls.append(8)
print(ls)
ls.insert(2,10)
print(ls)
mathscores = [10,4,56,44,89,10,7]
del mathscores[1:3]
print( mathscores)
print(2 in mathscores)
print(10 in mathscores)
mathscores = [10,4,56,44,89,10,7]
print(mathscores.count(4))
mathscores = [10,4,56,44,89,10,7]
mathscores.remove(10)
print(mathscores)

ls = ['a','b','c']
print(mathscores + ls)
ls =[[1,5],[8,7],5,5]
#print(ls[0])
print(ls[1][0]) #先外層在內層
print(sorted(mathscores))  #由小排大
grades = [[5,14,7],[23,36,28],[88,80,92]] #隨練
print(grades[2])
print(sum(grades[0])/3)
print(sum(grades[1])/3)
print(sum(grades[2])/3)
science =[94,90,96]  #grades.append({94,90,96}) #print(grades)
print(grades + science) #因為是加上去的所以一個一個+
#tuple()
turple3 =('lisa',23,'female')
name,age,sex=turple3
print(name,age,sex)
print(turple3[0:2])
gradestuple=((5,14,7),(23,36,28),(88,80,92))
print(gradestuple[2])
print(sum(gradestuple[0])/3)
print(sum(gradestuple[1])/3)  #右鍵然後refector在rename可以取代
print(sum(gradestuple[2])/3) #(,)就好 #append無法執行
gradestuple+=((94,90,96),) #tuple無法更改 因此這行為+=為tuple=turple+94,90,96
print(gradestuple)
family ={}
family['dad'] = 'homer'
print(family)
family['dad'] = 'iris'
print(family)

print(family.get('mom'))
print(family.pop('dad'))
family.update({'mom':'lisa','Son':'je'})
print(family)

gradesDict ={'chinese':[5,14,17],'english':[23,36,28],'math':[88,80,92]}
print(gradesDict['math'])
mathscores=(sum(gradesDict['chinese'])/3)
print(mathscores)
englishscores=(sum(gradesDict['english'])/3)
print(englishscores)
chinesescores=(sum(gradesDict['chinese'])/3)
print(chinesescores)

allStudents={'John','Eva','Jill','Eric','Andy','Albert','Polina','Kristin','Angle'}
guitarClub={'John','Eva','Jill','Eric','Andy'}
danceClub={'Andy','Eric','Albert','Polina','Kristin'}
print(guitarClub&danceClub)
print(guitarClub-danceClub)
print(allStudents-(guitarClub|danceClub))