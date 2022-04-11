from pointer import DB

q = DB()
print(q.ask("select * from sakila.actor "))
print(q.ask("select * from sakila.address"))


print()