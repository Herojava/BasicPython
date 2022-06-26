class Stock():

	def __init__(self, name, business, marketCap):

		self.name = name
		self.business = business
		self.marketCap = marketCap

	def stock_details(self):

		if self.marketCap >= 100000:
			size = 'หุ้นขนาดใหญ่'
		elif self.marketCap >= 50000:
			size = 'หุ้นขนาดกลาง'
		else:
			size = 'หุ้นขนาดเล็ก'

		print(f'{self.name} อยู่ในกลุ่ม {self.business} มี Market cap {self.marketCap:,.2f} ล้านบาท')
		print(f'ดังนั้น {self.name} จึงเป็น{size}')

class SET50(Stock):
	def __init__(self, name, business, marketCap, ranking):

		super().__init__(name, business, marketCap)
		self.ranking = ranking

	def rank(self):

		print(f'{self.name} เป็นหุ้นลำดับที่ {self.ranking} ของ SET50 ตาม Market Cap')

	def stock_details(self):

		print(f'{self.name} เป็นหุ้นขนาดใหญ่ใน SET50 มี Market Cap {self.marketCap:,.2f} ล้านบาท')




if __name__ == '__main__':

	stock1 = Stock('PTT', 'Energy', 949719.63)
	stock1.stock_details()
	stock3 = Stock('TMD', 'Industru/Packaging', 3735.00)
	stock3.stock_details()

	print('---------------------------------------')
	print('---------------------------------------')

	stock2 = SET50('ADVANC', 'Tele', 600790.37, 4)
	stock2.stock_details()
	stock2.rank()	