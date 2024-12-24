#Практическое задание по теме: "Словари и множества"
#словари
my_dict={'Dima':1984,'Milya':1995, 'Sasha':2010,'Mila':2011}
print('my dict:',my_dict)
print("Existing value:",my_dict['Dima'])
#my_dict['Masha']=1988
print('Not existing value:',my_dict.get('Masha'))
my_dict.update({'Harley':2014,'Polina':2000})
x=my_dict.pop('Polina')
print('Deleted value:',x)
print('Modified dictionary',my_dict)
print( )
#Множества
my_set={1,2,3,4,"apple",x,2,3,x}
print('my_set:',my_set)
my_set.add(5)
my_set.update((6,7,8))
my_set.discard(1)
print('my_set_update:',my_set)


