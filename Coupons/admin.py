from django.contrib import admin
from .models import Coupon, CouponRedeem

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Coupon model.
    
    Displays the ID, coupon code, and validity in the list view.
    """
    list_display = ['id', 'coupon_code', 'validity']


@admin.register(CouponRedeem)
class CouponRedeemAdmin(admin.ModelAdmin):
    """
    Admin interface options for the CouponRedeem model.
    
    Displays the ID, user, coupon, and redeem date in the list view.
    """
    list_display = ['id', 'user', 'coupon', 'redeem_date']
