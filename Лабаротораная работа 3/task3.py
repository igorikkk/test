salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев
delta = spend - salary
while months != 0:
    delta = spend - salary
    money_capital += delta
    spend *= 1 + increase
    months -= 1



# TODO Оформить решение

print(round(money_capital))
