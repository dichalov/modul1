#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var =(1,2,3,4,'war','peace')
print(immutable_var)
#immutable_var[1]=11
# получим TypeError: 'tuple' object does not support item assignment
# т.к. кортеж не изменить
mutable_var=[1,2,3,4,"кружка", "ложка","миска", "нож"]
print(mutable_var)