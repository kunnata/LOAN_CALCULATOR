import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['annuity', 'diff'])
parser.add_argument('--principal', type=float, help='loan principal')
parser.add_argument('--periods', type=int, help='number of payments')
parser.add_argument('--interest', type=float, help='interest')
parser.add_argument('--payment', type=float, help='annuity monthly payment ')
args = parser.parse_args()
alist = []


def end_foo(number):
    non_letter = ''
    letter = 's'
    if number > 1:
        return letter
    else:
        return non_letter


def number_of_periods(p, a, i):  # (loan Principal, Annuity monthly payment, loan Interest)
    i = i / (12 * 100)
    n = math.ceil(math.log((a / (a - i * p)), (1 + i)))
    o = math.ceil(a * n - p)
    year = n // 12
    month = n % 12
    if month == 0:
        print(f'It will take {year} year{end_foo(year)} to repay this loan!')
        print(f'Overpayment = {o}')
        return
    elif year == 0:
        print(f'It will take {month} month{end_foo(month)} to repay this loan!')
        print(f'Overpayment = {o}')
        return
    else:
        print(f'It will take {year} year{end_foo(year)} and\
        {month} month{end_foo(month)} to repay this loan!')
        print(f'Overpayment = {o}')
        return


def annuity_monthly_payment(p, n, i):  # (Loan principal, Number of payments, Loan interest)
    i = i / (12 * 100)
    a = math.ceil(p * (i * pow((1 + i), n)) / (pow((1 + i), n) - 1))
    o = math.ceil(a * n - p)
    print(f'Your annuity payment = {a}!')
    print(f'Overpayment = {o}')
    return


def loan_principal(a, n, i):  # (annuity Payments, Number of periods, loan Interest)
    i = i / (12 * 100)
    p = a / ((i * pow((1 + i), n)) / (pow((1 + i), n) - 1))
    o = math.ceil(a * n - p)
    print(f'Your loan principal = {int(p)}!')
    print(f'Overpayment = {o}')
    return


def different_monthly_payment(p, n, i):
    sum_d = 0
    i = i / (12 * 100)
    for m in range(1, n + 1):
        d = math.ceil(p / n + i * (p - (p * (m - 1) / n)))
        print(f'Month {m}: payment is {d}')
        sum_d += d
        m += 1
    o = math.ceil(sum_d - p)
    print(f'Overpayment = {o}')
    return


for arg in vars(args):
    if getattr(args, arg) is not None:
        alist.append(getattr(args, arg))
if args.interest is None or args.type not in ("diff", "annuity") or len(alist) != 4:
    print("Incorrect parameters")

elif args.type == 'annuity':
    if args.periods is None:
        number_of_periods(args.principal, args.payment, args.interest)
    elif args.payment is None:
        annuity_monthly_payment(args.principal, args.periods, args.interest)
    elif args.principal is None:
        loan_principal(args.payment, args.periods, args.interest)

elif args.type == 'diff':
    if args.principal is not None:
        different_monthly_payment(args.principal, args.periods, args.interest)
