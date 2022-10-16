print('Bonus Report')
print('================================================')
print('Name       SirName    Dept              Bonus ')
print('================================================')
def main():
    emp = open('Employee.txt', 'r')
    point = open('WorkPoints.txt','r')
    dep = open('DepartmentRate.txt','r')

    employee1 = emp.read()
    employee1 = employee1.split('\n')

    work_point1 = point.read()
    work_point1 = work_point1.split()

    dep_rate1 = dep.read()
    dep_rate1 = dep_rate1.split()

    index = 1
    index_point = 1
    listbonus = []
    sumtotal = 0

    while index < len(employee1):
        print(employee1[index].ljust(10),employee1[index+1].ljust(10),employee1[index+2].ljust(10),end=''.ljust(7))
        for w in work_point1:
            if w == employee1[index-1]:
                point_1 = int(work_point1[index_point])

                for d in dep_rate1:
                    if d == employee1[index+2]:
                        rate1 = int(dep_rate1[dep_rate1.index(d)+2])
                        rate2 = int(dep_rate1[dep_rate1.index(d)+1])
        
                bonus = (point_1-40)*rate1+40*rate2
                listbonus.append(bonus)
                print('{:,}'.format(bonus)+".00")

        index += 4
        index_point += 2

    for sum in listbonus:
        sumtotal += sum

    print('================================================')
    print('Total Bonus'.ljust(37), '{:,}'.format(sumtotal)+".00")
    print('================================================')
    emp.close()
    point.close()
    dep.close()

main()