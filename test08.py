def showProgramName() :
    print('   โปรแกรมตรวจสอบความเป็นเด็ก หนุ่ม หรือแก่--**')

def inputData() :
    name = input('ป้อนชื่อ : ')
    age = int(input('ป้อนอายุ : '))
    return name, age

def checkShowStatus ( name, age ) :
    if age <= 18 :
        print(f'คุณ{name} อายุ {age} ปี เป็นเด็ก')
    elif age >= 19 and age <= 45 :
        print(f'คุณ{name} อายุ {age} ปี เป็นคนหนุ่ม')
    else :
        print(f'คุณ{name} อายุ {age} ปี เป็นนคนแก่')

print('------------------------------')
showProgramName()
print('------------------------------')
name, age = inputData()
print('------------------------------')
checkShowStatus( name, age)
print('------------------------------')
