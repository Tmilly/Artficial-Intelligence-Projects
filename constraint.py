from z3 import *

results = []

while(True):
	n = 0
	m = 0

	n, m = map(int, input().split())


	members = [Int('x%s' % i) for i in range(n)]

	if n == 0 and m == 0:
		break

	committeeMax = 1
	s = z3.Solver()

	#possible committee
	f =  Function('f', IntSort(), IntSort())

	x = Int('x')
	s.push()


	#adding constraints for each pair that cant work together
	for i in range(0, m):

		#input
		member1, member2 = map(int, input().split())

		#member1 and member2 cannot be in the same committee
		s.add(f(members[member1 - 1]) != (f(members[member2 - 1])))


		#Constraint: possible committee for member1 and 2 must be less than or equal to x  
		s.add(f(members[member1 - 1]) <= x)
		s.add(f(members[member2 - 1]) <= x)

		#Constraint: possible committee for member1 and 2 must be more than 0
		s.add(f(members[member1 - 1]) > 0)
		s.add(f(members[member2 - 1]) > 0)
	

	#checker
	#print(committeeMax)
	#print(n)
	while committeeMax <= n:
		s.push()
		s.add(x == committeeMax)	
		if s.check() == z3.sat:
			results.append(committeeMax)
			break	
		else: 
			committeeMax += 1
			s.pop()
	s.pop()

for result in results:
	print(result)