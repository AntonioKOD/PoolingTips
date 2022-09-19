
lst = []

n = int(input("Enter the amount of cash: "))

for i in range(0,n):
    ele = int(input())
    lst.append(ele)


sum = 0


for i in range(0, len(lst)):
    sum += lst[i]

print(sum)

cash_tips = int(input("Enter cash tips: "))

if cash_tips < 0:
    sum += cash_tips

if cash_tips > 0:
    sum -= cash_tips

print(sum)

busser = sum * 0.15

sum -= busser

food_runner = busser / 3

sum -= food_runner

print(f"Bussers: {busser}")
print(f"Food Runner: {food_runner}")
print(sum)

number_of_servers = int(input('Number of servers: '))
servers = []
hours = []

total_hours = 0

for i in range(0, number_of_servers):
    server_name = input("Enter the server's name: ")
    hours_worked = float(input("How many hours worked: "))
    servers.append(server_name)
    hours.append(hours_worked)
    total_hours += hours_worked

zip_together = zip(servers, hours)
make_dict = dict(zip_together)

hourly_rate = sum / total_hours
list_of_money = []

for money in make_dict.values():
    total = hourly_rate * money
    format_total = "{:.1f}".format(total)
    list_of_money.append(format_total)

print(f"Hourly Rate is: {hourly_rate}")
print(f"Total hours worked: {total_hours}")

zip_again = zip(servers, list_of_money)
final_dict = dict(zip_again)

for name, value in final_dict.items():
    print(f"{name} gets {value}")


