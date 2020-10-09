data = []
new =[]
wc = {}	 # word_count
# 檔案讀取
def read_file(filename):	
	count = 0
	with open(filename, 'r') as f:
		for line in f:
			data.append(line)
			count += 1 #count = count + 1
			if count % 1000 == 0: # (%是用來求餘數) 跟1000求餘數如果餘數是0 才列為計算
				print(len(data))
	print('檔案讀取完了,總共有', len(data), '筆資料')

# 計算平均字數
def word_avg():
	sum_len = 0
	for d in data:
		sum_len += len(d) # (sum_len + led(d))
	print('留言的平均長度為', sum_len/len(data))


# 縮小範圍
def narrwo():
	num = input('請輸入您想要查詢的留言長度範圍: ')
	for d in data:
		if len(d) < int(num):
			new.append(d)
	print('一共有', len(new), '筆留言長度小於', num)
	print(new[0])
	print(new[1])


# 文字計數
def word_count():
	
	for d in data:
		words = d.split()
		for word in words:
			times = 1
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1
	return wc


# 鎖定範圍(印出num範圍內文字)
def take_range():
	num = input('請輸入你所要查詢的出現次數: ')
	for word in wc:
		if wc[word] > int(num):
			print(word,wc[word])
	print(len(wc))


# 搜索功能
def word_serch():
	while True:
		word = input('請問你想查甚麼字:')
		if word == 'q':
			break
		if word in wc:
			print(word, '出現過的次數為: ', wc[word])
			continue
		else:
			print('這個字沒有出現過喔!')
			continue
		

# 執行
def main():
	read_file('reviews.txt')
	word_avg() 
	narrwo()
	word_count()
	take_range()
	word_serch()
	print('感謝使用本軟體')

main()