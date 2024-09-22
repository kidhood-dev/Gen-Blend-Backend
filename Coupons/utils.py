from .models import CouponRedeem
from datetime import datetime

def get_coupen(user):
    coupon_redeemed = CouponRedeem.objects.filter(user=user).first()
    if coupon_redeemed:
        if coupon_redeemed.redeem_date >= datetime.now():
            return True
    return False