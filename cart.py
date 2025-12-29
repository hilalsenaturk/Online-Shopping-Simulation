from decimal import Decimal, ROUND_HALF_UP

def add_to_cart(cart: dict, product: dict, quantity: int):
    product_id = product['id']
    stock = product['stock']
    if 'items' not in cart:
        cart ['items'] = []
    if product_id not in cart['items']:
        cart['items'] = {}
    current_quantity = cart['items'][product_id]['quantity']
    if current_quantity + quantity > stock:
        print(f"Error: not enough stock for {product_id}")
        return cart
    if product_id in cart['items']:
        cart['items'][product_id]['quantity'] += quantity
    else: cart['items']['product_id'] = {
        'id' : product ['id'],
        'name' : product ['name'],
        'price' :product ['price'],
        'stock' : stock,
        'quantity': quantity,
    }
    print(f"You added {quantity} {product_id} to cart.  ")
    return cart

def remove_from_cart(cart: dict, product_id: str):
    if 'items' in cart and product_id in cart['items']:
        del cart['items'][product_id]
        print(f"You removed {product_id} from cart.")
    else:
        print(f"Error: not enough stock for {product_id}")
        return cart

def update_quantity(cart: dict, product_id: str , quantity: int):
    if 'items' in cart and product_id in cart['items']:
        if quantity <= 0:
            return remove_from_cart(cart, product_id)
        cart['items'][product_id]['quantity'] = quantity
        print(f"You updated {product_id} quantity to {quantity}")
    else:
        print(f"Error: not enough stock for {product_id}")
    return cart

def calculate_totals(cart: dict, tax_rate: float, discounts: list):
    total = 0
    if 'items in cart' in cart:
        for item in cart['items'].values():
            total += item['price'] * item['quantity']
    cart['total'] = total

    discount_amount = 0
    for discount in discounts:
        if discount['type'] == 'percent':
            discount_amount += total * discount['amount']
        elif discount['type'] == 'amount':
            discount_amount += discount['amount']
    cart['discount_amount'] = discount_amount
    total -= discount_amount

    tax_amount = total * tax_rate
    cart['tax_amount'] = tax_amount
    return cart

