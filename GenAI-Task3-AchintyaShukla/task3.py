# Task 3 - Lambda Function: GST Calculator

# lambda function to add 18% gst
gst = lambda price: price + (0.18 * price)

print("100 with GST is", gst(100))
print("500 with GST is", gst(500))

# extra: final price after discount and GST
# applying discount first then GST
gst_and_discount = lambda price, discount: (price - (price * discount / 100)) * 1.18

print("100 with 10% discount and GST is", gst_and_discount(100, 10))
