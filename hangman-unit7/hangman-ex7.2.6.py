def main():
    str_of_products = input("Enter a list of products for shopping: ")
    products = str_of_products.split(",")
    with_out_duplicate_list = []
    
    while True:
        print("\n=== MENU ===")
        print("1. Print the list of products")
        print("2. Print the number of products in the list")
        print("3. Check if a product is on the list")
        print("4. Count how many times a certain product appears")
        print("5. Delete a product from the list")
        print("6. Add a product to the list")
        print("7. Print all invalid products")
        print("8. Remove all duplicates from the list")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nList of products:")
            for product in products:
                print("- " + product)
        elif choice == "2":
            print("\nNumber of products:", len(products))
        elif choice == "3":
            product_name = input("\nEnter a product name to check if it's on the list: ")
            if product_name in products:
                print("Yes, the product is on the list.")
            else:
                print("No, the product is not on the list.")
        elif choice == "4":
            product_name = input("\nEnter a product name to count how many times it appears: ")
            count = products.count(product_name)
            print("The product appears", count, "times in the list.")
        elif choice == "5":
            product_name = input("\nEnter a product name to delete from the list: ")
            if product_name in products:
                products.remove(product_name)
                print("The product has been deleted from the list.")
            else:
                print("The product is not on the list.")
        elif choice == "6":
            product_name = input("\nEnter a product name to add to the list: ")
            products.append(product_name)
            print("The product has been added to the list.")
        elif choice == "7":
            print("\nInvalid products:")
            valid = True
            for product in products:
                if len(product) < 3 or not product.isalpha():
                    print("- " + product)
                    valid = False
            if valid:
                print("all of the products are valid!")
        elif choice == "8":
            for product in products:
                if not(product in with_out_duplicate_list):
                    with_out_duplicate_list.append(product)
            products = with_out_duplicate_list
            with_out_duplicate_list = []
            print("\nAll duplicates have been removed from the list.")
        elif choice == "9":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 9.")
    

if __name__ == "__main__":
    main()