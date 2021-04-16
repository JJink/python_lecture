def triangle_area() :
    width = float(input("밑변 길이: "))
    height = float(input("높이 : "))
    TA = (width * height)*(1/2)
    return(TA)

print(triangle_area())


def area_circum():
    radius = float(input("원의 반지름을 입력하세요 : "))
    area = radius * radius * 3.14 
    circum = 2 * radius * 3.14
    return area, circum
print(area_circum())
