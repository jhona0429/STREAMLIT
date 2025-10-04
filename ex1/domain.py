from decimal import Decimal, ROUND_HALF_EVEN, getcontext

getcontext().prec = 28

FEE_RATE = Decimal("0.014")
FEE_FIXED = Decimal("0.30")
MIN_PAYOUT = Decimal("1.00")

def _dec(x):
    return x if isinstance(x, Decimal) else Decimal(str(x))

def convert(amount: float, fx_rate: float) -> Decimal:
    amount = _dec(amount)
    fx_rate = _dec(fx_rate)

    if amount <= 0 or fx_rate <= 0:
        raise ValueError("Amount and FX rate must be greater than zero")

    gross = amount * fx_rate
    fee = gross * FEE_RATE + FEE_FIXED
    net = gross - fee
    rounded = net.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)

    if rounded < MIN_PAYOUT:
        raise ValueError("Below minimum payout")

    return rounded
