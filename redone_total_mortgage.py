# author: Steven De Jesus
# assignment : 5 redo

# define main
def main():
    # call display title
    display_title()
    # gather inputs from user 
    principal = float(input('Principal $: '))
    # validation loops of course
    while principal < 0:
        print('Cannot be negative.')
        principal = float(input('Principal $: '))
    # gather inputs from user 
    annual_interest = float(input('Interest rate %: '))
    # validation loops of course
    while annual_interest < 1 or annual_interest > 10:
        print('Choose a reasonable interest rate.')
        annual_interest = float(input('Interest rate %: '))
    # gather inputs from user 
    term = int(input('Term (years): '))
    # validation loops of course
    while term < 5 or term > 30:
        print('Choose a reasonable year.')
        term = int(input('Term (years): '))
    # finally call total mortgage
    total_mortgage(principal, annual_interest, term)
    


# define total_mortgage
def total_mortgage(principal, annual_interest, term):
    # formula for total mortgage
    mortgage = principal * (1 + annual_interest/100) ** term
    print(f'Amount: ${mortgage:,.2f}')


# define display_title():
def display_title():
    print('-------------------')
    print('Mortgage Calculator')
    print('-------------------')

# call main
if __name__ == '__main__':
    main()