extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

principal = 500000.0
rate = 0.05
minimum = 2684.11
total_paid = 0.0
month = 1

while principal > 0:
    payment = minimum
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment = minimum + extra_payment

    amount_owing = principal * (1+rate/12)

    if payment >= amount_owing:
         payment = amount_owing

    principal = amount_owing - payment
    total_paid = total_paid + payment

    print(f"{month} {total_paid:.2f} {principal:.2f}")
    month += 1

formatted_total = f'${total_paid:.2f} over {month} months'

print('Total paid', formatted_total)
