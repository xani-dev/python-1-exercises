def calc_total(arr,tax):
    total = sum(arr) 
    tax_percentage = float(tax.strip('%'))/100
    tax_amount = total * tax_percentage
    total_with_tax = total + tax_amount
    formatted_total = "${:,.2f}".format(total_with_tax)
    
    print(formatted_total)


        