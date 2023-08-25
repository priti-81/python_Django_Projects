from html import unescape

encoded_string = "[&#x27;Parking&#x27;, &#x27;Tubewel&#x27;]"
decoded_string = unescape(encoded_string)
print(decoded_string)
