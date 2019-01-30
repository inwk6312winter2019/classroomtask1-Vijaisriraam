class myMac():
	"""this is a class creating and storing mac addresses"""
	def __init__(self,maclist=[0x00,0x00,0x00,0x00,0x00,0x00]):
		self.mlist=maclist
	
thispc=myMac()

def printmac(somemac):
	print(thispc.mlist)

class cellphone():
	def __init__(self,pname,pmodel):
		self.name=pname
		self.macadd=myMac([0xFF,0xFF,0xFF,0xFF,0xFF,0xFF])
		self.model=pmodel

class ipaddress():
	def __init__(self,mname,mmodel):
		self.name=mname
		self.ipadd=myMac([0xFF,0xFF,0xFF,0xFF])
		self.model=mmodel

printmac(thispc)

newphone=cellphone('raghu','MTA23C')
print(newphone.name)

myphone=ipaddress('vijai','IPXS')
print(myphone.name)

printmac(newphone.macadd)
printmac(myphone.ipadd)
