# NOTE: these are methods for the BSTree class


def get_all_products(self, root, products):
    """Return list of tuples with productid and number of orders for each
    productid.
    i.e. [(productid, count), ...]
    """
    if root is not None:
        self.get_all_products(root.Lptr, products)
        products.append((root.productid, root.orders.size()))
        self.get_all_products(root.Rptr, products)

    return products


def most_popular(self):
    products = self.get_all_products(self.Root, list())

    # sort products in descending order of order count
    for i in range(len(products)-1):
        for j in range(len(products)-1-i):
            if products[j][1] < products[j+1][1]:
                temp = products[j]
                products[j] = products[j+1]
                products[j+1] = temp

    # get product(s) with highest orders
    highest_orders = products[0][1]
    best_selling_prods = list()
    for product in products:
        no_of_orders = product[1]
        if no_of_orders == highest_orders:
            productid = product[0]
            best_selling_prods.append(productid)
        else:
            break

    print("Best-sellers:", ', '.join(best_selling_prods))


# tree.most_popular()
