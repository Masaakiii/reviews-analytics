data = []
count = 0
with open('reviews.txt', 'r') as f:
	 for line in f:
	 	 data.append(line)
	 	 count += 1 #count = count + 1
	 	 if count % 1000 == 0: # (%是用來求餘數) 跟1000求餘數如果餘數是0 才列為計算
	 	 	print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')
# print(data[0])


sum_len = 0
for d in data:
	sum_len += len(d) # (sum_len + led(d))
print('留言的平均長度為', sum_len/len(data))


new =[]
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '比留言長度小於100')
print(new[0])
print(new[1])


#文字計數
wc = {}	 # word_count
for d in data:
	words = d.split()
	for word in words:
		times = 1
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])

print(len(wc))

while True:
	word = input('請問你想查甚麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用本軟體')



