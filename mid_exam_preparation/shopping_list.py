def shopping_list(budget, **kwargs):
    basket = 0
    products = []
    if budget < 100:
        return "You do not have enough budget."
    else:
        for product_name, product_info in kwargs.items():
            if basket == 5:
                break
            product_price, product_quantity = product_info
            total_price = product_price * product_quantity
            if budget >= total_price:
                products.append(f"You bought {product_name} for {total_price:.2f} leva.")
                budget -= total_price
                basket += 1
    return "\n".join(products)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
