from django.db import models
from core.models import BaseModel
from Users.models import User

class Coupon(BaseModel):
    """
    A model representing a coupon.

    Attributes:
        coupon_code (CharField): The code of the coupon.
        validity (IntegerField): The validity period of the coupon in days.
    """

    coupon_code = models.CharField(max_length=50)
    validity = models.IntegerField(null=True)

    def __str__(self) -> str:
        """
        Returns the string representation of the coupon, which is the coupon code.

        Returns:
            str: The coupon code.
        """
        return self.coupon_code


class CouponRedeem(BaseModel):
    """
    A model representing the redemption of a coupon by a user.

    Attributes:
        user (ForeignKey): The user who redeemed the coupon.
        coupon (ForeignKey): The coupon that was redeemed.
        redeem_date (DateField): The date the coupon was redeemed.
    """

    user = models.ForeignKey(User, related_name="usercoupons", on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, related_name="coupons", on_delete=models.CASCADE)
    redeem_date = models.DateField(default=False)

    def __str__(self) -> str:
        """
        Returns the string representation of the coupon redemption, which is the coupon code.

        Returns:
            str: The coupon code.
        """
        return str(self.coupon)
