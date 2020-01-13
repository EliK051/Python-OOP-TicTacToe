# new_tuple=(6,5,{'lamp':'on','gas':"off"},(3,4),[1,2],'dad','a',7)

# print(new_tuple[3])
# print(new_tuple[-4])

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
removed=list(days)
removed.remove("Tuesday")
print(removed)
tuple(removed)
print(removed)

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# new_tuple=()
# for i in range(1,len(numbers)+1):
#     new_tuple+=(numbers[-i],)
#
# print(new_tuple)