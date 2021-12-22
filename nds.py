# расчет ставки НДС при начислении и выделении НДС, а также самой величины НДС

print(f"Приветствую! Здесь можно рассчитать ставку НДС для выделения и начисления")
print(f"А также можно просто рассчитать процент от числа :)")
nds_percent = input("Введите ставку НДС(процент): ")
nds_percent = float(nds_percent)
stavka_nds = nds_percent / 100
stavka_nds = float(stavka_nds)

nds_plus_one = stavka_nds + 1.0


def nds_equation_plus_summa(summa):
    nds_eq = summa * stavka_nds
    result_plus = summa + nds_eq
    return result_plus


def nds_equation_plus_nds(summa):
    nds_eq = summa * stavka_nds
    return nds_eq


def nds_equation_minus_summa(summa):
    summa_bez_nds = summa / nds_plus_one
    result_minus = summa - summa_bez_nds
    return result_minus


def nds_equation_minus_nds(summa):
    summa_bez_nds = summa / nds_plus_one
    return summa_bez_nds


summa = input("Введите сумму: ")
summa = float(summa)

operation = input("Введите операцию (+ или -): ")

if operation == '+':
    result = nds_equation_plus_summa(summa)
    print(f"Ваша сумма с начисленным НДС составляет: ")
    print(result)
    result2 = nds_equation_plus_nds(summa)
    print(f"Сумма НДС: ")
    print(result2)
elif operation == '-':
    result = nds_equation_minus_summa(summa)
    result2 = nds_equation_minus_nds(summa)
    print(f"Ваша сумма с выделенным НДС составляет: ")
    print(result2)
    print(f"Сумма НДС: ")
    print(result)
else:
    print(f"Вы ввели некорректную операцию!")
