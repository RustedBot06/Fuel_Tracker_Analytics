#FOR INPUT VALIDATION

class ValidationError(Exception):
    pass

def validate_price(price):
    if price <= 0:
        raise ValidationError(
            "Price must be greater than 0."
        )

def validate_amount(amount):
    if amount <= 0:
        raise ValidationError(
            "Fuel amount must be greater than 0."
        )

def validate_odometer(odometer, prev_odo):
    if odometer <= 0 and odometer < prev_odo:
        raise ValidationError(
            "Odometer reading must be greater than 0."
        )

def validate_full_refill_flag(flag):
    if flag not in [0, 1]:
        raise ValidationError(
            "Full refill flag must be 0 or 1."
        )