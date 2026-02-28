import json
orders=[
  {
    "order_id": 1,
    "user": "Ali",
    "items": ["phone", "case"],
    "total": 300000
  },
  {
    "order_id": 2,
    "user": "Dana",
    "items": ["laptop"],
    "total": 800000
  },
  {
    "order_id": 3,
    "user": "Ali",
    "items": ["mouse", "keyboard"],
    "total": 70000
  }
]
with open("orders.json","w", encoding="utf-8") as f:
    json.dump(orders,f,indent=4)

import json
with open("orders.json","r", encoding="utf-8") as f:
  orders = json.load(f)
total_revenue=0
user_orders={} #әр қолданушы неше заказ жасағаны
items={}
top_user=""
most_popular_item=""
max_orders=0
for order in orders:
  total_revenue += order["total"]
  user=order["user"]  #заказдан адамның атын аламыз
  user_orders[user]=user_orders.get(user,0)+1
  if order["total"]>max_orders:
    max_orders=order["total"]
    top_user=user
  for item in order["items"]:
    items[item]=items.get(item,0)+1
most_popular_item=max(items,key=items.get)
summary={
  "total_revenue":total_revenue,
  "top_user":top_user,
  "most_popular_item":most_popular_item,
  "total_orders":len(orders),
}
with open("summary.json", "w", encoding="utf-8") as f:
  json.dump(summary, f, indent=4)


