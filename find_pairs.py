categories = []

categories.append('/corner')
categories.append('/freekick/close')
categories.append('/freekick/far')
categories.append('/heading')
categories.append('/pass')
categories.append('/shoot/bicycle')
categories.append('/shoot/goal')
categories.append('/shoot/goalpost')
categories.append('/shoot/kept')
categories.append('/shoot/out')
categories.append('/tackle/foul')
categories.append('/tackle/poke')
categories.append('/tackle/sliding')
categories.append('/touch')

class Pairs():
	def __init__(self):
		self.pairs = []
		
	def add(self,p1,p2):
		if p1 < p2:
			stradded = '%s-%s' % (p1,p2)
			
			if not (stradded in self.pairs):
				self.pairs.append(stradded)
		else:
			stradded = '%s-%s' % (p2,p1)
			
			if not (stradded in self.pairs):
				self.pairs.append(stradded)
				
	def numOfPairs(self):
		return len(self.pairs)
		
	def printPairs(self):
		print 'Olasi ikilikler: '
		
		for pair in self.pairs:
			print pair
			
		print ''
		print 'Ikilik sayisi = %d' % self.numOfPairs()
		
pairs = Pairs()

pairs.add('/corner','/freekick/far')
pairs.add('/corner','/pass')
pairs.add('/corner','/shoot/kept')
pairs.add('/corner','/tackle/poke')
pairs.add('/touch','/heading')
pairs.add('/touch','/pass')
pairs.add('/touch','/tackle/sliding')
pairs.add('/tackle/sliding','/freekick/far')
pairs.add('/tackle/sliding','/pass')
pairs.add('/tackle/sliding','/tackle/foul')
pairs.add('/tackle/poke','/shoot/kept')
pairs.add('/tackle/poke','/pass')
pairs.add('/tackle/poke','/freekick/far')
pairs.add('/tackle/poke','/tackle/foul')
pairs.add('/tackle/poke','/shoot/goal')
pairs.add('/tackle/poke','/corner')
pairs.add('/tackle/foul','/tackle/sliding')
pairs.add('/tackle/foul','/tackle/poke')
pairs.add('/tackle/foul','/freekick/close')
pairs.add('/shoot/out','/pass')
pairs.add('/shoot/goalpost','/pass')
pairs.add('/shoot/goal','/tackle/poke')
pairs.add('/shoot/goal','/freekick/close')
pairs.add('/shoot/goal','/pass')
pairs.add('/shoot/goal','/shoot/bicycle')
pairs.add('/shoot/bicycle','/shoot/goal')
pairs.add('/shoot/kept','/tackle/poke')
pairs.add('/shoot/kept','/pass')
pairs.add('/shoot/kept','/heading')
pairs.add('/pass','/shoot/kept')
pairs.add('/pass','/shoot/goal')
pairs.add('/pass','/shoot/goalpost')
pairs.add('/pass','/shoot/out')
pairs.add('/pass','/tackle/poke')
pairs.add('/pass','/tackle/sliding')
pairs.add('/pass','/touch')
pairs.add('/pass','/corner')
pairs.add('/pass','/heading')
pairs.add('/pass','/freekick/far')
pairs.add('/heading','/pass')
pairs.add('/heading','/touch')
pairs.add('/heading','/shoot/kept')
pairs.add('/freekick/far','/corner')
pairs.add('/freekick/far','/tackle/sliding')
pairs.add('/freekick/far','/tackle/poke')
pairs.add('/freekick/far','/pass')
pairs.add('/freekick/close','/shoot/kept')
pairs.add('/freekick/close','/tackle/poke')
pairs.add('/freekick/close','/shoot/goal')
pairs.add('/freekick/close','/tackle/foul')

pairs.printPairs()
