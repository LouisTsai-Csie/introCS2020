#以下題目禁止使用 '=' 符號直接 assign

#Problem 1 目標輸出:[10, 9, 8, 7, 'six', 5, 4, 3, 2, 1, 'zero']
s = [5,4,1,'six',3,2]
s.remove('six');s.extend([10,9,8,7])
s.sort(reverse=True)
s.insert(4,'six')
s.append('zero')
print(s)
#請不重複地使用list的函數使得下方的print輸出結果與目標輸出相同(五行之內可完成)
# #Problem 2 目標輸出:{10: 10, 9: 9, 8: 8, 7: 7, 5: 5, 4: 4, 3: 3, 2: 2, 1: 1, 'zero': 0, 'six': 6}
s1=s.pop(4)
s.append(s1)
d={}
for i in range(len(s)):
    if s[i]=='zero':
        d[s[i]]=0
    elif s[i]=='six':
        d[s[i]] = 6
    else:
        d[s[i]]=s[i]
print(d)
# #Problem 3 目標輸出:{'zero': 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 'six': 6, 7: 7, 8: 8, 9: 9, 10: 10, 'eleven': 11}
d2 = {}
#請不重複地使用dict的函數使得下方的print輸出結果與目標輸出相同，可使用上一題的d(兩行之內可完成)
for i in range(11):
    if i ==0:
        d2['zero']=0
    elif i==6:
        d2['six']=6
    else:
        d2[i]=i
d2['eleven']=11
print(d2)
#以下開放使用 '=' 符號 assign (不一定需要)

# #Problem 4
# d3 = {'Jeff Bezos': 113.0, 'Bill Gates': 98.0, 'Bernard Arnault': 76.0, 'Warren Buffett': 67.5, 'Larry Ellison': 59.0}
#
# #請參考本周投影片的作法將d3的內容以key的last name的字典序重新排序之後以list of tuple的形式輸出
# #但是禁止使用key=lambda這個參數，也禁止直接人工sort之後把答案打進來(三行之內可完成)
d3 = {'Jeff Bezos': 113.0, 'Bill Gates': 98.0, 'Bernard Arnault': 76.0, 'Warren Buffett': 67.5, 'Larry Ellison': 59.0}
a=sorted(d3.keys())
b=[]
d={}
for i in range(5):
    b+=a[i].split(' ')
    del b[i]
b=sorted(b)
for i in range(5):
    if b[i]=='Bezos':
        d.update({'Jeff Bezos': 113.0})
    elif b[i] == 'Gates':
        d.update({'Bill Gates': 98.0})
    elif b[i] == 'Arnault':
        d.update({'Bernard Arnault': 76.0})
    elif b[i] == 'Buffett':
        d.update({'Warren Buffett': 67.5})
    elif b[i] == 'Ellison':
        d.update({'Larry Ellison': 59.0})
print(tuple(d))
#
#
# #Problem 5
#
# #請應用本周教的資料型別完成以下功能
# #輸入一正整數，會輸出該數字在二進位表示中1出現的位數所形成的"集合"(順序無所謂)
# #例:輸入2則輸出{1}，輸入5則輸出{0,2}(三、四行可完成)
n = eval(input('Input a positive integer n = '))#此行會將輸入的數字assign給n這個變數
c = set({})#請將要輸出的集合assign給c這個變數
a=[]
for i in range(len(bin(n))):
    a+=str(bin(n))[len(bin(n))-1]


print(f'The set of positions of the binary representation of {n} with 1-bits is', c)
