
import re
import re


def return_cart_items(items):

    cart_lists = {'items_count': 0, 'Total_amount': 0}
    if len(items)>1:
        for item in items:
            if 'item' in item.lower():
                number = re.findall(r'\d+', item)
                cart_lists['items_count'] = int(number[0]) if number else 0
        cart_lists['Total_amount'] = items[-1]
    return cart_lists

